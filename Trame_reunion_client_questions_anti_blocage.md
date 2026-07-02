# Trame réunion client - Questions anti-blocage

Date de réunion :  
Participants :  
Projet : Thé Tip Top - Site jeu-concours + workflow

## Mode d'emploi (pendant la réunion)

- Remplir la colonne **Réponse client** avec les mots du client.
- Formaliser une **décision claire** (pas de zone grise).
- Attribuer un **responsable** et une **deadline**.
- Identifier les points sans réponse dans un lot "A arbitrer".

## 1) Cadrage et périmètre


| Question                                                                     | Réponse client | Décision | Responsable | Deadline |
| ---------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Quel est le périmètre strict de la V1 (must-have) ?                          |                |          |             |          |
| Quelles fonctionnalités sont explicitement hors périmètre pour cette phase ? |                |          |             |          |
| Niveau attendu : prototype avancé, MVP, ou produit prêt à exploiter ?        |                |          |             |          |
| Quels sont les 3 critères de réussite prioritaires ?                         |                |          |             |          |


## 2) Règles métier du jeu-concours


| Question                                                                            | Réponse client | Décision | Responsable | Deadline |
| ----------------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Confirmez-vous 500 000 codes pré-générés et la répartition des gains ?              |                |          |             |          |
| Que fait-on pour un code invalide, déjà utilisé, expiré ou dupliqué ?               |                |          |             |          |
| Un même utilisateur peut-il jouer plusieurs fois ? Y a-t-il un plafond ?            |                |          |             |          |
| Pour le gros lot : confirmez-vous "1 chance par personne" (pas par participation) ? |                |          |             |          |


## 3) Juridique et conformité


| Question                                                                                  | Réponse client | Décision | Responsable | Deadline |
| ----------------------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Quelles clauses obligatoires imposées par l'huissier doivent figurer dans l'application ? |                |          |             |          |
| Quelles données personnelles sont strictement nécessaires et autorisées ?                 |                |          |             |          |
| Quelle durée de conservation des données et des logs ?                                    |                |          |             |          |
| Quelles règles RGPD applicables : consentement, droit à l'oubli, export des données ?     |                |          |             |          |


## 4) Intégrations techniques (zone à risque)


| Question                                                                       | Réponse client | Décision | Responsable | Deadline |
| ------------------------------------------------------------------------------ | -------------- | -------- | ----------- | -------- |
| L'intégration caisses/e-commerce est-elle réelle ou simulée pour cette phase ? |                |          |             |          |
| Disposez-vous d'une documentation API (format, auth, SLA, erreurs) ?           |                |          |             |          |
| Qui fournit les accès et l'environnement de test ?                             |                |          |             |          |
| Quels flux doivent être temps réel et quels flux peuvent être différés ?       |                |          |             |          |


## 5) Exploitation et back-office


| Question                                                                               | Réponse client | Décision | Responsable | Deadline |
| -------------------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Quels KPI sont indispensables dans le dashboard admin ?                                |                |          |             |          |
| Faut-il des exports (CSV/Excel), à quelle fréquence, pour qui ?                        |                |          |             |          |
| Quels rôles et permissions (admin, boutique, marketing) ?                              |                |          |             |          |
| Quelles actions doivent être tracées pour audit (remise lot, correction, annulation) ? |                |          |             |          |


## 6) CI/CD, infrastructure et sécurité


| Question                                                                                 | Réponse client | Décision | Responsable | Deadline |
| ---------------------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Production : déploiement automatique ou validation manuelle (go/no-go) ?                 |                |          |             |          |
| Quelle disponibilité attendue (heures ouvrées / 24-7) ?                                  |                |          |             |          |
| Exigences de sauvegarde : fréquence, rétention, délai max de restauration ?              |                |          |             |          |
| Contraintes sécurité : MFA, chiffrement, localisation de l'hébergement, journalisation ? |                |          |             |          |


## 7) UX, contenu et image de marque


| Question                                                       | Réponse client | Décision | Responsable | Deadline |
| -------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Refonte visuelle totale ou évolution légère de l'existant ?    |                |          |             |          |
| Qui valide les maquettes et sous quel délai ?                  |                |          |             |          |
| Qui fournit les contenus (textes, visuels, mentions légales) ? |                |          |             |          |
| Contraintes de ton, wording, éléments à éviter absolument ?    |                |          |             |          |


## 8) Gouvernance et validation projet


| Question                                                             | Réponse client | Décision | Responsable | Deadline |
| -------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Qui est le décideur final côté client ?                              |                |          |             |          |
| Quel circuit de validation (qui valide quoi, en combien de temps) ?  |                |          |             |          |
| Quel rythme de suivi (hebdo, bi-hebdo) et format de compte rendu ?   |                |          |             |          |
| Quelle procédure en cas de changement de besoin en cours de projet ? |                |          |             |          |


## 9) Budget et planning


| Question                                                                                      | Réponse client | Décision | Responsable | Deadline |
| --------------------------------------------------------------------------------------------- | -------------- | -------- | ----------- | -------- |
| Budget fixe ou ajustable selon les priorités ?                                                |                |          |             |          |
| Date de mise en ligne impérative ?                                                            |                |          |             |          |
| Compromis acceptés en cas de tension (scope, délai, automatisation, design) ?                 |                |          |             |          |
| Contraintes internes bloquantes à anticiper (validation légale, disponibilité équipe, etc.) ? |                |          |             |          |


## Lot "A arbitrer" (si réponse non obtenue en séance)


| Sujet | Impact | Option A | Option B | Arbitrage attendu | Échéance |
| ----- | ------ | -------- | -------- | ----------------- | -------- |
|       |        |          |          |                   |          |
|       |        |          |          |                   |          |
|       |        |          |          |                   |          |


## Compte-rendu de clôture (5 minutes)

- Décisions prises :
- Points à arbitrer :
- Risques majeurs identifiés :
- Actions immédiates (48h) :
- Date de la prochaine réunion :