# Stratégie emailing — Thé Tip Top

**Projet :** jeu-concours Thé Tip Top, objectif n°2  
**Section du cahier des charges :** D.5 — Emailing  
**Version :** 1.0 — 25/09/2026  
**Statut :** préconisation pour le MVP et l'exploitation future ; aucune campagne ni aucun compte prestataire n'est présenté comme déjà créé.

## 1. Finalité et périmètre

L'email accompagne le participant dans le jeu-concours, sécurise les étapes importantes et, uniquement si la personne a accepté de recevoir des communications commerciales, permet de prolonger sa relation avec Thé Tip Top. Le site demandé est celui du **jeu-concours**, et non une boutique en ligne complète. Le client a précisé que le MVP à présenter pour la rentrée et l'examen est limité à la webApp : aucune connexion réelle aux caisses ou au futur site e-commerce ne doit être annoncée dans les emails. [file:7][file:28]

Deux circuits sont séparés dès la conception :

1. **Service du jeu :** emails nécessaires au compte, à la participation, à la sécurité et à la gestion des lots ; contenu strictement informatif.
2. **Marketing :** newsletter et messages promotionnels adressés seulement aux personnes dont l'inscription dans la liste marketing est licite et documentée ; pour ce MVP, l'équipe retient par prudence une case de consentement dédiée, facultative et décochée par défaut.

La création du compte et la participation ne valent pas abonnement à la newsletter. Même un message présenté comme « conseil autour du thé » peut relever de la prospection s'il vise à promouvoir la marque ou ses produits. [web:32][web:33]

## 2. Objectifs et indicateurs

| Objectif | Type de message | Indicateur | Cible de travail, non garantie |
| --- | --- | --- | --- |
| Permettre au participant de retrouver son accès | Service | Emails de création/réinitialisation délivrés, erreurs | Vérifier 100 % des scénarios de test avant examen |
| Rassurer sur le résultat et la remise du lot | Service | Emails envoyés après action, taux d'échec, tickets support | Chaque changement de statut prévu dans le MVP est testé |
| Réduire les codes non saisis avant la date limite | Service, si rappel justifié par le fonctionnement du jeu | Rappels délivrés, codes validés ensuite | Décision après test de charge et rédaction du règlement |
| Développer une audience volontaire | Marketing | Taux d'opt-in, preuves de consentement, désabonnements | Mesurer sans promettre de volume avant lancement |
| Entretenir la relation avec les abonnés | Marketing | Clics, désinscriptions, visites attribuables | Bilan après chaque campagne |

Les objectifs de portée et de vente ne sont pas présentés comme des résultats acquis. Dans le MVP sans intégration caisse/e-commerce, il n'est pas possible de prouver un chiffre d'affaires directement attribuable aux emails. [file:28]

## 3. Origine des données et segmentation

| Population | Origine de l'adresse | Utilisation permise dans le projet | Exclusion / précaution |
| --- | --- | --- | --- |
| Participant avec compte | Formulaire classique de la webApp | Messages indispensables au compte et à la participation | Ne pas l'ajouter automatiquement à la liste marketing |
| Participant via Google ou Facebook | Adresse communiquée dans le parcours de connexion, selon les permissions effectivement accordées | Messages nécessaires au compte et au jeu | Contrôler les données réellement fournies ; pas d'opt-in déduit de la connexion sociale |
| Abonné à la newsletter | Case dédiée lors de l'inscription, décochée par défaut | Contenus promotionnels dans la limite de la finalité annoncée | Garder la date, la source, le texte du consentement et son retrait |
| Ancien client figurant dans une base externe | Données éventuelles de Thé Tip Top | **Hors MVP** tant que l'origine et les droits d'utilisation ne sont pas documentés | Ne pas importer par défaut |
| Liste achetée, adresse collectée sur réseau social | Aucune provenance maîtrisée | **Non retenue** | Ne pas acheter ou aspirer de bases pour ce concours |

Le client mentionne nom, prénom, adresse et email comme données classiques, et demande un formulaire d'effacement. L'adresse postale n'est pas à transmettre au prestataire emailing sauf nécessité démontrée pour le message concerné ; elle reste dans la webApp lorsqu'elle est nécessaire à la remise d'un lot. L'email et, facultativement, le prénom suffisent aux modèles présentés ici. [file:28][web:32]

**Séparation pratique :** `participants` dans la base du jeu ; `abonnes_marketing` dans le prestataire, alimentée uniquement après l'opt-in ; `oppositions` pour éviter toute réinscription ou relance indue après désabonnement. Le statut marketing doit être consultable et modifiable dans la webApp. [web:32]

## 4. Plan de messages

Les dates exactes de jeu et la remise des lots ne sont pas renseignées dans les réponses client. Les échéances ci-dessous sont donc relatives aux événements et devront être raccordées au règlement public. [file:7][file:28]

| Message | Public et provenance | Déclenchement / fréquence | Contenu strictement nécessaire | Consentement marketing ? | Priorité |
| --- | --- | --- | --- | --- | --- |
| Confirmation de création de compte | Participant inscrit sur la webApp | Une fois après inscription, si le compte utilise un email | Lien de connexion, rappel du règlement et contact support | Non, si contenu strictement lié au service | MVP |
| Réinitialisation du mot de passe | Participant concerné | À sa demande, à chaque demande valide avec limitation d'abus | Lien à durée de vie limitée ; aucun mot de passe en clair | Non | MVP |
| Confirmation de participation et résultat | Participant ayant utilisé un code valide | Après validation du code, si l'envoi est retenu dans le parcours | Lot réellement attribué, statut, accès à l'espace et modalités validées | Non, sans promotion ajoutée | MVP si techniquement réalisable |
| Information de remise ou de changement de statut | Participant concerné | À la mise à jour par le caissier ou l'administrateur | Statut réel « remis » / « à réclamer », sans promesse de stock non vérifiée | Non, si utile au suivi du gain | Option MVP |
| Rappel de date limite de saisie | Participant avec code connu mais non saisi, **uniquement si cet état est suivi de manière fiable** | Un rappel maximum, à une date définie par le règlement | Délai officiel, lien vers l'espace et assistance | À qualifier par finalité ; ne pas intégrer de vente | Option, pas de simulation trompeuse |
| Newsletter de découverte | Personne inscrite volontairement à la liste marketing | Une fois par mois maximum au départ | Produits, savoir-faire et actualités de la marque ; lien de désinscription | Oui dans l'option prudente retenue | Après MVP |
| Offre ou relance promotionnelle | Abonné marketing uniquement | Ponctuellement, après validation d'une offre réelle | Offre exacte, prix, durée, conditions et désinscription | Oui dans l'option prudente retenue | Après MVP |

Le tirage final, l'éligibilité après J+30 et la date d'annonce du grand gagnant doivent correspondre au règlement arrêté ; aucun email « vous avez remporté le gros lot » n'est prévu sans vérification du résultat et de l'identité. Le sujet prévoit une chance par personne pour ce tirage, quel que soit le nombre de codes. [file:7]

## 5. Pourquoi choisir Brevo

**Prestataire recommandé : Brevo**, sous réserve de vérification du contrat, des conditions de traitement des données, de l'offre et des prix au moment de la création du compte. Ce choix est une préconisation de l'agence, pas une préférence exprimée par le client.

| Critère | Intérêt pour Thé Tip Top | Limite à prendre en compte |
| --- | --- | --- |
| Compte gratuit | Permet une démonstration et la création d'un template sans budget d'envoi initial | Plafond de 300 emails par jour sur l'offre gratuite ; insuffisant pour un concours à forte volumétrie |
| API transactionnelle et SMTP | Intégration possible à la webApp sans intégration caisse/e-commerce | Il faut vérifier le domaine expéditeur, protéger la clé API et tester les erreurs |
| Éditeur de modèles et campagnes | Permet de produire le template demandé par le référentiel et de séparer service et marketing | La séparation doit aussi exister dans les listes et le code applicatif |
| Gestion des retours | Statuts et webhooks de livraison, rebonds et désabonnements | La preuve de livraison n'est pas une preuve que le destinataire a lu l'email |

Brevo annonce un essai gratuit à **300 emails par jour** et indique que ses offres donnent accès aux emails transactionnels via API/SMTP. La documentation confirme l'utilisation d'un expéditeur vérifié, de modèles et de webhooks. [web:37][web:34]

**Point de capacité :** 500 000 codes représentent un maximum de tickets prévus dans le sujet, **pas** 500 000 adresses emails ou 500 000 envois automatiques. Néanmoins, à titre de scénario de dimensionnement, si 500 000 confirmations de participation devaient partir sur les 30 jours de jeu, cela représenterait environ **16 667 envois par jour en moyenne**, avant les autres emails. L'offre gratuite ne serait donc qu'un outil de démonstration ; une offre payante ou des crédits dimensionnés sur les prévisions d'envoi réelles sont à chiffrer auprès du prestataire. Ne pas faire figurer un abonnement chiffré inventé dans le devis. [file:7][web:37]

**Coût de référence dans le cahier :** création et tests sur le plan gratuit à 0 €/mois dans la limite de 300 emails/jour ; exploitation réelle : coût **à confirmer par devis** après estimation des comptes, des événements déclencheurs et du volume d'envoi. Ajouter séparément le temps d'intégration et de maintenance calculé avec le TJM de l'équipe. [web:37][file:5]

## 6. Mise en œuvre dans le MVP

1. Créer un compte Brevo gratuit réservé à la démonstration, avec l'identité de l'agence ou de l'entité autorisée pour l'exercice ; documenter à qui il appartient.
2. Définir un expéditeur vérifié et authentifier le domaine d'envoi retenu ; ne pas utiliser un domaine fictif dans un vrai envoi.
3. Créer deux espaces logiques : messages transactionnels et contacts marketing opt-in ; définir des listes et tags distincts.
4. Produire au minimum **un template réel** dans l'éditeur et une version texte lisible. Le modèle proposé en section 7 peut servir de base.
5. Lier la webApp au prestataire côté serveur par l'API transactionnelle ; conserver la clé API dans un secret non versionné ; tester les erreurs et les envois à une boîte contrôlée par l'équipe.
6. Envoyer un email de test à un compte de démonstration et conserver la preuve technique : capture du modèle, envoi d'essai, réception, lien cliquable et journal de livraison.
7. Préparer la politique de traitement des rebonds, désinscriptions et demandes d'effacement avant toute utilisation marketing.

La documentation Brevo permet d'envoyer des emails transactionnels par API avec `sender`, `to` et un contenu ou un `templateId`, et de suivre des événements de délivrabilité. Le référentiel impose expressément le compte gratuit lié au site et un template créé ; une simple rédaction dans le cahier ne suffit donc pas à prouver la réalisation. [web:34][file:5]

**Important :** ne jamais utiliser de vrais comptes clients ni importer un fichier de participants fictifs présenté comme réel pour la soutenance. Les envois de test restent internes à l'équipe.

## 7. Modèle d'email à créer

### Confirmation de participation — transactionnel

**Nom du modèle Brevo :** `TTT_Confirmation_Participation`  
**Expéditeur affiché :** `Thé Tip Top <[EXPEDITEUR_VERIFIE]>`  
**Objet :** `Votre participation au jeu-concours Thé Tip Top`  
**Pré-en-tête :** `Consultez votre lot et les modalités de remise dans votre espace.`

> Bonjour [Prénom],
>
> Votre code de participation a été validé. Le lot associé est : **[Nom exact du lot]**.
>
> Son statut actuel est : **[Statut issu de la webApp]**. Pour consulter les modalités de remise et votre historique, connectez-vous à votre espace personnel : **[Lien officiel de la webApp]**.
>
> Vous trouverez les dates, les conditions de participation et le règlement ici : **[Lien vers le règlement public]**.
>
> Pour toute question concernant ce gain, utilisez **[Lien vers l'assistance]**. Ne communiquez pas votre code complet par réponse à cet email ou sur les réseaux sociaux.
>
> À bientôt,  
> L'équipe Thé Tip Top
>
> **Informations sur vos données :** [Lien vers la politique de confidentialité] · [Lien vers le formulaire de demande d'effacement]

**Règles de génération :** le prénom est facultatif ; le lot et le statut proviennent de l'application, jamais d'un texte inventé. Ne pas inclure le code intégral, l'adresse postale, une publicité ou une incitation à un nouvel achat dans ce modèle de service. Ne pas annoncer que le lot a été remis tant que le caissier ne l'a pas enregistré. Le sujet demande l'historique des gains et la possibilité pour le personnel de marquer un lot comme remis. [file:7][file:28]

**Adaptation graphique :** largeur lisible sur smartphone, logo validé, contraste vérifié, texte alternatif du logo et absence d'image indispensable à la compréhension. Couleurs et typographies définitives à reprendre de la charte lorsqu'elle sera finalisée. Un email texte doit rester compréhensible si les images sont bloquées.

### Encadré distinct pour une newsletter, à réaliser seulement avec opt-in

> **Objet :** Découvrez l'univers Thé Tip Top  
> Bonjour [Prénom],  
> Découvrez [contenu produit ou actualité réellement validée].  
> [Lien vers l'information officielle]  
> Vous recevez ce message parce que vous avez accepté les actualités de Thé Tip Top le [date enregistrée].  
> [Se désinscrire] · [Politique de confidentialité]

La newsletter ne doit jamais être ajoutée en bas du modèle de confirmation de participation sous prétexte de « personnalisation ». La CNIL distingue le transactionnel de la prospection, y compris lorsque le message paraît simplement informatif. [web:32]

## 8. Consentement, droits et conservation

**Texte proposé pour la case marketing :**

> ☐ Je souhaite recevoir par email les actualités et offres de Thé Tip Top. Je peux retirer mon accord à tout moment depuis les emails ou mon compte. Cette décision n'a aucun effet sur ma participation au jeu-concours.

La case reste décochée par défaut, distincte de l'acceptation du règlement, des CGU et des conditions de création du compte. Enregistrer la preuve du choix : horodatage, version du libellé, source et statut courant. Le traitement des messages de service est documenté séparément. La CNIL rappelle le principe du consentement préalable pour la prospection B2C, avec une exception encadrée pour certains clients existants ; l'équipe retient ici l'opt-in explicite afin de simplifier et sécuriser le MVP. [web:32][web:33]

Chaque email marketing contient l'identité de l'expéditeur et un moyen simple de se désinscrire. La désinscription prend effet dans la liste marketing et dans toute synchronisation ultérieure ; conserver une liste minimale d'opposition pour ne pas réimporter par erreur une adresse désinscrite. Le formulaire d'effacement demandé par le client est accessible dans la webApp, avec un traitement documenté qui tient compte des éventuelles obligations de conservation liées au jeu. Les durées précises doivent être fixées dans le règlement et la politique de confidentialité : le client n'a pas donné de nombre de mois ou d'années. [web:32][file:28]

Le prestataire doit recevoir seulement les champs nécessaires à l'envoi ; accès limités aux membres habilités, secrets hors dépôt Git et procédure de purge après la période définie. Les données de profil, d'âge ou de sexe éventuellement utilisées dans les statistiques du concours ne deviennent pas automatiquement des critères de ciblage marketing. [file:7][web:32]

## 9. Déclenchements et calendrier

| Moment | Message de service | Message marketing |
| --- | --- | --- |
| Création du compte | Confirmation ou vérification si retenue dans le parcours | Aucun par défaut ; l'opt-in est recueilli séparément |
| Code validé | Confirmation du lot et lien vers l'historique, si le flux d'envoi est actif | Aucun automatiquement |
| Lot remis | Notification de statut si la fonctionnalité existe et est testée | Aucun automatiquement |
| Période additionnelle après les 30 jours du jeu | Information de service ciblée uniquement si l'état du code et la date limite sont fiables | Pas de relance promotionnelle déguisée en rappel de service |
| Après l'opération | Information utile sur le compte si nécessaire | Newsletter mensuelle maximum pour les seuls abonnés opt-in |

Les événements de la webApp doivent être idempotents : un rechargement de page, un double clic ou une relance technique ne doit pas envoyer plusieurs confirmations du même gain. Chaque envoi conserve un identifiant de message et un statut sans stocker inutilement le contenu complet du courrier.

## 10. Indicateurs et bilan

| Indicateur | Calcul ou lecture | Usage |
| --- | --- | --- |
| Envois transactionnels par jour | Nombre par type d'événement | Dimensionner le forfait et éviter de dépasser le quota |
| Taux de délivrabilité | Emails délivrés / emails envoyés | Détecter des problèmes techniques |
| Rebonds et plaintes | Comptes retournés par le prestataire | Corriger les adresses ou la réputation d'envoi |
| Opt-in marketing | Consentements valides / comptes créés | Mesurer une audience réellement volontaire |
| Désinscriptions | Désabonnements / emails marketing délivrés | Ajuster fréquence et pertinence |
| Clics vers la webApp | Liens balisés sans données personnelles | Mesurer l'utilité des contenus ; pas une vente prouvée |
| Erreurs de synchronisation | Écarts entre statut dans la webApp et liste emailing | Éviter les envois après retrait de consentement |

La mesure des ouvertures peut être incomplète ; la priorité est la délivrabilité, les clics utiles et les actions effectivement constatées sur la webApp. Toute mesure du comportement via traceurs doit respecter les choix de consentement applicables. [web:32]

## 11. Budget et charge de travail

| Poste | Position retenue | Chiffrage à inscrire au devis |
| --- | --- | --- |
| Compte gratuit Brevo et modèle de test | À réaliser pour le jury | 0 €/mois d'abonnement, sous réserve des limites du plan |
| Intégration API et tests transactionnels | Travail de l'équipe | Temps × TJM du développeur, à inscrire au Gantt |
| Design du modèle et relecture | Travail de l'équipe | Temps × TJM du graphiste/rédacteur |
| Campagnes commerciales réelles | À décider après examen du plan et de la base opt-in | Volume d'envois × offre/prestation confirmée ; demander un devis |
| Maintenance et suivi de délivrabilité | Option d'exploitation | Temps et coût mensuel estimés, séparés du MVP |

Le référentiel demande le coût du prestataire et une justification : le coût **d'essai** est documenté, tandis que celui de la mise en production doit être quantifié avec une hypothèse de volume et l'offre tarifaire valable à cette date. Le volume potentiel du concours interdit d'assimiler l'offre gratuite au coût d'exploitation définitif. [file:5][web:37][file:7]

## 12. Preuves pour le jury et arbitrages

**Preuves à produire :** capture du compte Brevo gratuit, nom du modèle créé, configuration de l'expéditeur vérifié, preuve de liaison à la webApp, email de test reçu, capture de la case marketing décochée et de la page de désinscription, capture du formulaire d'effacement et mini-rapport des envois. Ne pas présenter ces preuves comme déjà obtenues.

**Informations encore non fixées par le client :** dates exactes, texte final du règlement et durée de conservation, nom de domaine d'envoi, volume prévisionnel de courriels, mode exact de remise de chaque lot, nombre réel de contacts opt-in et coût contractuel d'exploitation. La réunion a indiqué que l'équipe doit prendre les décisions manquantes et que la règle du jeu doit rester publique ; le présent plan avance donc des choix prudents sans leur attribuer à tort une validation client. [file:28]
