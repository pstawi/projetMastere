# Stratégie éditoriale — Thé Tip Top

**Projet :** site du jeu-concours Thé Tip Top — objectif n°2  
**Version :** 2.0 — adaptée aux réponses du client  
**Date :** 25/09/2026  
**Statut :** proposition éditoriale pour le MVP et le dossier de soutenance

> Ce document se base sur les réponses réellement obtenues auprès du client. Lorsque le client a répondu que le choix appartenait à l'équipe, la présente stratégie formule une recommandation. Lorsqu'une information n'a pas été précisée, elle reste indiquée comme un point à arbitrer et non comme une décision client.

## 1. Décisions client intégrées

Les réponses client conduisent aux choix suivants :

- La priorité est de terminer un **MVP pour la rentrée** ; le périmètre complémentaire est géré par l'équipe.
- Pour cette phase, l'intégration avec les caisses et le site e-commerce n'est pas réalisée : le périmètre est limité à la **webApp**.
- Le client fournit les accès et l'environnement de test.
- Les données prévues sont les données classiques : nom, prénom, adresse, email et informations nécessaires à la connexion réseau, sous réserve de minimisation et de validation RGPD.
- Un formulaire de demande d'effacement des données doit être prévu.
- Les rôles attendus sont : administrateur et caissier ; le back-office doit aussi permettre la gestion du stock de cadeaux et des KPI par boutique.
- Les exports CSV/Excel ne sont pas obligatoires mais peuvent être proposés comme amélioration.
- Le niveau d'automatisation de la production est laissé au choix de l'équipe.
- L'objectif de disponibilité est un temps d'arrêt minimal en cas de bug ou d'attaque DDoS.
- Les sauvegardes sont prévues toutes les heures, avec une conservation glissante d'une journée.
- L'équipe produit les contenus et les visuels à partir de l'analyse concurrentielle.
- Le budget est à estimer par l'équipe selon le besoin réel du projet.
- La date de mise en ligne est liée à l'examen.

Ces décisions viennent de la trame de réunion client du 07/05/2026. [file:28]

## 2. Rôle de la stratégie éditoriale

La stratégie éditoriale sert à produire des textes cohérents sur la webApp, les réseaux sociaux, les supports de présentation et, si nécessaire, les messages des influenceurs. Elle doit en priorité rendre le MVP compréhensible et rassurant : le participant doit savoir quoi faire, le caissier doit comprendre le fonctionnement du gain et l'administrateur doit disposer d'informations exploitables dans son tableau de bord.

Le projet ne comporte pas d'intégration réelle aux caisses ou au futur e-commerce dans cette phase. Les contenus ne doivent donc pas promettre une synchronisation opérationnelle qui n'est pas livrée dans le MVP. [file:28]

**Ligne directrice :**

> **« Thé Tip Top simplifie le jeu, valorise ses thés et accompagne chaque participant jusqu'à son gain. »**

Le ton doit être chaleureux pour la marque, pédagogique pour les règles, factuel pour les résultats et administratif pour la gestion des données.

## 3. Objectifs éditoriaux du MVP

| Objectif | Public | Réponse éditoriale | Indicateur de réussite |
| --- | --- | --- | --- |
| Faire comprendre le concours | Participant | Expliquer les étapes, la condition liée au ticket/facture, le code et le résultat | Peu de questions répétitives sur le parcours |
| Faciliter la participation | Participant | Formulaire court, libellés clairs, erreurs actionnables | Code correctement saisi et validé |
| Rassurer | Participant et caissier | Règlement public, règles de gain visibles, statut du code explicite | Consultation du règlement et baisse des demandes d'aide |
| Faciliter la remise du gain | Caissier | Afficher le lot, son statut et l'action « remis » | Lot traité sans ambiguïté |
| Piloter l'opération | Administrateur | Libeller clairement les KPI et les stocks par boutique | Dashboard compréhensible et exploitable |
| Protéger les personnes | Tous | Informations minimales, formulaire d'effacement et messages de confidentialité | Demande d'effacement traçable |

Le référentiel demande que la stratégie éditoriale soit liée aux cibles, aux contenus et aux recommandations de communication. [file:5]

## 4. Principes éditoriaux

### 4.1 Clarté avant l'effet promotionnel

Le contenu ne doit pas chercher à créer du suspense au détriment de la compréhension. La condition de participation, les dates du concours, les lots et la procédure de remise doivent être visibles sans devoir interpréter une publicité.

### 4.2 Une action par écran

Chaque écran principal du MVP doit avoir une action prioritaire :

- Accueil : comprendre l'opération et commencer.
- Inscription/connexion : créer ou retrouver son compte.
- Participation : saisir le code.
- Résultat : comprendre le lot et la suite.
- Historique : retrouver ses gains.
- Caissier : vérifier et remettre un lot.
- Administration : lire les KPI et gérer les stocks.

### 4.3 Une information dans le bon vocabulaire

- « Code » : chaîne alphanumérique à saisir.
- « Ticket ou facture » : justificatif indiqué dans le sujet et à confirmer dans le règlement final.
- « Lot associé » : gain lié au code pré-généré.
- « Tirage final » : opération distincte du gain associé au code.
- « Stock disponible » : quantité réellement enregistrée par boutique.
- « Lot remis » : lot effectivement délivré et enregistré par un caissier.

### 4.4 Pas de promesse technique non livrée

Le MVP concerne la webApp. Il ne faut pas écrire que l'application récupère automatiquement les tickets des caisses ou du e-commerce. Une formulation acceptable est : « Les intégrations caisse et e-commerce pourront être prévues dans une évolution ultérieure. » [file:28]

## 5. Ton selon les utilisateurs

| Utilisateur | Ton | Caractéristiques | Exemple |
| --- | --- | --- | --- |
| Visiteur | Chaleureux et explicatif | Présenter la marque, le concours, les lots et les règles | « Découvrez le concours Thé Tip Top et les lots associés aux codes valides. » |
| Participant | Simple, rassurant et direct | Guider l'inscription, la saisie et la réclamation | « Saisissez les 10 caractères de votre code. » |
| Participant ayant gagné | Positif mais précis | Nommer le lot et expliquer la prochaine étape sans ambiguïté | « Votre code est valide. Votre lot est : [nom]. Consultez les modalités de remise. » |
| Participant en erreur | Neutre et aidant | Expliquer ce qui doit être corrigé, sans jugement | « Le code doit contenir 10 caractères. Vérifiez votre saisie. » |
| Caissier | Opérationnel et synthétique | Afficher les informations nécessaires à la remise | « Lot disponible — marquer comme remis après délivrance. » |
| Administrateur | Factuel et analytique | Nommer les indicateurs et les stocks | « Codes utilisés : [nombre] ; lots disponibles par boutique : [détail]. » |
| Support / conformité | Formel et traçable | Diriger vers le règlement, l'effacement ou le contact officiel | « Votre demande d'effacement a été enregistrée. » |

## 6. Messages par cible

Les profils ci-dessous reprennent les hypothèses déjà produites dans la grille d'état d'esprit : cœur de cible mobile-first, consommateurs réguliers et acheteurs occasionnels. [file:25]

| Cible | Message principal | Preuve ou contenu associé | CTA |
| --- | --- | --- | --- |
| Cœur de cible mobile-first | « Participez rapidement depuis votre smartphone. » | Étapes courtes, code à 10 caractères, résultat lisible | « Saisir mon code » |
| Consommateurs réguliers | « Le concours prolonge la découverte des thés Thé Tip Top. » | Présentation des gammes, lots, règlement public | « Découvrir les lots » |
| Acheteurs occasionnels | « Comprenez le parcours en quelques étapes. » | Vidéo courte, FAQ, aide au code | « Participer » |
| Caissiers | « Vérifiez le gain et enregistrez sa remise. » | Fiche lot, statut, stock par boutique | « Vérifier un gain » |
| Administrateurs | « Suivez les codes, les lots et les stocks par boutique. » | Dashboard KPI, filtres, stock cadeau | « Ouvrir le tableau de bord » |

## 7. Architecture éditoriale de la webApp

### 7.1 Accueil

Objectif : expliquer immédiatement le projet et orienter vers la participation.

Contenu recommandé :

- Titre : « Le jeu-concours Thé Tip Top ».
- Sous-titre : « Découvrez les modalités, les lots et la marche à suivre. »
- Étapes en quatre blocs : vérifier son justificatif, retrouver son code, créer un compte, saisir le code.
- Présentation visuelle des lots.
- Encadré sur les dates, une fois confirmées.
- Lien visible vers le règlement public.
- Lien vers la politique de confidentialité et la demande d'effacement.
- CTA : « Participer avec mon code ».

### 7.2 Inscription et connexion

Le sujet impose une inscription classique ainsi que des possibilités via Google/Facebook. Le client prévoit des données classiques : nom, prénom, adresse et email. Le formulaire doit distinguer les champs nécessaires au compte et les consentements facultatifs, notamment l'abonnement marketing. [file:7][file:28]

Texte introductif :

> Créez votre compte pour participer au jeu-concours et retrouver l'historique de vos gains. Les informations demandées servent au fonctionnement du compte et à la gestion de votre participation. Les communications commerciales nécessitent un choix séparé.

Microtextes :

- Email : « Utilisé pour vous connecter et recevoir les informations liées à votre compte. »
- Nom et prénom : « Utilisés pour identifier votre compte et traiter votre gain si nécessaire. »
- Adresse : « Demandée uniquement si elle est nécessaire à la remise ou à l'envoi du lot. »
- Consentement marketing : « Je souhaite recevoir les actualités et offres de Thé Tip Top par email. »
- Effacement : « Vous pouvez demander l'effacement de vos données depuis le formulaire dédié. »

### 7.3 Participation

> **Saisissez votre code**  
> Entrez les 10 caractères indiqués sur votre ticket ou votre facture, puis validez. Ne partagez jamais votre code sur les réseaux sociaux.

Le support exact du code et les conditions d'achat doivent rester identiques au règlement final. Le sujet prévoit un ticket ou une facture supérieur à 49 €. [file:7]

### 7.4 Résultat

> **Votre code est valide.**  
> Votre lot associé est : **[nom exact du lot]**.  
> Consultez les modalités de remise et ajoutez ce résultat à votre historique.

Ajouter, selon le fonctionnement retenu :

- statut « à retirer » ou « remis » ;
- boutique concernée ou choix du mode de remise ;
- délai de réclamation ;
- accès au règlement ;
- rappel du tirage final, sans présenter ce tirage comme une garantie supplémentaire liée au nombre de participations.

### 7.5 Historique des gains

> Retrouvez ici vos participations et le statut de chaque lot : à réclamer, réservé, remis ou expiré.

Chaque entrée doit afficher : date, code masqué, lot, statut, boutique ou mode de remise et date de remise si disponible. Ne jamais afficher un code complet dans un historique accessible à un tiers.

### 7.6 Caissier

> **Recherche d'un gain**  
> Recherchez la participation avec l'identifiant prévu par l'application. Vérifiez le lot et la boutique avant de le délivrer. Après remise effective, sélectionnez « Marquer comme remis ».

Le caissier ne doit voir que les informations nécessaires à la remise, pas l'ensemble des données personnelles du client.

### 7.7 Administration

> **Tableau de bord concours**  
> Consultez les participations, les codes utilisés, les lots gagnés et les stocks cadeaux par boutique.

KPI à prévoir, en cohérence avec le CDC et la réponse client :

- codes générés, distribués et utilisés ;
- participations validées ;
- lots associés, réclamés et remis ;
- stock disponible par type de lot et par boutique ;
- répartition des participations par boutique lorsque l'information existe ;
- données statistiques autorisées sur les participants ;
- demandes d'effacement en cours et terminées ;
- journal des actions sensibles.

Les exports CSV/Excel ne sont pas obligatoires selon la réunion, mais peuvent être proposés comme amélioration pour le marketing et le suivi du stock. [file:28]

## 8. Ligne éditoriale par canal

| Canal | Rôle | Contenu prioritaire | Formulation recommandée |
| --- | --- | --- | --- |
| WebApp | Source de vérité opérationnelle | Règles, étapes, résultat, historique et aide | Précise, complète, sans slogan ambigu |
| Instagram | Découverte et pédagogie visuelle | Présentation des lots, tutoriel, boutique et FAQ | Chaleureuse, courte, renvoi vers le règlement |
| TikTok | Démonstration | Parcours mobile, découverte produit, ouverture de Nice | Naturelle, sous-titrée, factuelle sur les conditions |
| Facebook | Relais local | Informations pratiques, rappels et accès au site | Pédagogique, rassurante et détaillée |
| Influenceurs | Recommandation incarnée | Visite, dégustation, tutoriel et lien vers la webApp | Personnelle mais strictement alignée sur le brief |
| Email transactionnel | Service | Confirmation de compte, résultat, remise du lot | Formel, utile, sans publicité non consentie |
| Email marketing | Fidélisation | Découverte de produits et actualités | Envoyé uniquement selon le consentement prévu |

Le référentiel demande une stratégie d'écriture mise en pratique dans les contenus sociaux, les choix de mots-clés et les recommandations de communication. [file:5]

## 9. Piliers de contenu

| Pilier | Part indicative | Intention | Exemples |
| --- | ---: | --- | --- |
| Comprendre le concours | 40 % | Réduire les blocages | Comment participer, FAQ, dates, règlement |
| Découvrir Thé Tip Top | 25 % | Donner du sens aux lots | Thés bio, mélanges signatures, infusions, accessoires |
| Nice et la proximité | 15 % | Valoriser la boutique et la communauté | Ouverture, équipe, adresse et informations validées |
| Aide et service | 10 % | Résoudre les problèmes | Code non reconnu, lot remis, demande d'effacement |
| Communauté et responsabilité | 10 % | Créer un lien durable | Questions, retours, sobriété, réutilisation de l'infuseur |

## 10. Formats et calendrier de production

Les dates exactes du concours n'ayant pas été renseignées dans la réunion, ce calendrier est exprimé en jalons relatifs à la date officielle de lancement.

| Période | Objectif | Contenus à produire | Responsable |
| --- | --- | --- | --- |
| J-14 à J-8 | Faire connaître la boutique et l'univers | Texte de présentation, photos/vidéos des produits, teaser | Marketing / graphiste |
| J-7 à J-1 | Expliquer le parcours | Carrousel des étapes, FAQ, page règlement, script influenceur | Marketing / conformité |
| J0 à J+7 | Lancer le MVP et guider les premières participations | Publication de lancement, tutoriel, assistance, email de compte | Community manager / support |
| J+8 à J+20 | Entretenir la compréhension | Focus lots, rappel des modalités, questions-réponses | Marketing / caissiers |
| J+21 à fin du concours | Informer sans pression | Rappel de date, conditions et accès au site | Community manager |
| Période de réclamation | Aider à vérifier et retirer les lots | Tutoriel historique, statut des gains, support | Support / caissiers |
| Après clôture | Fidéliser et documenter | Remerciement, bilan, suite du tirage selon règlement | Marketing / administrateur |

La production des textes et visuels est à la charge de l'équipe, sur la base de l'analyse concurrentielle et de la stratégie retenue par le projet. [file:28]

## 11. Exemples de contenus

### 11.1 Texte d'accueil

> **Bienvenue dans le jeu-concours Thé Tip Top**  
> À l'occasion de l'ouverture de notre nouvelle boutique, découvrez les modalités du jeu et les lots associés aux codes valides. Après un achat éligible supérieur à 49 €, retrouvez votre code à 10 caractères sur votre ticket ou votre facture. Créez votre compte, saisissez votre code et consultez votre résultat. Les dates, les lots et les conditions complètes sont disponibles dans le règlement.

### 11.2 Publication sociale

> Une nouvelle adresse Thé Tip Top arrive à Nice.  
> Vous avez réalisé un achat éligible supérieur à 49 € ? Retrouvez votre code à 10 caractères, créez votre compte sur le site du concours et saisissez-le pour consulter votre lot.  
> Conditions, dates et règlement accessibles depuis le lien officiel.

### 11.3 Texte pour influenceur

> Collaboration commerciale avec Thé Tip Top. À l'occasion de l'ouverture de leur nouvelle boutique, un jeu-concours est accessible après un achat éligible supérieur à 49 €. Récupérez le code indiqué sur votre ticket ou votre facture, puis utilisez le site officiel pour participer. Les conditions et le règlement sont accessibles via le lien indiqué.

### 11.4 Email transactionnel : confirmation de compte

**Objet :** Votre compte Thé Tip Top est créé

> Bonjour [Prénom],
>
> Votre compte Thé Tip Top a bien été créé. Vous pouvez maintenant vous connecter au site du jeu-concours et saisir votre code à 10 caractères.
>
> Retrouvez le règlement et la politique de confidentialité depuis votre espace. Pour demander l'effacement de vos données, utilisez le formulaire dédié.
>
> À bientôt,  
> L'équipe Thé Tip Top

### 11.5 Message de gain

**Objet :** Votre résultat au jeu-concours Thé Tip Top

> Bonjour [Prénom],
>
> Votre code a été reconnu. Le lot associé est : **[nom du lot]**.
>
> Consultez votre espace pour connaître le statut du gain et les modalités de remise. Le règlement reste accessible depuis le site.
>
> L'équipe Thé Tip Top

### 11.6 Message d'effacement

> Votre demande d'effacement a bien été enregistrée. Elle sera traitée selon les vérifications nécessaires à la conservation des éléments indispensables au suivi du jeu-concours et à la prévention des fraudes. Un retour vous sera adressé à [adresse email].

Cette formulation doit être validée par le référent RGPD et adaptée à la durée de conservation fixée dans le règlement. [file:28]

## 12. Règles de rédaction

### À faire

- Employer des titres explicites : « Comment participer ? », « Consulter le règlement », « Vérifier mon gain ».
- Donner les informations essentielles avant le bouton d'action.
- Répéter les conditions importantes dans les supports où le gain est mentionné.
- Utiliser des phrases courtes et des listes pour les étapes.
- Décrire clairement une erreur et la correction attendue.
- Prévoir les variantes mobile et desktop.
- Relire les textes avec le règlement final et les valeurs réellement enregistrées en base.

### À éviter

- « Cadeau garanti » sans préciser le code valide et la condition d'éligibilité.
- « Plus vous jouez, plus vous avez de chances » pour le tirage final.
- « Détoxifie », « soigne » ou toute autre promesse de santé non validée.
- Demander un code complet ou des données personnelles en commentaire.
- Affirmer que les caisses et le e-commerce sont connectés dans le MVP.
- Utiliser un texte différent entre la webApp, les réseaux sociaux et le règlement.

## 13. Accessibilité, RGPD et RSE

### Accessibilité

- Contraste suffisant entre texte et arrière-plan.
- Texte de remplacement pour les visuels essentiels.
- Sous-titres pour les contenus vidéo.
- Navigation et formulaires utilisables au clavier.
- Messages d'erreur associés aux champs et compréhensibles sans utiliser uniquement la couleur.
- Informations disponibles en texte et non uniquement via une animation.
- Titres et boutons explicites sur mobile.

### RGPD

- Distinguer les données nécessaires au compte des données facultatives de marketing.
- Présenter la politique de confidentialité et le règlement avant ou pendant l'inscription.
- Ne pas collecter plus de données que nécessaire.
- Prévoir le formulaire d'effacement demandé par le client.
- Protéger l'accès aux données selon les rôles administrateur et caissier.
- Journaliser les actions sensibles côté back-office, conformément à la veille juridique du projet. [file:11][file:28]

### RSE

- Réutiliser les contenus entre réseaux sociaux et réduire les productions inutiles.
- Privilégier des images authentiques des produits et de la boutique.
- Compresser les images et vidéos sans perdre l'information.
- Éviter d'encourager une surconsommation uniquement pour obtenir plusieurs codes.
- Mettre en avant la découverte des produits et la réutilisation de l'infuseur.
- Limiter les impressions et utiliser un support de code lisible, durable et réellement utile.

Le sujet demande explicitement une démarche RSE, une accessibilité sur tous les appareils et une conformité RGPD. [file:7]

## 14. Mesure éditoriale

| Événement | Nom GA4 proposé | Objectif |
| --- | --- | --- |
| Consultation de la page concours | `view_campaign_page` | Mesurer l'intérêt initial |
| Clic sur un CTA | `click_campaign_cta` | Mesurer l'efficacité des textes et boutons |
| Consultation du règlement | `view_rules` | Mesurer la recherche de réassurance |
| Début de saisie | `begin_code_entry` | Mesurer l'entrée dans le parcours |
| Envoi du formulaire | `submit_code` | Suivre la conversion du formulaire |
| Code reconnu | `code_validated` | Mesurer les participations valides |
| Gain affiché | `prize_revealed` | Suivre la révélation du lot |
| Demande d'effacement | `request_erasure` | Suivre le traitement des droits |
| Clic depuis un réseau | `social_cta_click` | Comparer les canaux éditoriaux |

Le référentiel demande des événements pour les vues de page, les formulaires et les clics CTA, ainsi qu'un rapport personnalisé. [file:5]

## 15. Checklist de validation finale

Avant de déplacer la carte « Stratégie éditoriale » dans « Terminé », vérifier :

- [ ] Le ton est défini par type d'utilisateur.
- [ ] Les trois cibles et leurs messages sont présentés.
- [ ] Les piliers de contenu, formats et cadences sont indiqués.
- [ ] Les textes de la webApp et des réseaux sociaux sont rédigés.
- [ ] Le parcours MVP uniquement webApp est respecté.
- [ ] Les rôles administrateur et caissier sont pris en compte.
- [ ] Les KPI par boutique et la gestion des stocks cadeaux sont intégrés.
- [ ] Le formulaire d'effacement est prévu.
- [ ] Le règlement public est mentionné comme source de vérité.
- [ ] Le calendrier relatif reste compatible avec l'absence de dates client.
- [ ] Les contenus partenaires incluent la transparence commerciale.
- [ ] L'accessibilité, le RGPD et la RSE sont traités.
- [ ] Les textes sont relus contre le règlement final avant publication.

## 16. Points non répondus à conserver en « À arbitrer »

Ces points n'ont pas reçu de réponse précise pendant la réunion. Ils ne doivent pas être inventés dans les contenus définitifs :

1. Les fonctionnalités hors périmètre exactes du MVP.
2. Les trois critères de réussite prioritaires.
3. La confirmation opérationnelle de la génération des 500 000 codes, même si elle est imposée par le sujet.
4. Les clauses détaillées demandées par l'huissier.
5. La durée précise de conservation des données et des logs.
6. La durée exacte de traitement d'une demande d'effacement.
7. Les KPI définitifs du dashboard.
8. Les dates exactes de lancement, de clôture et de tirage.
9. Le niveau précis de disponibilité et le plan anti-DDoS.
10. Le format final des contenus et la charte visuelle définitivement validée.

## Sources mobilisées

- Référentiel « Plan cahier des charges » : stratégie éditoriale, SMO, emailing, performance et contraintes de rédaction. [file:5]
- Sujet « Agence Furious Ducks — Objectif n°2 Thé Tip Top » : fonctionnement du concours, webApp, comptes, gains et contraintes RSE/RGPD. [file:7]
- Trame de réunion client du 07/05/2026 : réponses client sur MVP, périmètre webApp, rôles, KPI, sauvegardes, données et contenus. [file:28]
- Veille juridique Thé Tip Top : transparence, règlement public, données personnelles et exigences de conformité. [file:11]
- Grille d'état d'esprit Thé Tip Top : attentes de rapidité, de simplicité et de transparence des trois cibles. [file:25]
