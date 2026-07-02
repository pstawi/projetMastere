# Objectif n°1 - Architecture cible du workflow (serveur dédié + Jenkins)

## 1. Principes de conception

- Conformité sujet : Jenkins comme CI principale, stack open source, exécution sous Linux avec Docker.
- Niveau d'ambition équilibré : robuste pour soutenance et exploitable, sans surcomplexifier.
- Séparation claire des environnements : dev, preprod, prod.
- Industrialisation via pipelines "pipeline as code".

## 2. Socle infrastructure (serveur dédié)

### 2.1 Hypothèse serveur

- OS : Ubuntu Server LTS
- Runtime : Docker Engine + Docker Compose
- Durcissement minimal : pare-feu, SSH par clé, fail2ban, mises à jour régulières

### 2.2 Segmentation logique

- Zone publique : reverse proxy (HTTPS)
- Zone outils internes : Jenkins, SCM, registry, monitoring
- Zone projets : stacks dev/preprod/prod
- Zone données : volumes persistants + sauvegardes

## 3. Briques retenues

- Reverse proxy : Traefik (TLS, routage par sous-domaines)
- CI : Jenkins (pipelines déclaratifs via Jenkinsfile)
- SCM : Gitea (dépôts + PR + webhooks Jenkins)
- Registry : Docker Registry (privée, authentifiée)
- Observabilité :
  - Prometheus (métriques)
  - Grafana (dashboards)
  - Uptime Kuma (supervision disponibilité)
- Sauvegardes :
  - Restic (snapshots chiffrés)
  - stockage distant (bucket S3-compatible ou NAS distant)

## 4. Nommage DNS recommandé

- `jenkins.wk-<classe>-<groupe>.fr`
- `git.wk-<classe>-<groupe>.fr`
- `registry.wk-<classe>-<groupe>.fr`
- `grafana.wk-<classe>-<groupe>.fr`
- `prometheus.wk-<classe>-<groupe>.fr`
- `app-dev.<domaine-projet>.fr`
- `app-preprod.<domaine-projet>.fr`
- `app.<domaine-projet>.fr`

## 5. Flux CI/CD cible

## 5.1 Déclencheurs

- Push sur branches de feature
- Pull request vers branche d'intégration
- Tag/release pour promotion versionnée

### 5.2 Étapes pipeline Jenkins

1. Checkout code
2. Lint + tests unitaires
3. Scan qualité (ex: SonarQube optionnel)
4. Build image Docker
5. Push image vers registry privée
6. Déploiement automatique dev
7. Tests d'intégration/smoke dev
8. Promotion automatique preprod
9. Validation manuelle
10. Déploiement prod + smoke test prod

### 5.3 Politique de déploiement

- Dev : automatique
- Preprod : automatique après qualité verte
- Prod : manuel (approval) + fenêtre de changement

## 6. Conventions opérationnelles

- Branching : GitFlow simplifié
  - `main` (stable prod)
  - `develop` (intégration)
  - `feature/*`, `release/*`, `hotfix/*`
- Versioning : SemVer (`MAJOR.MINOR.PATCH`)
- Secrets : variables Jenkins + fichiers chiffrés hors dépôt
- Rollback : redeploy de la dernière image stable taggée

## 7. Backups et continuité

### 7.1 Périmètre sauvegardé

- Volumes Jenkins, Gitea, registry, monitoring, bases applicatives
- Fichiers de configuration Compose / infra

### 7.2 Fréquence et rétention

- Snapshot quotidien + rétention glissante 30 jours
- Snapshot hebdomadaire longue conservation (12 semaines)

### 7.3 Test de restauration

- Test mensuel sur environnement isolé
- Vérification intégrité + temps de restauration

## 8. Sécurité minimale attendue

- TLS obligatoire (certificats Let's Encrypt)
- MFA sur outils critiques si disponible
- Comptes nominatifs + principe du moindre privilège
- Journalisation accès admin et actions sensibles
- Pas d'exposition directe des ports internes non nécessaires

## 9. Risques techniques et parades

- Point unique de défaillance serveur dédié  
Parade : sauvegardes externalisées + procédure de reconstruction rapide.
- Saturation stockage registry/logs  
Parade : politique de rétention images et logs.
- Dérive de configuration  
Parade : infrastructure déclarative et revue de changements.

## 10. Critères d'acceptation architecture

- Les outils clés sont accessibles via sous-domaines HTTPS.
- Un projet type peut être build, testé, containerisé et déployé dev/preprod/prod.
- Le rollback vers N-1 est démontré.
- Un test de restauration est exécuté et documenté.