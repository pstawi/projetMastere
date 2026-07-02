# Objectif n°1 (Workflow Furious Ducks) - Ce qu'il reste à faire

Statut global : **Objectif 1 considéré comme terminé sur le plan documentaire.** Le cahier des spécifications techniques et les artefacts techniques sont rédigés et enrichis (`rendu/CST_Objectif1_Furious_Ducks_FINAL.md` + `rendu/workflow-technique/`), avec tous les compléments possibles sans infrastructure réelle (RACI, UML, Gantt détaillé, PowerPoint, checklist jury). Ce livrable est **autonome et complet au regard de la structure officielle** : il ne dépend pas de l'Objectif n°2 ni du projet Thé Tip Top.

**Décisions actées avec l'utilisateur** :
- Page de garde : placeholders (`<Prénom NOM>`, date) conservés, à compléter en tout dernier avant export final.
- Données juridiques fictives de l'agence : conservées telles quelles.
- Mise en ligne réelle du workflow : **reportée / hors périmètre pour l'instant** (section 1 ci-dessous conservée pour mémoire, à réactiver si nécessaire avant le jury).

Ce qui reste ci-dessous n'est donc plus bloquant pour la complétude de l'Objectif 1.

Légende Statut : `[ ]` à faire, `[x]` fait.

## 1) Mise en ligne réelle du workflow (reportée - décision utilisateur)

> **Décision actée** : la mise en ligne réelle (achat serveur/domaine, déploiement effectif) n'est **pas engagée pour l'instant**. Le périmètre actuel reste le cahier des spécifications techniques + les artefacts techniques (`docker-compose.yml`, `Jenkinsfile`, configs), jugés suffisants pour démontrer la faisabilité des choix (cf. `0.2 Périmètre de preuve` du cahier). Cette section reste documentée pour mémoire, à réactiver si la mise en ligne redevient nécessaire avant le jury (exigence transverse du brief).

| Statut | Tâche | Détail | Priorité | Responsable | Échéance |
| --- | --- | --- | --- | --- | --- |
| [ ] | Souscrire un hébergement | Serveur dédié/VPS Linux, dimensionnement 8 vCPU / 32 Go RAM / 500 Go SSD (section D.3 du cahier) | Reportée | | |
| [ ] | Acheter le nom de domaine | Format imposé `wk-<classe>-<groupe>.fr` | Reportée | | |
| [ ] | Configurer le DNS | Sous-domaines jenkins/git/registry/grafana/prometheus/status | Reportée | | |
| [ ] | Remplacer les placeholders | `rendu/CST_Objectif1_Furious_Ducks_FINAL.md` (F.4) et `rendu/workflow-technique/.env.example` | Reportée | | |
| [ ] | Déployer `docker-compose.yml` | Sur le serveur réel + générer `registry/auth/htpasswd` et le hash pour `traefik/dynamic.yml` | Reportée | | |
| [ ] | Vérifier les certificats TLS | Let's Encrypt effectif sur chaque sous-domaine | Reportée | | |
| [ ] | Maintenir le workflow en ligne | Jusqu'à la date du jury (contrainte obligatoire si la mise en ligne est réactivée) | Reportée | | |

## 2) Compléments techniques optionnels (hors périmètre strict de l'Objectif 1)

> La structure officielle n'exige pas de preuve d'exécution réelle pour l'Objectif 1 : le cahier et les artefacts techniques (`docker-compose.yml`, `Jenkinsfile`, configs) suffisent à démontrer la faisabilité des choix. Les éléments ci-dessous ne sont donc **pas requis** ; ils ne sont utiles que si vous décidez, de votre propre initiative, de faire tourner concrètement le workflow.

| Statut | Tâche (facultative) | Détail | Priorité |
| --- | --- | --- | --- |
| [ ] | Écrire des scripts `ci/*.sh` d'exemple | lint/tests/quality-gate/deploy/smoke-test/rollback référencés par le `Jenkinsfile` - par nature spécifiques à chaque projet client, à écrire au cas par cas | Facultative |
| [ ] | Ajouter des exporters de métriques | `node-exporter`/`cadvisor` sur les environnements applicatifs, uniquement si des environnements réels sont déployés | Facultative |

## 3) Compléments documentaires

| Statut | Tâche | Détail | Priorité | Responsable | Échéance |
| --- | --- | --- | --- | --- | --- |
| [x] | Matrice RACI visuelle | Ajoutée en section C.5 du cahier (16 activités x 7 rôles) | Moyenne | | Fait |
| [x] | Diagrammes UML (activité/séquence) | Ajoutés en sections H.6 (activité, couloirs par rôle) et H.7 (2 séquences) du cahier | Moyenne | | Fait |
| [x] | Gantt détaillé (tâches, prédécesseurs, ressources, jalons) | 28 tâches + 5 jalons avec prédécesseurs/ressources/coûts dans `rendu/workflow-technique/gantt_objectif1.csv` (générique) et `gantt_objectif1_ganttproject.csv` (structuré pour import GanttProject) + visuel Mermaid en section I.3 du cahier | Haute | | Fait (import réel dans l'outil = geste manuel restant, cf. guide ci-dessous) |
| [ ] | Import effectif dans GanttProject (ou MS Project) | Suivre le guide pas-à-pas ci-dessous pour générer le fichier projet natif (.gan/.mpp) + export visuel annexé, conformément à l'exigence stricte du sujet | Moyenne | | |

### Guide pas-à-pas : import du planning dans GanttProject

GanttProject a un import CSV **sensible à la langue de l'interface et au format de date** (retours d'expérience de la communauté GanttProject). Suivre cet ordre exact évite la quasi-totalité des échecs constatés :

1. **Ouvrir GanttProject** et créer un nouveau projet vide (ou l'utiliser directement sur un projet existant : l'import ajoute les tâches sans écraser l'existant).
2. **Passer l'interface en anglais** : `Settings` (ou `Édition > Préférences`) > `Application` > `Language` > `English`. Le fichier fourni (`gantt_objectif1_ganttproject.csv`) utilise des en-têtes anglais (`ID, Name, Begin date, End date, Duration, Completion, Cost, Predecessors, Resources, Notes`) car l'import de GanttProject exige que les en-têtes du CSV correspondent exactement à la langue de l'interface.
3. **Régler le format de date** sur `yyyy-MM-dd` dans les mêmes préférences (le fichier fourni utilise ce format ISO sans ambiguïté).
4. **Importer** : menu `File` > `Import` > `CSV...`, puis sélectionner `rendu/workflow-technique/gantt_objectif1_ganttproject.csv`.
5. **Vérifier après import** :
   - les 28 tâches + 5 jalons (durée 0) sont présentes avec les bonnes dates ;
   - les 3 ressources apparaissent dans l'onglet Ressources (`CDP`, `DEVOPS`, `DEV`) ;
   - les liens de dépendance sont bien créés, en particulier les tâches à prédécesseurs multiples (tâche 12 : prédécesseurs 9, 10 et 11 séparés par `;` dans le fichier) ;
   - le « Default role » des ressources n'est pas vide (sinon le recréer manuellement, bug connu de l'import).
6. **Si l'import ne fait rien** (aucune erreur mais aucune tâche créée) : vérifier que le fichier est bien encodé en UTF-8 (c'est le cas du fichier fourni) et que l'interface est toujours en anglais au moment de l'import.
7. Une fois l'import validé, **repasser l'interface en français** si besoin, compléter les taux horaires/ressources si nécessaire, puis exporter le Gantt visuel (`File > Export > Image/PDF`) et sauvegarder le fichier projet natif (`.gan`) pour l'annexer au cahier.
8. En cas d'échec persistant de l'import malgré ces étapes, solution de repli : recréer les 28 tâches manuellement dans GanttProject en s'appuyant sur `gantt_objectif1.csv` comme table de référence (saisie directe, plus lente mais fiable à 100 %).
| [x] | Présentation PowerPoint dédiée | Générée : `rendu/Soutenance_Objectif1_Furious_Ducks.pptx` (18 slides, script source `rendu/generate_soutenance_pptx.py`) | Moyenne | | Fait (relecture/adaptation du ton encore utile) |
| [ ] | Compléter la page de garde | Date réelle + nom(s) des rédacteurs (actuellement `<Prénom NOM>`) - **décision : laisser en placeholder pour l'instant**, à compléter en tout dernier avant export final | Basse | | |
| [x] | Valider les données juridiques fictives | SIREN/SIRET/capital de l'agence - **décision : conservées telles quelles** | Basse | | Fait |

## 4) Vérifications de cohérence

| Statut | Tâche | Détail | Priorité | Responsable | Échéance |
| --- | --- | --- | --- | --- | --- |
| [x] | Relecture complète post-placeholders | Vérifié : aucune trace résiduelle de "GitHub Cloud" (hors mention volontaire en alternative écartée), fichiers référencés dans `workflow-technique/` tous présents | Moyenne | | Fait |
| [ ] | Recalage des coûts | Section J du cahier si le tarif d'hébergement réel diffère des 90 €/mois estimés | Basse | | |
| [x] | Checklist preuves jury dédiée | Créée : `rendu/Tableau_Checklist_Preuve_Jury_Objectif1.md` | Basse | | Fait |
