# Objectif n°1 - Structure détaillée du cahier des spécifications techniques (Workflow Furious Ducks)

Version : 1.0  
Périmètre : Transformation digitale de l'agence (workflow de production)

## 0) Couverture et métadonnées

- Intitulé : Cahier des spécifications techniques - Workflow de production
- Version, date, rédacteurs, historique de versions
- Mentions légales agence

**Preuves attendues en soutenance**

- Versioning du document
- Trace des contributeurs et date de dernière mise à jour

## A) État des lieux

### A.1 Présentation synthétique de l'agence

- Storytelling agence, positionnement, contraintes de croissance
- Informations juridiques utiles

**Preuves**

- Fiche entreprise consolidée
- Justification de la capacité opérationnelle (effectif, activités)

### A.2 Problématique actuelle

- Limites de l'organisation actuelle (cycle en V, goulots, dette process)
- Impacts : qualité, délais, risques de prod, reprise incident

**Preuves**

- Liste des irritants classés par criticité
- Exemple concret d'incident évitable

### A.3 Méthodologie actuelle

- Description opérationnelle du cycle actuel
- Points de rupture observés (validation tardive, intégration manuelle)

**Preuves**

- Schéma "As-Is" du flux de travail
- Mesure initiale (fréquence de déploiement, délai de livraison)

## B) Méthodologie cible de gestion de projet

- Méthode retenue : Agile (Kanban ou Scrum, à figer)
- Rituels, rôles, artefacts, cadence
- Articulation entre gestion de projet et pipeline CI/CD

**Preuves**

- Cadence de pilotage (planning des rituels)
- Définition of Done alignée CI/CD

## C) DevOps / DevSecOps

- Définition appliquée au contexte Furious Ducks
- Topologie d'équipe cible (responsabilités run/build)
- Montée en maturité DevOps (court, moyen, long terme)

**Preuves**

- Matrice RACI simplifiée
- Plan de montée en maturité avec jalons

## D) Analyse du workflow CI/CD

### D.1 Contraintes de conception

- Linux + Docker
- Jenkins comme CI principale
- Outils open source

### D.2 Tâches automatisées cibles

- Build, tests, quality gate, packaging, publication images
- Déploiement dev/preprod automatique
- Déploiement prod avec validation manuelle

### D.3 Standards et conventions

- Stratégie de branches
- Convention de versioning
- Gestion secrets et rollback

**Preuves**

- Jenkinsfile type commenté
- Politique de branching/versioning validée
- Check-list de rollback

## E) Choix techniques du workflow

### E.1 Briques logicielles

- Reverse proxy
- SCM Git auto-hébergé
- Jenkins
- Docker registry
- Monitoring et alerting
- Sauvegardes automatisées

### E.2 Justification des choix

- Critères : coût, maintenabilité, courbe d'apprentissage, sécurité
- Alternatives écartées et raisons

**Preuves**

- Tableau de décision multicritère
- Diagramme d'interconnexion des briques

## F) Hébergement, capacité et backups

- Cible : serveur dédié
- Hypothèses CPU/RAM/stockage/réseau
- SLA/GTR cibles
- Politique de sauvegarde (fréquence, rétention, restauration)

**Preuves**

- Fiche de sizing infra
- Politique RTO/RPO formalisée
- Procès-verbal d'un test de restauration

## G) Diagramme d'infrastructure complet

- Vue logique et technique du workflow
- Ports et protocoles entre services
- Zones réseau et exposition externe

**Preuves**

- Diagramme lisible annoté
- Table des flux (source, destination, port, protocole, justification)

## H) Gestion RH

### H.1 Fiche de poste

- Poste : responsable workflow/DevOps
- Missions, compétences, prérequis, contrat, fourchette salariale

### H.2 Plan de formation

- Onboarding 2-4 semaines
- Compétences à valider et évaluation

**Preuves**

- Fiche de poste complète
- Parcours de formation avec objectifs hebdomadaires

## I) Procédures (BPMN)

- Processus de déploiement dev/preprod/prod
- Procédure de sauvegarde
- Procédure de restauration
- Procédure de gestion incident critique

**Preuves**

- Diagrammes BPMN validés
- Check-lists opérationnelles associées

## J) Planning, coûts et rentabilité

### J.1 Planification

- WBS, PERT, Gantt (jalons, prédécesseurs, avancement)

### J.2 Estimation des coûts

- Coûts infra
- Coûts humains setup + run
- Coûts formation

### J.3 Rentabilité

- Comparatif "avec workflow" vs "sans workflow"
- Gains attendus (temps, qualité, incidents)

**Preuves**

- Extrait Gantt + ressources
- Tableau de coûts détaillé
- Note de calcul de rentabilité

## K) Annexes minimales

- Base de calcul des taux journaliers / horaires
- Glossaire technique
- Sources et hypothèses de chiffrage

**Preuves**

- Feuilles de calcul annexées
- Références externes datées