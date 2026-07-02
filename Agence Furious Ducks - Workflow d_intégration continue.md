## TRANSFORMATION DIGITALE

# Agence Furious Ducks

## Spécialiste des technologies open source

## TRANSFORMATION DIGITALE

La webagency Furious Ducks est spécialisée dans les technologies open source et existe depuis 2007.
Cette agence est constituée de 45 employés et a pour directeur Mr Guido Brasletti. Ce dernier cherche
à développer son activité mais après plus de 15 ans d'existence Mr Guido Brasletti a constaté qu’une
désorganisation s’est progressivement installée leur faisant perdre en efficacité.

### Objectif n°1 – Agence Furious Ducks

En tant que nouveaux employés au sein de la société Furious Ducks, Mr Guido Brasletti a décidé avec
votre équipe de revoir les méthodes de travail et de mettre en place un workflow de production dans
l’agence.

Travaillant actuellement en cycle en V, Mr Guido Brasletti souhaite évoluer vers des méthodologies de
gestion de projet plus modernes et évolutives comme l’Agile. Votre premier objectif sera donc de
proposer une nouvelle organisation de travail.

Votre second objectif au sein de l'agence sera donc d' **industrialiser** la production des sites en
concevant et en mettant en œuvre un workflow de production. Ce Workflow devra répondre aux
attentes suivantes :

1. Être hébergé sur un ou plusieurs serveurs dédiés ou sur une offre cloud *(ce choix vous revient).*
  Ces serveurs tourneront sur une distribution Linux.
2. Être entièrement basé sur Docker que ce soit les serveurs utiles au workflow ou les serveurs
  que le workflow devra gérer tels que les serveurs de tests, de préproduction/QA et de
    productions, etc.
3. Il devra contenir :
  a. Une solution CI Jenkins
    b. Une solution SCM de type GIT *(Gitlab, Gitea...)*
    c. Une ou plusieurs solutions de tests applicatifs
    d. Une ou plusieurs solutions de backups automatisés
    e. Une ou plusieurs solutions de métriques *(Prometheus, Traefik, Kibana...)*

## TRANSFORMATION DIGITALE

1. La solution CI sera responsable de :
  a. Gérer l’optimisation des assets comme la minification, la compression, etc.
    b. Déployer automatiquement les serveurs de dev
    c. Stocker les images docker construite par votre CI
    d. Déployer les serveurs de pré-production automatiquement
    e. Déployer les serveurs de production *(à vous de déterminer le niveau d’automatisation)*
    f. Exécuter des tests unitaires et/ou des tests fonctionnels
    g. D’envoyer/stocker les rapports de tests
2. La configuration du workflow devra être modifiable par les développeurs sans qu’ils aient
  accès au CI en passant par exemple via les jenkinsfiles.
3. Les applications utilisées pour votre workflow devront être open source *(exemple MariaDB)*
  ou dans le pire des cas libres *(exemple MySQL).*
4. Tous les projets de l’agence seront gérés via votre workflow. Ce dernier devra donc pouvoir
  s'adapter au besoin de chaque client :
       a. Site vitrine HTML-CSS
       b. Site administrable PHP / NodeJS / Python / Ruby
       c. Application Mobile Hybride / Java / Swift
5. Vous devrez automatiser le backup de l’intégralité de votre workflow et des projets gérés avec
  ce dernier.

Sur le long terme, Mr Guido Brasletti souhaite engager quelqu’un pour la partie technique et la
maintenance du workflow. Vous devez donc établir une fiche de poste pour ce recrutement.

Pour ces futures ressources, vous devrez proposer une formation permettant la prise en main facile de
ce Workflow.

## TRANSFORMATION DIGITALE

### Objectif n°2 – Client Thé Tip Top

Afin d’éprouver le nouveau workflow de production, Mr Guido Brasletti a décidé de répondre à la
demande de leur nouveau client « Thé Tip Top » via ce dernier.

Voici quelques informations sur la société Thé Tip Top :

- Gérant : Mr Eric Bourdon
- Siège social : 18 rue Léon Frot, 75011 Paris
- SA au capital Social de 150 000€

Thé Tip Top est une société ayant pour activité la promotion de gammes de thés de très grande
qualité avec des mélanges signatures de l’entreprise, des thés détox, des thés blancs, des thés
légumes, infusions, etc. L’ensemble des thés sont bios et Handmades.

Afin de fêter l’ouverture de leur 10ème boutique à Nice mais surtout afin d'attirer l’attention de
nouveaux clients sur leurs produits, la société Thé Tip Top souhaite organiser un jeu-concours de type
tirage au sort. Ainsi tous les clients ayant un ticket de caisse ou une facture supérieure à 49€
retrouveront sur ces derniers un code à 10 caractères comprenant des chiffres et des lettres
permettant une participation.

100% des tickets seront gagnants, voici la répartition des gains :
● 60% des tickets offrent un infuseur à thé
● 20% des tickets offrent une boite de 100g d’un thé détox ou d’infusion
● 10% des tickets offrent une boite de 100g d’un thé signature
● 6% des tickets offrent un coffret découverte d’une valeur de 39€
● 4% des tickets offrent un coffret découverte d’une valeur de 69€

Le jeu-concours aura lieu sur une période de 30 jours durant lesquels 500 000 tickets maximums
pourront être distribués. Les joueurs auront les 30 jours du jeu concours ainsi que 30 jours
supplémentaires à compter de la date de clôture du jeu pour aller sur le site internet afin tester le
code de leur(s) ticket(s) et réclamer leur lot en magasin ou en ligne.

**Attention : Les codes qui seront présents sur les tickets de caisse devront être générés dès le début
du jeu concours afin de pouvoir respecter obligatoirement les pourcentages de gains. Vous devrez
donc avoir en base de données 500 000 codes qui pourront être utilisés avec leur gains déjà associé.**

À l’issue du jeu-concours, un tirage au sort sera effectué parmi tous les participants afin de déterminer
le gagnant d’un an de thé d’une valeur de 360€.

## TRANSFORMATION DIGITALE

Pour le tirage au sort du gros lot, le nombre de participations d’un client n'augmente pas ses chances
de gagner.

Le règlement et les modalités du jeu-concours ont été déposés auprès de Maître Arnaud Rick huissier
de justice et le tirage au sort du gros lot sera également effectué sous le contrôle de ce dernier.

Thé Tip Top souhaite profiter de ce jeu-concours pour revoir entièrement l’identité visuelle de leur
marque. Vous devez donc être force de proposition à la fois sur le logo et sur le visuel du jeu concours.
Faites bien attention toutefois de coller au mieux à l’activité et au positionnement de votre client.

Afin de faire la promotion du jeu concours, Thé Tip Top souhaite utiliser les réseaux sociaux et
particulièrement faire des partenariats avec influenceurs. Vous devez donc être force de proposition
sur cet aspect.

Le gérant de la société Thé Tip Top souhaite un site dédié au jeu-concours qui devra :

1. Présenter aux clients le jeu-concours et les lots à gagner
2. Permettre aux clients de s’inscrire au jeu-concours via un compte Google/Facebook et via un
  formulaire d’inscription “classique”
3. Permettre de participer au jeu-concours via leur(s) numéro(s) de ticket(s)
4. Permettre aux clients de visualiser l’historique de leurs gains
5. Permettre aux administrateurs de visualiser les statiques du jeu-concours *(nombres de tickets*
  *fournis, nombres de tickets utilisés, nombre de lots déjà gagnés, statistiques sur les gagnants*
    *en termes de sexe, âge, etc.)*
6. Permettre aux administrateurs d’utiliser les données récoltées à des fins d’emailing
7. Permettre aux employés en boutique de visualiser les gains d’un client afin de lui fournir son
  gain et de noter le gain comme remis
8. Évidemment le site devra être accessible à tous devices, respecter les bonnes pratiques
  d’accessibilité et de référencement et être RGPD friendly

**Attention : On ne vous demande pas de réaliser le site internet de Thé Tip Top, mais uniquement le
site du jeu-concours! Le site internet sera à terme refait par une autre agence en fonction de votre
identité visuelle.**

**Le site du jeu-concours sera composé d’une API et d’une webApp, l’API devra communiquer avec
votre webApp ainsi qu’avec les caisses en magasin et le futur site de vente en ligne afin par exemple
de pouvoir récupérer les lots gagnés, tickets, etc.**

**Les différents tirages au sort seront évidemment effectués par votre application côté serveur.**

Enfin, votre agence devra prendre un compte que dans sa démarche éco-responsable votre client Thé
Tip Top souhaite que le projet *(et particulièrement vos préconisations techniques)* soit mené dans une

#### démarche RSE.

## TRANSFORMATION DIGITALE

### Travail demandé

Il vous est donc demandé de réaliser dans un premier temps le cahier des spécifications techniques
pour le workflow et le workflow en lui-même pour l’agence.

Pour ce faire merci de prendre en compte les demandes ainsi que les contraintes suivantes pour la
mise en place du projet :

- Préconisations techniques avec justification des choix techniques des différentes briques
logicielles *(serveur CI, SCM, metrics, reverse proxy...)*
- Diagramme d’infrastructure complet du workflow
- Diagrammes UML et BPNM afin de présenter les procédures mises en place avec le workflow
- Détermination des facteurs-risques
- Une estimation des coûts d’études, de développement et de suivis
- Les différentes procédures rédigées pour les utilisateurs
- Une fiche de poste pour le recrutement d’une ressource pour la gestion et maintenance du
workflow ainsi qu’une proposition de formation
- Une présentation type PowerPoint

Dans un second temps, vous devrez réaliser le cahier des charges et le site internet du jeu-concours
pour le client Thé Tip Top.

Pour ce faire merci de prendre en compte les demandes ainsi que les contraintes suivantes pour la
mise en place du projet :

- Étude marketing complète *(marché, concurrence...)*
- Établissement d’un mix Marketing
- Détermination des facteurs-risques
- Un Gantt complet en ASAP sous MsProject ou Gantt Project obligatoirement
- Une estimation des coûts d’études, de développement et de suivis
- Une présence accrue sur les réseaux sociaux
- La mise en place des outils nécessaires au projet par rapport à vos préconisations *(Google*
*Analytics, Réseaux sociaux...)*
- Une charte graphique cohérente et justifiée
- Une accessibilité pour tous types de lecteurs
- Préconisations techniques avec justification des choix techniques
- Une lisibilité sur tous types de supports
- Une présentation type PowerPoint

**Enfin afin de planifier et de suivre correctement l’avancée de votre projet, nous vous demandons
obligatoirement de mettre un place un outil type Trello ou Notion dont les accès seront à nous
fournir.**