# Synthèse - Ce qu'il reste à faire sur l'ensemble du projet

Dernière mise à jour : à compléter à chaque revue.

Ce dossier `todo/` liste tout ce qui reste à produire ou à corriger pour arriver à un dossier complet et soutenable devant le jury. Il complète (sans les remplacer) `rendu/` (livrables finalisés de l'Objectif 1) et les fichiers `Objectif2_*` (brouillons de l'Objectif 2).

## Fichiers de ce dossier

| Fichier | Contenu |
| --- | --- |
| [`01_Objectif1_Reste_A_Faire.md`](01_Objectif1_Reste_A_Faire.md) | Ce qui manque pour l'Objectif n°1 (workflow Furious Ducks) |
| [`02_Objectif2_Reste_A_Faire.md`](02_Objectif2_Reste_A_Faire.md) | État d'avancement de l'Objectif n°2 (client Thé Tip Top) |
| [`03_Transverse_Suivi_Projet.md`](03_Transverse_Suivi_Projet.md) | Exigences communes aux deux objectifs |
| [`04_Mapping_Referentiel_RNCP_Bloc5.md`](04_Mapping_Referentiel_RNCP_Bloc5.md) | Croisement avec le référentiel officiel RNCP (Bloc 5 / Épreuve 7) |
| [`05_Mapping_Referentiel_RNCP_Blocs123.md`](05_Mapping_Referentiel_RNCP_Blocs123.md) | Croisement avec le référentiel officiel RNCP (Blocs 1, 2, 3 communs / Épreuves 1 à 5) |

## Référentiel officiel RNCP

Le projet Furious Ducks + Thé Tip Top sert de preuve pour :
- le **Bloc 5 (optionnel n°2) : « Piloter le développement technique d'une solution digitale »** (Épreuve n°7, C29-C35) ;
- les **3 blocs communs obligatoires** : Bloc 1 (stratégie marketing digitale, Épreuves 1-2), Bloc 2 (image de marque/UX, Épreuves 3-4), Bloc 3 (management de projet, Épreuve 5) - tous validés **au travers de l'Objectif n°2**.

Voir `04_Mapping_Referentiel_RNCP_Bloc5.md` et `05_Mapping_Referentiel_RNCP_Blocs123.md` pour le détail croisé, et `Referentiel_RNCP_ExpertStrategieTransformationDigitale_extrait.txt` pour le texte source complet.

## Indépendance des deux objectifs

L'Objectif n°1 (cahier des spécifications techniques du workflow + artefacts techniques) est **autonome et complet au regard de la structure officielle** : il ne dépend pas de l'Objectif n°2, ni du projet Thé Tip Top. Il n'est pas exigé de fournir des preuves d'exécution réelle (pipeline vert, déploiements, etc.) pour l'Objectif 1 - seule la mise en ligne de l'infrastructure du workflow reste requise (exigence transverse du brief, cf. `03_Transverse_Suivi_Projet.md`), indépendamment de tout projet client.

## Objectif 1 : statut

**Terminé sur le plan documentaire.** Tous les compléments possibles sans infrastructure réelle sont produits (cahier consolidé, artefacts techniques, RACI, UML, Gantt détaillé, PowerPoint de soutenance, checklist jury). Décisions actées : page de garde et données juridiques laissées telles quelles, mise en ligne réelle reportée (hors périmètre pour l'instant). Voir `01_Objectif1_Reste_A_Faire.md` pour le détail.

## Vue d'ensemble priorisée (toutes tâches confondues)

| Statut | Priorité | Tâche | Objectif | Détail |
| --- | --- | --- | --- | --- |
| [ ] | Reportée | Mise en ligne réelle du workflow (serveur + domaine + DNS) | Objectif 1 (hors périmètre pour l'instant, décision utilisateur) | Voir tableau 1 de `01_Objectif1_Reste_A_Faire.md` |
| [ ] | Haute | Mise en ligne réelle du site jeu-concours | Objectif 2 | Voir tableau 9 de `02_Objectif2_Reste_A_Faire.md` |
| [ ] | Haute | Outil de suivi de projet public (Trello/Notion) avec tâches + comptes rendus | Transverse | Voir tableau 1 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Haute | Gantt global sous MS Project/GanttProject (tâches, prédécesseurs, ressources, jalons) | Transverse | Voir tableau 2 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Haute | Contenu réel du benchmark, personas, mapping concurrentiel, UX/UI | Objectif 2 | Voir tableaux 1 et 4 de `02_Objectif2_Reste_A_Faire.md` |
| [ ] | Haute | Développement effectif du site du jeu-concours (API + webapp) | Objectif 2 | Voir tableau 7 de `02_Objectif2_Reste_A_Faire.md` |
| [x] | Moyenne | Matrice RACI visuelle (workflow) | Objectif 1 | Fait - section C.5 du cahier |
| [x] | Moyenne | Diagrammes UML (activité/séquence) en plus des BPMN | Objectif 1 | Fait - sections H.6/H.7 du cahier |
| [x] | Haute | Gantt détaillé (28 tâches, prédécesseurs, ressources) + PowerPoint de soutenance | Objectif 1 | Fait - `gantt_objectif1.csv`, `Soutenance_Objectif1_Furious_Ducks.pptx` (import MS Project/GanttProject = geste manuel restant) |
| [x] | Basse | Checklist preuves jury dédiée à l'Objectif 1 | Objectif 1 | Fait - `rendu/Tableau_Checklist_Preuve_Jury_Objectif1.md` |
| [ ] | Basse | Remplacement des placeholders (`<classe>-<groupe>`, rédacteurs, dates) | Objectif 1 (volontairement différé jusqu'à l'export final) | Voir tableau 1/3 de `01_Objectif1_Reste_A_Faire.md` |
| [ ] | Moyenne | Présentation PowerPoint de soutenance - Objectif 2 | Transverse | Voir tableau 4 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Moyenne | Harmonisation des devis (Objectif 1 vs Objectif 2, taux différents) | Transverse | Voir tableau 2 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Moyenne | Rédaction définitive légale (mentions légales, CGU, règlement concours) | Objectif 2 | Voir tableau 5 de `02_Objectif2_Reste_A_Faire.md` |
| [ ] | Basse | Scripts CI (`ci/*.sh`) et preuves d'exécution du workflow | Objectif 1 (facultatif, hors périmètre strict) | Voir tableau 2 de `01_Objectif1_Reste_A_Faire.md` |
| [ ] | Basse | Répétition orale + questions pièges | Transverse | Voir tableau 5 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Basse | Vérification finale de cohérence globale (cahiers/preuves/démo) | Transverse | Voir tableau 5 de `03_Transverse_Suivi_Projet.md` |
| [ ] | Moyenne | 5 compléments révélés par le référentiel officiel RNCP (RSE, RGAA, schéma de navigation, méthode de modélisation, cycle de vie) | Objectif 2 | Voir `04_Mapping_Referentiel_RNCP_Bloc5.md` |
| [ ] | Haute | Créer le document "Stratégie d'accompagnement du changement" (formation équipes, inclusion handicap, conduite du changement) | Objectif 2 | Production centrale de l'Épreuve 5 (Bloc 3), actuellement inexistante - voir `05_Mapping_Referentiel_RNCP_Blocs123.md` |
| [ ] | Haute | Ajouter une section "Technologies d'innovation et de disruption" (IA, AR-VR, etc.) avec justification RSE | Objectif 2 | Exigé explicitement par C23 (Bloc 3), actuellement inexistant - voir `05_Mapping_Referentiel_RNCP_Blocs123.md` |
| [ ] | Moyenne | 8 compléments supplémentaires révélés par le référentiel (veille handicap/RGAA/propriété intellectuelle, IA comportementale, prestataires, seuils de performance, handicap/langue en management) | Objectif 2 | Voir tableau de synthèse de `05_Mapping_Referentiel_RNCP_Blocs123.md` |
