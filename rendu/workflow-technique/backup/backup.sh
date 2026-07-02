#!/usr/bin/env bash
# Script de sauvegarde automatisee - Workflow Furious Ducks
# A planifier via cron (exemple quotidien 02h00) :
#   0 2 * * * /opt/workflow/backup/backup.sh >> /var/log/workflow-backup.log 2>&1
#
# Preuve attendue en soutenance : journal Restic + rapport de succes/echec + exercice de restauration mensuel.

set -euo pipefail

RESTIC_REPOSITORY="${RESTIC_REPOSITORY:?Variable RESTIC_REPOSITORY manquante (ex: s3:https://s3.exemple.fr/furious-ducks-backup)}"
RESTIC_PASSWORD="${RESTIC_PASSWORD:?Variable RESTIC_PASSWORD manquante}"
export RESTIC_REPOSITORY
export RESTIC_PASSWORD

DATE_JOUR=$(date +%F)
LOG_PREFIX="[backup-workflow][$DATE_JOUR]"

VOLUMES_A_SAUVEGARDER=(
  "/var/lib/docker/volumes/workflow-technique_jenkins_home/_data"
  "/var/lib/docker/volumes/workflow-technique_gitea_data/_data"
  "/var/lib/docker/volumes/workflow-technique_gitea_db/_data"
  "/var/lib/docker/volumes/workflow-technique_registry_data/_data"
  "/var/lib/docker/volumes/workflow-technique_prometheus_data/_data"
  "/var/lib/docker/volumes/workflow-technique_grafana_data/_data"
  "/opt/workflow"
)

echo "$LOG_PREFIX Debut de sauvegarde"

# 1) Verification etat des services (evite une sauvegarde partielle en pleine ecriture)
if ! docker ps --format '{{.Names}}' | grep -q "jenkins"; then
  echo "$LOG_PREFIX ALERTE: service jenkins non detecte, sauvegarde annulee" >&2
  exit 1
fi

# 2) Snapshot chiffre (Restic chiffre nativement le depot avec RESTIC_PASSWORD)
if restic snapshots >/dev/null 2>&1; then
  echo "$LOG_PREFIX Depot Restic existant detecte"
else
  echo "$LOG_PREFIX Initialisation du depot Restic"
  restic init
fi

echo "$LOG_PREFIX Snapshot des volumes critiques"
restic backup "${VOLUMES_A_SAUVEGARDER[@]}" \
  --tag "quotidien" \
  --tag "$DATE_JOUR"

# 3) Controle d'integrite (contre un echantillon pour rester rapide au quotidien)
echo "$LOG_PREFIX Controle d'integrite (echantillon 10%)"
restic check --read-data-subset=10%

# 4) Politique de retention : 30 jours glissants + 12 snapshots hebdomadaires
echo "$LOG_PREFIX Application de la politique de retention"
restic forget --keep-daily 30 --keep-weekly 12 --prune

echo "$LOG_PREFIX Sauvegarde terminee avec succes"

# 5) Rapport succes/echec (a brancher sur un webhook Uptime Kuma / alerting mail en cas d'echec du script)
exit 0
