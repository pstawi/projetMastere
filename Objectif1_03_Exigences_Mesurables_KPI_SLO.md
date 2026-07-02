# Objectif n°1 - Exigences mesurables (KPI, SLO, SLA, RTO/RPO)

## 1) Objectif du document

Définir des seuils clairs, mesurables et vérifiables pour prouver l'efficacité du workflow de production.

## 2) Indicateurs CI/CD


| Domaine     | Indicateur                      | Cible           | Seuil d'alerte | Méthode de mesure           | Périodicité |
| ----------- | ------------------------------- | --------------- | -------------- | --------------------------- | ----------- |
| Build       | Durée moyenne pipeline standard | <= 12 min       | > 15 min       | Jenkins job metrics         | Hebdo       |
| Build       | Taux de succès pipeline         | >= 90 %         | < 85 %         | Jenkins (7 jours glissants) | Hebdo       |
| Qualité     | Taux de passages quality gate   | >= 85 %         | < 75 %         | Rapport qualité (ex Sonar)  | Hebdo       |
| Déploiement | Fréquence déploiements preprod  | >= 3 / semaine  | < 1 / semaine  | Historique Jenkins          | Hebdo       |
| Livraison   | Lead time commit -> preprod     | <= 1 jour ouvré | > 2 jours      | SCM + Jenkins timestamp     | Hebdo       |


## 3) Indicateurs tests


| Domaine           | Indicateur                             | Cible   | Seuil d'alerte | Méthode                |
| ----------------- | -------------------------------------- | ------- | -------------- | ---------------------- |
| Tests unitaires   | Couverture minimale (code critique)    | >= 70 % | < 60 %         | Outil de coverage      |
| Tests unitaires   | Taux de succès                         | >= 95 % | < 90 %         | Rapport pipeline       |
| Tests intégration | Taux de succès smoke tests dev/preprod | >= 98 % | < 95 %         | Étape post-déploiement |
| Régression        | Défauts critiques échappés en prod     | 0       | >= 1 / mois    | Suivi incidents        |


## 4) Disponibilité et exploitation (SLO/SLA)


| Service               | SLO disponibilité | Fenêtre de mesure | SLA interne | Preuve      |
| --------------------- | ----------------- | ----------------- | ----------- | ----------- |
| SCM (Gitea)           | 99.5 %            | Mensuelle         | 99.0 %      | Uptime Kuma |
| Jenkins               | 99.0 %            | Mensuelle         | 98.5 %      | Uptime Kuma |
| Registry              | 99.0 %            | Mensuelle         | 98.5 %      | Uptime Kuma |
| Reverse proxy         | 99.5 %            | Mensuelle         | 99.0 %      | Uptime Kuma |
| Environnement preprod | 99.0 %            | Mensuelle         | 98.5 %      | Sondes HTTP |


## 5) Sauvegarde et résilience


| Domaine          | Exigence cible             | Seuil d'échec        | Validation                        |
| ---------------- | -------------------------- | -------------------- | --------------------------------- |
| Fréquence backup | 1 sauvegarde/jour minimum  | Pas de backup > 24h  | Journal Restic                    |
| Rétention courte | 30 jours glissants         | < 21 jours effectifs | Politique backup                  |
| Rétention longue | 12 snapshots hebdomadaires | < 8 snapshots        | Inventaire snapshots              |
| RPO              | <= 24h                     | > 24h                | Contrôle date dernière sauvegarde |
| RTO              | <= 4h (services critiques) | > 6h                 | Exercice de restauration          |


## 6) Sécurité et conformité opérationnelle


| Domaine          | Exigence                          | Cible                       |
| ---------------- | --------------------------------- | --------------------------- |
| Accès            | Comptes nominatifs admin          | 100 % des accès admin       |
| Authentification | MFA activé si supporté            | 100 % des comptes sensibles |
| Secrets          | Aucun secret en clair dans dépôts | 0 occurrence                |
| Correctifs       | Patch de sécurité critiques       | < 7 jours                   |
| Traçabilité      | Journalisation actions admin      | 100 % des outils critiques  |


## 7) Critères "Go/No-Go" pour production

Un déploiement prod est autorisé seulement si :

- Pipeline vert (build, tests, quality gate).
- Image versionnée publiée en registry.
- Smoke test preprod validé.
- Validation manuelle enregistrée.
- Plan de rollback disponible.

## 8) Preuves minimales à annexer

- Captures Jenkins (durée, succès, historique jobs)
- Rapport de couverture de tests
- Export dashboard disponibilité (Uptime/Grafana)
- Journal des sauvegardes + preuve restauration
- Journal d'un rollback de démonstration

## 9) Revue de performance du workflow

- Revue hebdomadaire : incidents, lenteurs pipelines, qualité.
- Revue mensuelle : disponibilité, restauration, sécurité.
- Actions correctrices tracées (responsable + date + résultat).

