# Objectif n°1 - Macro-planning, coûts et argumentaire de soutenance

## 1) Macro-planning (WBS -> PERT -> Gantt)

## 1.1 Lots de travail (WBS simplifié)

1. Cadrage et spécifications
2. Mise en place infra dédiée
3. Déploiement des briques workflow
4. Industrialisation CI/CD
5. Monitoring + sauvegardes + sécurité
6. Procédures, RH et formation
7. Validation, documentation et soutenance

## 1.2 Planning proposé (5 semaines)


| Semaine | Lot principal                      | Livrable clé                                        |
| ------- | ---------------------------------- | --------------------------------------------------- |
| S1      | Cadrage + cahier technique         | Structure validée + exigences                       |
| S2      | Infra + services cœur              | Jenkins, SCM, registry, reverse proxy opérationnels |
| S3      | Pipelines CI/CD                    | Déploiement dev/preprod/prod avec approval prod     |
| S4      | Monitoring, backup, sécurité, BPMN | Dashboards + test restauration + procédures         |
| S5      | Chiffrage final + présentation     | Dossier consolidé + support soutenance              |


## 1.3 Jalons (à placer dans Gantt)

- J1 : Architecture validée
- J2 : Pipeline bout en bout démontré
- J3 : Backup/restauration testés
- J4 : Procédures et RH finalisées
- J5 : Dossier final prêt soutenance

## 2) Estimation des coûts (ordre de grandeur)

## 2.1 Hypothèses

- Équipe projet : chef de projet, ingénieur DevOps, développeur
- Durée de mise en place initiale : 5 semaines
- Exploitation mensuelle incluse (maintenance de base)
- Chiffrage pédagogique cohérent "mode agence"

## 2.2 Coûts infra (mensuels)


| Poste                     | Hypothèse                       | Coût mensuel estimé |
| ------------------------- | ------------------------------- | ------------------- |
| Serveur dédié Linux       | 1 instance principale           | 90 EUR              |
| Stockage backup distant   | 200-500 Go                      | 20 EUR              |
| Nom de domaine + DNS      | lissé mensuel                   | 3 EUR               |
| Supervision/notifications | outils open source (coût infra) | 0 EUR               |
| Total mensuel infra       |                                 | **113 EUR**         |


## 2.3 Coûts de mise en place (one-shot)


| Poste                              | Charge estimée | Taux jour moyen | Coût estimé   |
| ---------------------------------- | -------------- | --------------- | ------------- |
| Cadrage + spécifications           | 4 j            | 450 EUR         | 1800 EUR      |
| Installation infra et tooling      | 6 j            | 500 EUR         | 3000 EUR      |
| Pipelines et déploiement           | 6 j            | 500 EUR         | 3000 EUR      |
| Monitoring + backups + sécurité    | 4 j            | 500 EUR         | 2000 EUR      |
| Documentation + procédures + RH    | 3 j            | 450 EUR         | 1350 EUR      |
| Recette + soutenance + ajustements | 3 j            | 450 EUR         | 1350 EUR      |
| Total one-shot                     | 26 j           |                 | **12500 EUR** |


## 2.4 Coûts run mensuels (maintenance)


| Poste                            | Charge mensuelle | Coût mensuel estimé |
| -------------------------------- | ---------------- | ------------------- |
| Maintenance corrective/évolutive | 2 j/mois         | 1000 EUR            |
| Supervision et sauvegarde        | 1 j/mois         | 500 EUR             |
| Support utilisateurs internes    | 0.5 j/mois       | 225 EUR             |
| Total run humain                 |                  | **1725 EUR**        |


Coût mensuel global (infra + run) : **1838 EUR**

## 3) Estimation de rentabilité (comparatif)

## 3.1 Situation sans workflow industrialisé (estimation)

- Déploiements manuels plus longs
- Taux d'erreur de mise en production plus élevé
- Reprises incident plus coûteuses

## 3.2 Gains attendus avec workflow (12 mois)

- Réduction du lead time livraison : 30-50 %
- Réduction incidents déploiement : 30 %
- Temps de reprise sur incident standardisé (RTO ciblé <= 4 h)
- Gain productivité équipe projet (moins de tâches manuelles répétitives)

## 3.3 Lecture financière simplifiée

- Investissement initial : 12500 EUR
- Coûts récurrents mensuels : 1838 EUR
- Gains potentiels (temps + qualité) à estimer via KPI réels après 2-3 mois

## 4) Trame d'argumentaire de soutenance

## 4.1 Pourquoi cette architecture

- Conformité stricte aux contraintes sujet (Jenkins, Docker, open source).
- Approche équilibrée : solide sans complexité excessive.
- Standardisation reproductible pour plusieurs projets clients.

## 4.2 Pourquoi ces exigences mesurables

- Le jury peut vérifier objectivement les performances du workflow.
- Les KPI couvrent delivery, qualité, disponibilité, résilience.
- Les seuils "go/no-go" sécurisent les mises en production.

## 4.3 Pourquoi ce modèle d'exploitation

- Clarifie les rôles (build/run), réduit les zones d'ombre.
- Documente les procédures critiques (incident, backup, restauration).
- Facilite l'onboarding via fiche de poste et plan de formation.

## 4.4 Risques et réponses

- Risque surcharge technique -> priorisation par jalons.
- Risque de panne serveur dédié -> backups externalisés + restauration testée.
- Risque dérive coûts -> revue mensuelle KPI + capacité.

## 5) Check-list finale avant jury

- Cahier structuré et justifié section par section.
- Démo pipeline complète (commit -> prod avec approval).
- Preuves de backup + restauration.
- Diagrammes infra + procédures lisibles.
- Chiffrage transparent et cohérent avec hypothèses.

