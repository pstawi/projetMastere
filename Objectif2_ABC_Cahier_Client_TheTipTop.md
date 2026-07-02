# Objectif n°2 - Cahier client (Sections A à J)

Version : 1.0  
Client : Thé Tip Top  
Périmètre : site jeu-concours (API + webapp), hors refonte du site corporate complet  
Niveau : équilibré (qualité soutenable dans le temps imparti)

## A. Descriptifs

### A.1 Présentation du client

Thé Tip Top est une entreprise française positionnée sur le thé premium et les infusions, avec une promesse orientée qualité, expérience et image de marque. Son enjeu actuel est double : soutenir son développement commercial et moderniser sa présence digitale avec une mécanique d'acquisition plus engageante.

Le projet jeu-concours s'inscrit dans un moment fort d'activité (ouverture d'une nouvelle boutique), et doit transformer une opération promotionnelle ponctuelle en opportunité de collecte de données, de fidélisation et de visibilité.

Informations de base connues :

- Gérant : M. Eric Bourdon
- Siège social : 18 rue Léon Frot, 75011 Paris
- Forme : SA
- Capital social : 150 000 EUR

### A.2 Présentation du projet

#### Besoin reformulé

Le client souhaite un dispositif digital dédié au jeu-concours capable de :

- présenter l'opération et les lots,
- permettre l'inscription des participants,
- valider des codes de tickets générés en amont,
- tracer les gains et leur remise,
- fournir des statistiques d'usage aux équipes métier.

#### Contraintes structurantes

- 500 000 codes pré-générés avec gains associés (respect des pourcentages imposés).
- période du concours + période post-clôture de réclamation.
- logique multi-acteurs : participants, administrateurs, employés magasin.
- exigences de conformité : RGPD, accessibilité, bonnes pratiques SEO.

#### Livrables attendus sur ce bloc A-C

- section descriptive complète du cahier client,
- plan de veille exploitable par l'équipe,
- benchmark argumenté avec implications produit.

### A.3 Présentation de l'agence (projetée)

L'agence Furious Ducks se positionne comme intégrateur web orienté open source et industrialisation des livraisons. Sur ce projet, l'agence intervient comme maître d'oeuvre digital, avec un pilotage structuré, des choix justifiés et une exigence de traçabilité des preuves.

Positionnement de réalisation :

- méthode Scrum,
- conception progressive par incréments,
- validation régulière des hypothèses avec livrables démontrables.

### A.4 Comité de pilotage (version de travail)

#### Maîtrise d'ouvrage (client)

- Sponsor : direction Thé Tip Top
- Référent marketing : communication et activation
- Référent opérations : coordination boutiques / remise des lots

#### Maîtrise d'oeuvre (agence)

- Chef de projet : cadrage, arbitrages, planning
- Lead technique : API, sécurité, intégration
- Développeur full-stack : implémentation webapp/back-office
- QA / accessibilité : vérification conformité fonctionnelle et UX

Coordonnées minimales à compléter avant rendu final (obligatoire) :


| Entité | Nom/Prénom  | Rôle                | Email       | Téléphone   | Jours/horaires | Backup en cas d'absence |
| ------ | ----------- | ------------------- | ----------- | ----------- | -------------- | ----------------------- |
| Client | À compléter | Sponsor             | À compléter | À compléter | À compléter    | À compléter             |
| Client | À compléter | Référent marketing  | À compléter | À compléter | À compléter    | À compléter             |
| Client | À compléter | Référent opérations | À compléter | À compléter | À compléter    | À compléter             |
| Agence | À compléter | Chef de projet      | À compléter | À compléter | À compléter    | À compléter             |
| Agence | À compléter | Lead technique      | À compléter | À compléter | À compléter    | À compléter             |
| Agence | À compléter | Développeur         | À compléter | À compléter | À compléter    | À compléter             |


### A.5 Descriptif rédactionnel fonctionnel

Le site jeu-concours est conçu comme un service transactionnel simple côté utilisateur et rigoureux côté administration.

Côté front-office, le visiteur peut comprendre l'opération, créer un compte, soumettre ses codes et consulter l'historique de ses participations et gains. L'expérience doit être fluide sur mobile, car une part significative des participants saisira son code depuis un smartphone.

Côté back-office, les administrateurs disposent d'indicateurs d'activité (tickets distribués/activés, lots attribués/remis, répartition des profils), d'outils de contrôle et d'exports utiles à la communication et à l'emailing.

Un espace dédié aux boutiques permet de vérifier rapidement un gain et de tracer la remise effective du lot, ce qui réduit les litiges et sécurise l'opération.

L'architecture fonctionnelle repose sur une API centrale qui orchestre :

- la validation des codes,
- l'attribution des gains,
- la traçabilité des événements métier,
- la restitution des données pour les interfaces web et reporting.

## B. Plan de veille

### B.1 Objectifs de veille

Le plan de veille doit alimenter des décisions concrètes et non accumuler de l'information passive. Les objectifs retenus sont :

- anticiper les contraintes juridiques du jeu-concours et des traceurs,
- suivre les pratiques concurrentes sur les mécaniques promotionnelles,
- maintenir une qualité technique cohérente (performance, accessibilité, SEO),
- orienter les choix marketing digital à court terme.

### B.2 Types de veille

1. Veille juridique :

- RGPD (collecte, consentement, durée de conservation),
- cookies/traceurs (CNIL),
- obligations de transparence liées au jeu-concours.

1. Veille concurrentielle :

- expérience participant sur des opérations comparables,
- modalités d'inscription et de validation des participations,
- qualité perçue des interfaces.

1. Veille technique :

- bonnes pratiques API/webapp,
- instrumentation analytics orientée événements,
- accessibilité et performance web.

1. Veille marketing digitale :

- tendances d'acquisition e-commerce,
- KPI d'engagement et de conversion.

### B.3 Routine de veille

- Fréquence : hebdomadaire (synthèse consolidée en fin de sprint).
- Format : fiche de veille unique par sujet.
- Diffusion : équipe projet + référent client.

Template recommandé pour chaque fiche :

- Sujet de veille
- Date
- Source (URL complète)
- Information clé
- Impact projet
- Décision / action
- Responsable
- Échéance

### B.4 Sources de référence initiales

- CNIL - Règles cookies et traceurs : [https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles)
- CNIL - Refus des cookies aussi simple que l'acceptation : [https://cnil.fr/fr/refuser-les-cookies-doit-etre-aussi-simple-quaccepter-mise-en-conformite-de-tous-les-organismes](https://cnil.fr/fr/refuser-les-cookies-doit-etre-aussi-simple-quaccepter-mise-en-conformite-de-tous-les-organismes)
- Fevad - Bilan e-commerce 2024 : [https://www.fevad.com/bilan-du-e-commerce-en-france-en-2024/](https://www.fevad.com/bilan-du-e-commerce-en-france-en-2024/)
- Google Analytics 4 - Events : [https://developers.google.com/analytics/devguides/collection/ga4/events](https://developers.google.com/analytics/devguides/collection/ga4/events)

## C. Benchmark

### C.1 Étude de marché et chiffres clés (synthèse utile au projet)

Le contexte e-commerce français reste porteur pour des dispositifs digitaux promotionnels. La Fevad indique pour 2024 un marché à 175,3 milliards d'euros, en hausse de 9,6 %, avec une dynamique portée par la reprise des transactions. Cette tendance valide le choix d'une activation participant orientée web/mobile.

Sur la catégorie thé/infusions, plusieurs publications sectorielles confirment une consommation soutenue et une progression de certains segments (bio, infusions fonctionnelles). Ces signaux renforcent la pertinence d'un jeu-concours à forte dimension découverte et fidélisation.

Sources (à conserver en annexe avec date de consultation) :

- Fevad 2024 : [https://www.fevad.com/bilan-du-e-commerce-en-france-en-2024/](https://www.fevad.com/bilan-du-e-commerce-en-france-en-2024/)
- Synthèse marché thé/infusions (source sectorielle secondaire) : [https://madeinfr.fr/etudes-de-marche/agroalimentaire-alimentation/le-marche-des-thes-et-infusions-en-france/](https://madeinfr.fr/etudes-de-marche/agroalimentaire-alimentation/le-marche-des-thes-et-infusions-en-france/)

### C.2 Positionnement / concurrence

#### C.2.1 Concurrents retenus

- Concurrent direct 1 : Palais des Thés (`palaisdesthes.com`)
- Concurrent direct 2 : Kusmi Tea (`kusmitea.com`)
- Concurrent indirect : Nespresso (`nespresso.com/fr`)  
(indirect car acteur boisson premium avec forte maturité CRM/e-commerce, utile en référence d'expérience digitale)

#### C.2.2 Grille d'audit (5 axes)

Pour chaque concurrent :

- audit technique (stack visible, performance, responsive),
- audit Green IT (poids pages, requêtes, optimisation assets),
- audit SEO (balises, structure, indexation, maillage),
- audit design/ergonomie (parcours, lisibilité, conversion),
- audit accessibilité (contrastes, navigation clavier, structure sémantique).

### C.3 Synthèses concurrentielles (version intermédiaire)

#### Palais des Thés (direct)

- Points forts : univers de marque cohérent, profondeur catalogue, pédagogie produit.
- Points faibles : pages parfois denses, charge cognitive potentielle sur mobile.
- Implication projet : privilégier une page concours plus épurée, centrée sur l'action principale (participer).

#### Kusmi Tea (direct)

- Points forts : branding fort, modernité visuelle, hiérarchie marketing claire.
- Points faibles : interfaces parfois riches en scripts, vigilance performance.
- Implication projet : conserver une identité forte sans alourdir l'expérience participant.

#### Nespresso (indirect)

- Points forts : parcours client industrialisé, CRM, tunnel optimisé.
- Points faibles : complexité potentielle sur certains parcours riches.
- Implication projet : reprendre la logique de fluidité transactionnelle et de traçabilité, pas la complexité.

### C.4 Conclusions benchmark actionnables

- Priorité UX : réduire le nombre d'étapes entre arrivée et validation d'un code.
- Priorité technique : maintenir un front léger pour mobile.
- Priorité confiance : expliciter les règles du jeu, l'usage des données et l'état de la participation.
- Priorité exploitation : back-office lisible et orienté décisions métier.

### C.5 Mapping concurrentiel (à produire)

Axes recommandés pour le mapping :

- Axe X : lisibilité/praticité parcours digital.
- Axe Y : intensité de marque premium.

Positionnement attendu :

- Thé Tip Top doit se situer dans la zone "forte praticité + image premium lisible".

### C.6 Analyse de stratégie - cibles

#### Cibles

- Cible principale : consommateurs de thé/infusions 25-45 ans, usage régulier, sensibles qualité.
- Coeur de cible : urbains actifs 28-38 ans, appétence digitale, recherche produits premium.
- Cible secondaire : acheteurs occasionnels attirés par le jeu-concours et la découverte.

#### Motivations principales

- Découverte de produits,
- opportunité de gain immédiat,
- confiance dans la marque et simplicité du parcours.

### C.7 Grille d'analyse d'état d'esprit (format)

Contexte type : "Utilisateur en mobilité souhaitant vérifier rapidement un code ticket".

Éléments à renseigner pour chaque cible :

- ce que la cible pense/ressent,
- ce qu'elle voit (concurrence/offres),
- ce qu'elle dit/fait,
- ses freins,
- ses gains attendus.

### C.8 Personas (à intégrer en version visuelle)

Personas minimum à produire :

- Persona 1 : coeur de cible digital.
- Persona 2 : cible principale orientée découverte produit.
- Persona 3 : cible secondaire opportuniste concours.

Pour chaque persona :

- identité et profil socio-démographique,
- usages web/mobile/réseaux,
- motivations et freins,
- attentes vis-à-vis du jeu-concours.

### C.9 Tableau des acteurs (format attendu)


| Rôle        | Enjeux                           | Atouts            | Handicaps             | Stratégie                   |
| ----------- | -------------------------------- | ----------------- | --------------------- | --------------------------- |
| Participant | Gagner un lot rapidement         | Motivation élevée | Faible patience       | Parcours ultra-court        |
| Boutique    | Remettre les lots sans litige    | Proximité client  | Charge opérationnelle | Interface remise simplifiée |
| Marketing   | Booster acquisition/fidélisation | Pilotage campagne | Pression résultats    | KPI hebdo + optimisations   |
| Direction   | ROI et image de marque           | Décision rapide   | Risque réputationnel  | Gouvernance claire/crise    |


### C.10 Zone de chalandise (à produire)

Livrable attendu :

- carte de la zone actuelle + zone(s) d'extension,
- légende explicite,
- justification des zones au regard du besoin concours (et non seulement boutiques existantes).

## D. Stratégie de communication digitale

### D.1 Objectifs de communication (online/offline)

La stratégie de communication du jeu-concours poursuit quatre objectifs prioritaires :

- accroître la notoriété de l'opération sur la période active du concours,
- générer un volume élevé de participations qualifiées,
- enrichir la connaissance client dans un cadre RGPD conforme,
- convertir l'opération ponctuelle en levier de fidélisation post-concours.

#### Objectifs SMART proposés (version de travail)

- Atteindre un volume de sessions qualifiées défini avant ouverture (objectif à calibrer après baseline Analytics).
- Maintenir un taux de conversion "visite -> participation validée" cible.
- Limiter le taux d'abandon sur le parcours de saisie de code.
- Constituer une base de consentements exploitables pour les actions CRM post-opération.

### D.2 Stratégie éditoriale

Le ton éditorial recommandé est premium, rassurant et pédagogique :

- premium pour rester cohérent avec l'image Thé Tip Top,
- rassurant pour lever les freins liés aux données personnelles,
- pédagogique pour expliquer clairement les règles du concours.

Principes de contenu :

- message court orienté action sur les points d'entrée,
- transparence sur les mécaniques de participation et de gain,
- cohérence visuelle et verbale entre site, réseaux sociaux et emails.

### D.3 Gestion de l'e-réputation et gestion de crise

#### Dispositif de social listening

- fréquence minimale : 2 points de contrôle par semaine pendant la campagne,
- suivi des mentions marque + campagne + mots-clés associés,
- qualification des retours en 3 niveaux : neutre, sensible, critique.

#### Plan de réponse

- Niveau 1 (question simple) : réponse publique standard sous 24h.
- Niveau 2 (insatisfaction) : bascule en prise en charge individualisée.
- Niveau 3 (risque bad buzz) : cellule courte client/agence + message validé unique.

### D.4 SEO (levier organique)

Le SEO doit soutenir la découverte naturelle de l'opération et la compréhension rapide des règles.

Préconisations prioritaires :

- structure sémantique propre (title, meta description, Hn cohérents),
- page concours orientée intention de recherche (jeu concours + marque + thématique),
- optimisation mobile-first et performance de chargement,
- maillage interne clair vers règlement, FAQ, contact.

Contenus SEO à produire :

- page d'accueil concours (objectif conversion),
- page de présentation de l'opération (objectif réassurance + information).

### D.5 SMO (réseaux sociaux)

#### Plateformes recommandées

- Instagram : visibilité visuelle, storytelling, activation courte.
- Facebook : portée large et relais local pour les boutiques.
- Option TikTok (si ressources) : format court et viralité.

#### Cadence recommandée (phase active)

- 3 à 4 publications/semaine selon plateforme,
- alternance formats : rappel règles, preuve sociale, mise en avant lots, compte à rebours.

#### Partenariats influence

- privilégier des micro-influenceurs cohérents avec l'univers thé/lifestyle,
- contractualiser livrables, calendrier et obligations de transparence,
- suivre un KPI simple : trafic qualifié et participations générées.

### D.6 Emailing

Le canal email intervient sur trois moments :

- onboarding (confirmation de compte et rappel des règles),
- activation (rappel avant clôture),
- fidélisation (post-concours, offres et contenu marque).

Exigences :

- consentement explicite,
- segmentation minimale (nouveaux participants, participants actifs, inactifs),
- fréquence maîtrisée pour éviter la pression commerciale excessive.

### D.7 Mesure de performance

Le pilotage est assuré via Google Analytics 4 et des KPI orientés décision :

- trafic qualifié vers la page concours,
- taux de conversion inscription,
- taux de conversion saisie de code,
- taux d'abandon sur les étapes clés,
- performance des sources d'acquisition.

Gouvernance de mesure :

- revue hebdomadaire pendant la campagne,
- ajustements contenus/canaux à chaque sprint,
- archivage des décisions prises et de leur impact.

### D.8 Contraintes légales à intégrer dans la communication

- conformité CNIL sur cookies et consentement,
- informations claires sur traitement des données et finalités,
- transparence des règles du concours et modalités d'attribution des lots,
- mention explicite du caractère fictif étudiant sur l'environnement pédagogique si applicable.

## E. Cahier des charges fonctionnel

### E.1 Use cases prioritaires

#### Use case 1 - Participer au jeu-concours (acteur : Participant)

- Précondition : le participant possède un code ticket valide.
- Scénario nominal :
  1. L'utilisateur crée un compte ou se connecte.
  2. Il saisit un code ticket.
  3. Le système vérifie la validité et l'état du code.
  4. Le système affiche le résultat (gain associé).
  5. Le gain est ajouté à l'historique participant.
- Exceptions :
  - code invalide,
  - code déjà utilisé,
  - période de participation expirée.

#### Use case 2 - Valider la remise d'un lot (acteur : Employé boutique)

- Précondition : le participant présente un justificatif d'identité et son gain.
- Scénario nominal :
  1. L'employé recherche le gain via identifiant participant ou code.
  2. Le système affiche le statut du gain.
  3. L'employé confirme la remise.
  4. Le système trace l'opération (date, point de vente, opérateur).
- Exception :
  - tentative de remise sur un gain déjà remis.

### E.2 Arborescence cible (webapp)

- `/` : page concours (présentation + CTA)
- `/inscription` : création de compte
- `/connexion` : authentification
- `/participer` : saisie code ticket
- `/mes-gains` : historique participant
- `/reglement` : règles officielles du concours
- `/faq` : questions fréquentes
- `/backoffice` : dashboard administration
- `/boutique/remise` : interface remise lot

### E.3 Diagrammes d'activité attendus

Deux diagrammes d'activité minimum à fournir :

- activité "parcours participant" (inscription -> saisie code -> résultat),
- activité "remise de lot en boutique" (vérification -> validation -> traçabilité).

Statut actuel : structure validée, réalisation graphique à finaliser.

### E.4 Diagrammes de séquence attendus

Deux diagrammes de séquence minimum à fournir :

- séquence "soumission code -> validation API -> attribution gain",
- séquence "validation remise -> mise à jour statut gain -> traçabilité".

Statut actuel : structure validée, réalisation graphique à finaliser.

### E.5 Modèle de données (MLD cible simplifié)

Entités métier principales :

- `User` (participant, admin, employé boutique),
- `TicketCode` (code, statut, gain associé),
- `Prize` (type de lot, catégorie, valeur),
- `Participation` (horodatage, code utilisé, résultat),
- `PrizeClaim` (remise/expédition, statut, preuve),
- `AuditLog` (action, acteur, date, contexte).

## F. Cahier des clauses techniques détaillées

### F.1 Technologies et compatibilité

#### Stack cible

- Front webapp : framework JS moderne (React ou équivalent).
- API : Node.js/TypeScript (ou stack backend validée équipe).
- Base de données : PostgreSQL (recommandé pour intégrité transactionnelle).
- Authentification : email/mot de passe + OAuth (Google/Facebook) selon cadrage.

#### Compatibilité navigateurs (minimum cible)

- Chrome : version n-2
- Firefox : version n-2
- Edge : version n-2
- Safari : version n-2
- Responsive : mobile/tablette/desktop

### F.2 Outils projet

- Gestion projet : Trello ou Notion (accès public jury).
- Design : Figma.
- Dev : GitHub, VS Code/Cursor, Docker.
- Qualité : Lighthouse, WAVE, validateur HTML/CSS.
- Analytics : Google Analytics 4.

### F.3 Tests applicatifs

Plan de tests recommandé :

- tests unitaires API (règles de validation codes),
- tests d'intégration (API <-> base),
- tests fonctionnels (parcours utilisateur clés),
- tests de charge basique sur endpoint de validation de code.

Critères de validation minimum :

- aucune régression bloquante sur parcours inscription/participation,
- cohérence des statuts code et gain,
- traçabilité complète des opérations sensibles.

### F.4 Hébergement et nom de domaine (site concours)

- Hébergement : offre cloud ou VPS adaptée à un pic de trafic temporaire.
- Domaine : respecter strictement la nomenclature pédagogique imposée.
- HTTPS obligatoire.
- Sauvegardes :
  - base de données quotidienne,
  - conservation glissante,
  - test de restauration documenté.

### F.5 Exigences non fonctionnelles

- Performance : temps de réponse API stable sur les endpoints critiques.
- Sécurité : validation stricte des entrées, protection brute force, logs d'audit.
- Accessibilité : niveau WCAG AA visé sur les écrans clés.
- Conformité : RGPD, politique cookies, mentions légales.

## G. Identité visuelle et charte graphique

### G.1 Recherches de logo (méthode)

Trois axes créatifs sont recommandés pour la phase de recherche :

- Axe 1 : premium botanique (nature, qualité, savoir-faire).
- Axe 2 : contemporain épuré (digital-first, lisibilité maximale).
- Axe 3 : héritage modernisé (ancrage marque + codes actuels).

Pour chaque axe, prévoir 3 déclinaisons :

- version principale horizontale,
- version compacte/icône,
- version monochrome.

### G.2 Logo retenu (cadre de décision)

Le logo final sera retenu selon des critères objectifs :

- lisibilité multi-support,
- cohérence avec le positionnement premium accessible,
- capacité d'adaptation digital/print,
- conformité accessibilité contrastes.

### G.3 UX Mapping

Cartographies UX à produire :

- empathy map (participants cibles),
- experience map (parcours découverte -> participation -> gain),
- pain points map (frictions critiques),
- opportunités d'amélioration priorisées.

### G.4 Zoning

Zonings minimum à fournir en responsive (desktop/tablette/mobile) :

- page d'accueil concours,
- page connexion/inscription,
- page profil / mes gains.

### G.5 Wireframes

Wireframes minimum (desktop/tablette/mobile) :

- page d'accueil concours (orientation conversion),
- tunnel inscription/connexion,
- écran saisie code ticket,
- écran historique des gains,
- vue back-office de synthèse.

### G.6 Maquettes

Maquettes haute fidélité attendues :

- parcours utilisateur principal complet,
- variantes mobile-first prioritaires,
- composants réutilisables documentés (boutons, formulaires, statuts).

### G.7 Charte graphique

La charte devra documenter au minimum :

- palette couleurs (CMJN, RVB, HEX) et usages autorisés,
- contrastes validés (WCAG AA sur combinaisons clés),
- typographies (titres, texte courant, fallback, licences),
- iconographie et styles visuels autorisés/interdits,
- règles d'usage logo.

## H. Cahier de légalité

### H.1 Mentions légales

Le site concours devra intégrer des mentions légales adaptées au cadre projet, incluant :

- identification éditeur,
- hébergeur,
- contact,
- périmètre de responsabilité,
- mention explicite du caractère pédagogique/fictif si requis.

### H.2 Conditions générales d'utilisation (CGU)

Les CGU devront couvrir :

- objet du service,
- conditions d'inscription/participation,
- règles d'utilisation du compte,
- gestion des données personnelles,
- limites de responsabilité,
- modalités de contestation.

### H.3 Spécifiques jeu-concours

Le règlement concours et ses modalités devront être accessibles et lisibles :

- période d'éligibilité,
- conditions de participation,
- règles d'attribution des lots,
- modalités de remise des gains,
- gestion des litiges.

## I. Matrices et Gantt

### I.1 WBS (Work Breakdown Structure)

Le projet doit être décomposé en lots hiérarchisés :

1. Cadrage et analyse
2. UX/UI et identité visuelle
3. Conception fonctionnelle et technique
4. Développement API
5. Développement webapp/back-office
6. Recette et conformité
7. Mise en ligne et suivi

### I.2 Méthodes de priorisation et gouvernance

- MoSCoW : tri des fonctionnalités (Must/Should/Could/Won't).
- Eisenhower : priorisation des tâches selon impact/urgence.
- RACI : responsabilités claires par lot.

### I.3 Matrice des risques

Registre minimal attendu :

- identifiant risque,
- nature (technique, juridique, planning, qualité),
- probabilité,
- impact,
- responsable prévention,
- action préventive,
- action corrective.

Exemples de risques prioritaires :

- surcharge trafic sur endpoint de validation code,
- non-conformité RGPD/cookies,
- retard de livraison des maquettes,
- dérive de périmètre en cours de sprint.

Registre initial (version exploitable) :


| ID  | Nature    | Description                    | Probabilité | Impact | Responsable         | Préventif              | Correctif                           |
| --- | --------- | ------------------------------ | ----------- | ------ | ------------------- | ---------------------- | ----------------------------------- |
| R1  | Technique | Pic de charge validation codes | Moyenne     | Élevé  | Lead technique      | Test de charge + cache | Limitation débit + scaling          |
| R2  | Juridique | Non-conformité cookies/RGPD    | Moyenne     | Élevé  | Référent conformité | Revue CNIL + CMP       | Correction bannière et consent logs |
| R3  | Planning  | Retard maquettes               | Moyenne     | Moyen  | Chef de projet      | Jalons intermédiaires  | Repriorisation backlog              |
| R4  | Produit   | Dérive périmètre               | Élevée      | Moyen  | PO/Chef de projet   | MoSCoW strict          | Arbitrage sprint review             |


### I.4 PERT

Le réseau PERT devra matérialiser :

- dépendances majeures entre lots,
- chemin critique,
- marges de manoeuvre.

Tableau d'antériorité minimal à compléter avant export Gantt :


| ID tâche | Tâche              | Durée estimée | Antécédent(s) |
| -------- | ------------------ | ------------- | ------------- |
| T1       | Cadrage besoin     | 3j            | -             |
| T2       | Benchmark détaillé | 4j            | T1            |
| T3       | UX/UI              | 5j            | T1,T2         |
| T4       | Conception API     | 3j            | T2            |
| T5       | Dev API            | 6j            | T4            |
| T6       | Dev webapp         | 6j            | T3,T4         |
| T7       | Tests/recette      | 4j            | T5,T6         |
| T8       | Mise en ligne      | 2j            | T7            |


### I.5 Gantt

Le Gantt final (MS Project ou GanttProject) doit contenir :

- tâches par lot,
- ressources affectées,
- jalons de validation,
- prédécesseurs,
- pourcentage d'avancement,
- coûts par lot.

## J. Devis

### J.1 Devis principal

Le devis principal couvre l'ensemble du cycle :

- cadrage,
- conception,
- réalisation,
- tests,
- déploiement,
- pilotage projet.

Version chiffrée simplifiée (à adapter avec vos TJM réels) :


| Lot                      | Charge (j) | TJM moyen | Montant       |
| ------------------------ | ---------- | --------- | ------------- |
| Cadrage/benchmark        | 7          | 450 EUR   | 3150 EUR      |
| UX/UI + conception       | 8          | 450 EUR   | 3600 EUR      |
| Développement API/webapp | 12         | 500 EUR   | 6000 EUR      |
| Tests/recette            | 4          | 450 EUR   | 1800 EUR      |
| Déploiement/pilotage     | 4          | 500 EUR   | 2000 EUR      |
| **Total HT**             | 35         |           | **16550 EUR** |


### J.2 Devis optionnels

Options recommandées à présenter séparément :

- accompagnement communication digitale renforcée,
- maintenance évolutive post-concours,
- formation des équipes boutique et marketing,
- amélioration continue analytics/CRM.

### J.3 Mentions obligatoires

Chaque devis devra contenir :

- informations légales émetteur/destinataire,
- date et numéro de devis,
- validité,
- conditions de paiement,
- périmètre inclus / exclus,
- hypothèses et limites.

Informations à ajouter dans la version finale :

- TVA applicable et total TTC,
- échéancier de paiement (ex: 40/40/20),
- pénalités de retard éventuelles,
- durée de validité du devis.

## Annexe - Preuves A-C et stratégie Analytics

### A.1 Dossier de preuves à constituer

- Fiches de veille datées avec décision associée.
- Captures d'audits concurrents (outils + captures manuelles).
- Tableau de synthèse forces/faiblesses par concurrent.
- Traçabilité des sources (URL + date d'accès + extrait utile).

### A.2 Stratégie Google Analytics (phase initiale)

Objectif : commencer à accumuler des preuves mesurables dès l'environnement de démo.

Événements GA4 à implémenter en priorité :

- vue page concours,
- soumission formulaire d'inscription,
- soumission code ticket,
- clic CTA principal,
- consultation historique des gains.

Preuves attendues :

- capture DebugView/Realtime,
- capture rapport événement personnalisé,
- tableau de correspondance "objectif métier -> événement mesuré".

### A.3 Hypothèses restantes à arbitrer avant sections suivantes

- niveau de profondeur des canaux sociaux à activer pendant le projet,
- politique de conservation des données participants,
- critères exacts de segmentation CRM pour l'emailing post-concours.