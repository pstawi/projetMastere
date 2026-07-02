# Workflow-technique - Furious Ducks (Objectif n°1)

Ce dossier contient les **artefacts techniques prêts à déployer** du workflow de production décrit dans [`../CST_Objectif1_Furious_Ducks_FINAL.md`](../CST_Objectif1_Furious_Ducks_FINAL.md). Il illustre la faisabilité concrète des choix documentés dans le cahier, indépendamment de tout projet client particulier.

> **Important** : ces fichiers sont prêts à l'emploi mais nécessitent un serveur Linux + Docker réel, un nom de domaine et un stockage de sauvegarde distant pour être mis en ligne. Ils ne sont pas déployés automatiquement par cet agent - c'est à vous d'exécuter le déploiement si vous souhaitez le mettre en ligne (localement, sur un VPS, ou sur le serveur dédié retenu).

> **Périmètre** : la structure officielle du cahier des spécifications techniques (Objectif n°1) demande de spécifier et de concevoir le workflow, pas de fournir des preuves d'exécution réelle sur un projet client. Ce dossier reste donc autonome : les instructions ci-dessous sont fournies à titre d'illustration, pas comme une exigence bloquante pour l'Objectif 1.

## Contenu du dossier

| Fichier | Rôle | Section du cahier associée |
| --- | --- | --- |
| `docker-compose.yml` | Orchestration de toutes les briques du workflow (Traefik, Jenkins, Gitea, Registry, Prometheus, Grafana, Uptime Kuma) avec segmentation réseau par zone | F) Diagramme d'infrastructure, D.2) Choix techniques |
| `Jenkinsfile` | Pipeline déclaratif type, à copier dans le dépôt Gitea de chaque projet client | D.1/D.2) Analyse du workflow CI/CD, H.1) Procédure de déploiement |
| `traefik/traefik.yml` + `traefik/dynamic.yml` | Configuration du reverse proxy (routage par sous-domaine, TLS Let's Encrypt, middlewares de sécurité) | F) Diagramme d'infrastructure, E.5) Sécurité |
| `prometheus/prometheus.yml` | Configuration de collecte des métriques (Jenkins, Gitea, Registry, Traefik, environnements applicatifs) | E.1-E.3) Indicateurs et SLO/SLA |
| `backup/backup.sh` | Script de sauvegarde Restic (snapshot, contrôle d'intégrité, rétention 30j/12 semaines) | D.3) Hébergement et backups, H.2) Procédure de sauvegarde |
| `.env.example` | Variables d'environnement et secrets à renseigner (jamais commité une fois complété) | E.5) Sécurité et conformité |

## Mise en route locale (si vous choisissez de déployer le workflow)

1. Copier `.env.example` en `.env` et renseigner des valeurs réelles (domaine, mots de passe, dépôt de sauvegarde).
2. Générer le hash `htpasswd` pour protéger les outils sans authentification native (ex. Prometheus) et le reporter dans `traefik/dynamic.yml`.
3. Créer le dossier `registry/auth/` avec un fichier `htpasswd` pour sécuriser l'accès à la registry Docker.
4. Lancer la stack :

```bash
docker compose up -d
```

5. Vérifier que chaque service est accessible via son sous-domaine (`jenkins.<domaine>`, `git.<domaine>`, `registry.<domaine>`, `grafana.<domaine>`, `prometheus.<domaine>`, `status.<domaine>`).

## Sauvegarde/restauration (script fourni)

```bash
chmod +x backup/backup.sh
./backup/backup.sh
restic snapshots
```

## Limites connues

- Ce dossier ne fournit pas les scripts `ci/*.sh` référencés par le `Jenkinsfile` (lint, tests, quality-gate, deploy, smoke-test, rollback) : ils sont par nature spécifiques à la stack technique de chaque projet client géré par le workflow, et seront écrits projet par projet au fur et à mesure de leur arrivée.
- L'achat du nom de domaine, la location du serveur dédié et le paramétrage DNS restent à réaliser par vos soins (remplacer les placeholders `<classe>-<groupe>`).
- Les exporters `app-*-exporter` référencés dans `prometheus.yml` doivent être ajoutés (ex. `node-exporter` ou `cadvisor`) sur chaque environnement applicatif au fur et à mesure des projets clients gérés par le workflow.
