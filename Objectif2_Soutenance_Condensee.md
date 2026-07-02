# Objectif n°2 - Version soutenance condensée

Version : 1.0  
Client : Thé Tip Top  
Format : support oral (synthèse opérationnelle)

## 1) Contexte et enjeu

Thé Tip Top lance un jeu-concours pour soutenir l'ouverture d'une nouvelle boutique et capter de nouveaux clients.  
Le projet doit transformer une opération marketing ponctuelle en levier digital mesurable (acquisition, participation, fidélisation), tout en respectant les contraintes juridiques et techniques.

## 2) Besoin reformulé

Livrer un dispositif digital de jeu-concours qui permet :

- l'inscription des participants,
- la saisie/validation de codes tickets pré-générés,
- l'attribution et le suivi des gains,
- la gestion des remises en boutique,
- la visualisation d'indicateurs métier en back-office.

Contraintes clés :

- 500 000 codes pré-générés avec répartition des gains imposée,
- parcours mobile-first,
- conformité RGPD/cookies,
- accessibilité et lisibilité.

## 3) Cibles et proposition de valeur

- **Participants** : expérience simple, rapide, rassurante.
- **Équipes boutique** : vérification/remise des gains sans friction.
- **Équipe marketing/admin** : pilotage par données, exports exploitables.

Proposition de valeur : un concours fluide côté utilisateur, contrôlable côté métier, traçable côté conformité.

## 4) Benchmark et enseignements

Concurrents de référence :

- Direct : Palais des Thés
- Direct : Kusmi Tea
- Indirect : Nespresso

Enseignements actionnables :

- réduire le nombre d'étapes jusqu'à la participation,
- privilégier une interface légère et lisible,
- renforcer la transparence des règles et du traitement des données.

## 5) Stratégie de communication digitale

Objectifs :

- notoriété de campagne,
- conversion visiteur -> participation,
- collecte qualifiée avec consentement,
- fidélisation post-concours.

Piliers :

- **SEO** : pages concours optimisées et explicites,
- **SMO** : publications régulières orientées participation,
- **Emailing** : onboarding, relance, fidélisation,
- **E-réputation** : protocole de réponse en 3 niveaux (simple/sensible/critique).

## 6) Architecture fonctionnelle cible

- **Webapp front-office** : inscription, participation, historique gains.
- **Back-office admin** : supervision campagne, statistiques, exports.
- **Espace boutique** : validation remise lot.
- **API centrale** : validation code, attribution gain, traçabilité.

Parcours critique :

1. Inscription / connexion
2. Saisie code
3. Validation API
4. Attribution gain
5. Historisation
6. Remise en boutique (si besoin)

## 7) Choix techniques (synthèse)

- Front : framework web moderne (SPA/SSR selon arbitrage final)
- API : backend transactionnel
- Base de données : modèle orienté traçabilité (codes, participations, gains, audits)
- Analytics : Google Analytics 4 (événements clés)
- Hébergement : cloud/VPS avec HTTPS et sauvegardes quotidiennes

## 8) Mesure de performance (preuves)

KPI prioritaires :

- sessions qualifiées vers page concours,
- taux conversion inscription,
- taux conversion saisie code,
- taux d'abandon parcours,
- performance des sources d'acquisition.

Preuves attendues jury :

- captures GA4 (DebugView/Realtime/rapports),
- traçabilité des événements implémentés,
- tableau objectif métier -> KPI -> décision.

## 9) Gouvernance projet et risques

Pilotage :

- Scrum en sprints courts,
- arbitrages hebdomadaires basés sur preuves,
- suivi des risques dans une matrice dédiée.

Risques majeurs :

- surcharge de trafic sur validation de codes,
- non-conformité cookies/RGPD,
- dérive de périmètre,
- retard UX/UI.

Réponses :

- tests ciblés + optimisation endpoint critique,
- gouvernance juridique intégrée,
- backlog priorisé (MoSCoW),
- jalons de validation intermédiaires.

## 10) Livrables et planning

Livrables principaux :

- cahier des charges client complet,
- livrables UX/UI (zoning, wireframes, maquettes, charte),
- spécifications fonctionnelles/techniques,
- plan de tests et conformité,
- matrices de pilotage + Gantt + devis.

Cadence proposée :

- S1-S2 : cadrage, benchmark, stratégie,
- S3-S4 : conception fonctionnelle et technique,
- S5+ : réalisation, tests, preuves, consolidation dossier.

## 11) Messages de défense orale

1. Le projet répond à un besoin business clair, pas uniquement technique.
2. Les choix sont justifiés par l'équilibre valeur/temps/risque.
3. La conformité et la traçabilité sont intégrées dès la conception.
4. Les preuves de performance guident les décisions, pas l'intuition.

## 12) Checklist finale avant jury

- récit projet clair (problème -> solution -> valeur),
- preuves analytics prêtes,
- parcours fonctionnels démontrables,
- conformité légale explicitée,
- planning/coûts cohérents et assumés.