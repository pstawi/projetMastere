# Tableau à cocher - Preuves jury (Objectif n°1)

Projet : Workflow de production Furious Ducks - Objectif n°1
Version : 1.0
Mode d'utilisation : cocher la case, ajouter le lien/chemin de preuve, puis indiquer la date de validation.

## Légende

- Statut : `[ ]` à faire, `[x]` fait
- Priorité : Haute / Moyenne / Basse

## 1) Preuves de cadrage et contenu du cahier

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Cahier des spécifications techniques complet (structure officielle respectée) | Haute | | | `rendu/CST_Objectif1_Furious_Ducks_FINAL.md` | |
| [x] | État des lieux, problématique et objectif To-Be rédigés | Haute | | | Section A du cahier | |
| [x] | Méthodologie Scrum détaillée (rôles, rituels, DoD) | Haute | | | Section B du cahier | |
| [x] | Introduction DevOps/DevSecOps et topologie d'équipe | Haute | | | Section C du cahier | |
| [x] | Matrice RACI finalisée | Haute | | | Section C.5 du cahier | |
| [ ] | Page de garde complétée (date réelle, noms des rédacteurs) | Basse | | | Section 0 du cahier | |
| [ ] | Données juridiques fictives validées avec le formateur | Basse | | | Section A.1 du cahier | |

## 2) Preuves d'architecture et de choix techniques

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Analyse du workflow CI/CD (définitions, contraintes, tâches automatisées) | Haute | | | Section D du cahier | |
| [x] | Choix techniques justifiés (tableau brique/solution/alternative écartée) | Haute | | | Section D.2 du cahier | |
| [x] | Hébergement et politique de sauvegarde détaillés | Haute | | | Section D.3 du cahier | |
| [x] | Diagramme d'infrastructure complet (flowchart) | Haute | | | Section F.1 du cahier | |
| [x] | Zones réseau et exposition externe | Haute | | | Section F.2 du cahier | |
| [x] | Table des flux/ports/protocoles | Haute | | | Section F.3 du cahier | |
| [x] | Nommage DNS conforme à la convention imposée | Moyenne | | | Section F.4 du cahier (placeholders à remplacer) | |
| [x] | Fichiers techniques fournis (`docker-compose.yml`, `Jenkinsfile`, configs) | Haute | | | `rendu/workflow-technique/` | |

## 3) Preuves d'exigences mesurables

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Indicateurs CI/CD (build, qualité, déploiement, lead time) | Haute | | | Section E.1 du cahier | |
| [x] | Indicateurs tests (couverture, succès, smoke tests, régression) | Haute | | | Section E.2 du cahier | |
| [x] | SLO/SLA de disponibilité par service | Haute | | | Section E.3 du cahier | |
| [x] | RTO/RPO et politique de sauvegarde chiffrée | Haute | | | Section E.4 du cahier | |
| [x] | Exigences de sécurité et conformité opérationnelle | Haute | | | Section E.5 du cahier | |
| [x] | Critères Go/No-Go de mise en production | Haute | | | Section E.6 du cahier | |

## 4) Preuves de procédures (BPMN/UML)

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Procédure de déploiement dev → préprod → prod (BPMN) | Haute | | | Section H.1 du cahier | |
| [x] | Procédure de sauvegarde automatisée (BPMN) | Haute | | | Section H.2 du cahier | |
| [x] | Procédure de restauration (BPMN) | Haute | | | Section H.3 du cahier | |
| [x] | Procédure de gestion d'incident critique (BPMN) | Haute | | | Section H.4 du cahier | |
| [x] | Diagramme d'activité UML (cycle de vie user story) | Moyenne | | | Section H.6 du cahier | |
| [x] | Diagrammes de séquence UML (déploiement, restauration) | Moyenne | | | Section H.7 du cahier | |
| [x] | Check-lists opérationnelles associées | Moyenne | | | Section H.5 du cahier | |

## 5) Preuves RH, planning et coûts

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Fiche de poste complète (recrutement) | Haute | | | Section G.1 du cahier | |
| [x] | Plan de formation/onboarding détaillé | Haute | | | Section G.2 du cahier | |
| [x] | WBS et macro-planning | Haute | | | Section I.1-I.2 du cahier | |
| [x] | Planning détaillé (28 tâches, prédécesseurs, ressources) | Haute | | | Section I.3 du cahier + `rendu/workflow-technique/gantt_objectif1.csv` | |
| [ ] | Gantt final généré sous MS Project ou GanttProject (fichier projet + export visuel) | Haute | | | À produire à partir du CSV fourni | |
| [x] | Jalons identifiés (J1 à J5) | Haute | | | Section I.4 du cahier | |
| [x] | Estimation des coûts (infra, mise en place, run) et rentabilité | Haute | | | Section J du cahier | |
| [x] | Base de calcul des taux journaliers (TJM) | Haute | | | Annexe 1 du cahier | |
| [x] | Registre des risques complet | Haute | | | Section K du cahier | |

## 6) Preuves de mise en œuvre réelle (exigence transverse de mise en ligne)

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Hébergement souscrit (serveur dédié/VPS) | Haute | | | | |
| [ ] | Nom de domaine acheté (format `wk-<classe>-<groupe>.fr`) | Haute | | | | |
| [ ] | DNS configuré pour tous les sous-domaines | Haute | | | | |
| [ ] | `docker-compose.yml` déployé sur le serveur réel | Haute | | | | |
| [ ] | Certificats TLS Let's Encrypt valides sur chaque sous-domaine | Haute | | | | |
| [ ] | Workflow maintenu en ligne jusqu'à la date du jury | Haute | | | | |

> Ces preuves de mise en œuvre réelle sont exigées par le brief au titre de la mise en ligne, indépendamment de tout projet client (cf. `todo/01_Objectif1_Reste_A_Faire.md` section 1). Elles ne conditionnent pas la complétude documentaire du cahier lui-même (déjà couverte par les sections 1 à 5 ci-dessus).

## 7) Preuves de support de soutenance

| Statut | Preuve attendue | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Support PowerPoint de soutenance généré | Haute | | | `rendu/Soutenance_Objectif1_Furious_Ducks.pptx` | |
| [ ] | Support relu et adapté (timing, ton, exemples) | Moyenne | | | | |
| [ ] | Répétition orale effectuée (questions pièges incluses) | Moyenne | | | | |

## 8) Vérification finale avant jury

| Statut | Contrôle final | Priorité | Responsable | Échéance | Lien/chemin de preuve | Validé (date) |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Absence de toute trace "GitHub Cloud" dans le cahier final | Haute | | | Vérifié par relecture automatisée | |
| [ ] | Tous les placeholders (`<classe>-<groupe>`, rédacteurs, dates) remplacés | Moyenne | | | | |
| [ ] | Cohérence globale entre cahier, artefacts techniques et support de soutenance | Haute | | | | |
| [ ] | Recalage des coûts si le tarif d'hébergement réel diffère de l'hypothèse (90 €/mois) | Basse | | | | |
