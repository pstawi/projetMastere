# Veille Juridique — Site Jeu-Concours Thé Tip Top

**Projet :** Thé Tip Top — Objectif n°2 (site jeu-concours)
**Agence :** Furious Ducks
**Type de veille :** Veille juridique (RGPD, cookies/traceurs, réglementation jeu-concours)
**Fréquence :** Hebdomadaire (synthèse consolidée en fin de sprint)
**Diffusion :** Équipe projet + référent client
**Dernière mise à jour :** 06/07/2026

---

## Objectifs de cette veille

- Anticiper les contraintes juridiques du jeu-concours et des traceurs.
- Garantir la conformité RGPD/CNIL du site (collecte, consentement, durée de conservation).
- Sécuriser le dispositif face aux obligations de transparence propres aux jeux-concours.

---

## Fiche 1 — Durcissement des contrôles RGPD en 2026

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Renforcement des contrôles RGPD et exigences de sécurité en 2026 |
| **Date** | 06/07/2026 |
| **Source** | [https://solutions.lesechos.fr/juridique/loi-conformite/nouveautes-rgpd-2026-comment-adapter-sa-conformite-des-maintenant/](https://solutions.lesechos.fr/juridique/loi-conformite/nouveautes-rgpd-2026-comment-adapter-sa-conformite-des-maintenant/) |
| **Information clé** | En 2026, la CNIL renforce ses contrôles et exige des preuves continues de conformité, avec des mesures de sécurité plus précises (authentification forte, journalisation des accès, politiques de mots de passe renforcées). |
| **Impact projet** | Le site jeu-concours doit journaliser les accès administrateur/boutique et sécuriser l'authentification (mot de passe robuste, MFA envisageable côté back-office) pour anticiper un contrôle CNIL. |
| **Décision / action** | Intégrer une politique de mot de passe renforcée et un logging des actions sensibles (entité `AuditLog` déjà prévue au MLD) dès la conception de l'API. |
| **Responsable** | Lead technique |
| **Échéance** | Avant le début du développement de l'API (lot 4 du WBS) |

---

## Fiche 2 — Réforme des règles cookies et traceurs

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Anticipation de la réforme "ePrivacy" intégrée au RGPD sur les cookies |
| **Date** | 06/07/2026 |
| **Source** | [https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles) |
| **Information clé** | La Commission européenne prépare une intégration des règles cookies dans le RGPD, avec un encadrement plus strict du suivi en ligne et une clarification attendue des bannières de consentement. Rappel CNIL : refuser les cookies doit être aussi simple que les accepter. |
| **Impact projet** | La bannière cookies du site concours doit déjà respecter ce principe, sans dark pattern, pour ne pas être en décalage avec la réforme à venir et pour rester conforme dès la mise en ligne. |
| **Décision / action** | Utiliser une Consent Management Platform (CMP) conforme CNIL, avec bouton refus visible au même niveau que le bouton acceptation. |
| **Responsable** | Référent conformité / chef de projet |
| **Échéance** | Avant la mise en ligne du site (lot 7 du WBS) |

---

## Fiche 3 — Obligations légales générales du jeu-concours

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Transparence et cadre légal des jeux-concours en ligne (loterie publicitaire) |
| **Date** | 06/07/2026 |
| **Source** | [https://www.legalstart.fr/fiches-pratiques/astuces-entrepreneurs/jeu-concours/](https://www.legalstart.fr/fiches-pratiques/astuces-entrepreneurs/jeu-concours/) |
| **Information clé** | Un jeu-concours en ligne doit disposer d'un règlement complet, accessible facilement depuis le site, précisant les modalités de participation, la période d'éligibilité, les règles d'attribution des lots et les voies de recours en cas de litige. |
| **Impact projet** | Le règlement du concours Thé Tip Top (500 000 codes, répartition des gains 60/20/10/6/4 %) doit être rédigé, déposé auprès de Maître Arnaud Rick (huissier), et accessible via la page `/reglement` du site. |
| **Décision / action** | Finaliser la rédaction du règlement avec le client, prévoir le dépôt chez l'huissier avant l'ouverture du concours, lier la page `/reglement` dans le footer et le tunnel de participation. |
| **Responsable** | Chef de projet / référent conformité |
| **Échéance** | Avant l'ouverture officielle du concours |

---

## Fiche 4 — Cadre légal des loteries publicitaires

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Régime juridique français des jeux-concours en ligne (Code de la consommation, Code de la sécurité intérieure) |
| **Date** | 06/07/2026 |
| **Source** | [https://www.twobirds.com/fr/insights/2025/france/jeuxconcours-en-ligne--vers-un-cadre-juridique-plus-clair](https://www.twobirds.com/fr/insights/2025/france/jeuxconcours-en-ligne--vers-un-cadre-juridique-plus-clair) |
| **Information clé** | Une loterie (hasard + gain + participation financière + public) est en principe interdite en France. Un jeu-concours lié à une opération commerciale est autorisé (article L.121-20 Code conso, article L.320-6 Code sécurité intérieure), à condition de ne pas constituer une pratique commerciale déloyale (trompeuse ou agressive). |
| **Impact projet** | Le concours Thé Tip Top doit s'appuyer sur ce cadre légal de l'opération commerciale : le mécanisme (achat + code ticket) doit être présenté clairement et loyalement dans le règlement et sur le site. |
| **Décision / action** | Faire valider par un juriste/référent conformité que le mécanisme retenu correspond bien à une opération commerciale licite, et non à une loterie interdite. |
| **Responsable** | Chef de projet / référent conformité |
| **Échéance** | Avant validation finale du parcours participant (E.1 use cases) |

---

## Fiche 5 — Dépôt du règlement chez un commissaire de justice (huissier)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Statut du dépôt de règlement auprès d'un huissier / commissaire de justice |
| **Date** | 06/07/2026 |
| **Source** | [https://commissaire-justice.fr/blog-juridique/jeux-concours-en-ligne-pourquoi-faire-appel-a-un-commissaire-de-justice](https://commissaire-justice.fr/blog-juridique/jeux-concours-en-ligne-pourquoi-faire-appel-a-un-commissaire-de-justice) |
| **Information clé** | Depuis 2014, le dépôt du règlement chez un commissaire de justice n'est plus obligatoire légalement, mais reste fortement recommandé : il donne une valeur probatoire incontestable en cas de litige et garantit l'équité entre participants. Le règlement doit néanmoins être rédigé et accessible dans tous les cas (article L.121-38 Code conso). |
| **Impact projet** | Le projet prévoit déjà un dépôt auprès de Maître Arnaud Rick (huissier) — démarche non obligatoire mais pertinente vu le volume (500 000 codes) et la répartition différenciée des gains (60/20/10/6/4 %). |
| **Décision / action** | Maintenir le dépôt chez l'huissier au planning, transmettre le règlement finalisé avant l'ouverture, conserver l'accusé de réception/procès-verbal comme preuve jury. |
| **Responsable** | Chef de projet |
| **Échéance** | Avant l'ouverture officielle du concours |

---

## Fiche 6 — Transparence et loyauté envers le participant

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Obligation de transparence sur l'aléa et les gains (jurisprudence loterie publicitaire) |
| **Date** | 06/07/2026 |
| **Source** | [https://www.solvoxia-avocats.com/fiches-juridiques/quelles-regles-pour-organiser-un-jeu-concours-en-ligne/](https://www.solvoxia-avocats.com/fiches-juridiques/quelles-regles-pour-organiser-un-jeu-concours-en-ligne/) |
| **Information clé** | La jurisprudence sanctionne les annonces de gain ambiguës (ex : "vous êtes le grand gagnant") sans mise en évidence claire de l'aléa/des conditions dès la première lecture : cela peut créer un quasi-contrat obligeant à délivrer le gain réclamé. Le règlement doit aussi encadrer la durée de conservation des données personnelles des participants. |
| **Impact projet** | Les écrans de résultat (`/participer`, historique des gains) doivent afficher sans ambiguïté le statut du code et les conditions d'obtention du lot, et le règlement doit préciser une durée de conservation limitée des données participants. |
| **Décision / action** | Revoir les maquettes/wireframes de l'écran de résultat avec le lead UX pour garantir un message univoque ; ajouter une clause de durée de conservation dans le règlement et la politique de confidentialité. |
| **Responsable** | UX/UI + référent conformité |
| **Échéance** | Avant validation des wireframes (section G.5) |

---

## Mise à jour — Concours "100% gagnant" avec obligation d'achat en boutique

**Contexte précisé du projet :** le concours Thé Tip Top est un dispositif **100% gagnant**, conditionné à un **achat en boutique** (produits thé/infusions). Les fiches ci-dessous précisent le régime juridique applicable à ce mécanisme spécifique.

## Fiche 7 — Légalité des jeux-concours avec obligation d'achat

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Légalisation des loteries publicitaires avec obligation d'achat depuis le 17 mai 2011 |
| **Date** | 06/07/2026 |
| **Source** | [https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html](https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html) |
| **Information clé** | Depuis le 17 mai 2011, les jeux-concours avec obligation d'achat sont autorisés en France (auparavant interdits). Le jeu doit être conditionné à un achat de produit ou service réel — il reste interdit de faire payer la participation elle-même (ce qui relèverait des jeux d'argent réservés). Une preuve d'achat peut être exigée pour valider la participation. |
| **Impact projet** | Le mécanisme "achat en boutique = code ticket remis" est légal, à condition que la participation reste liée à un achat réel de produit thé/infusion, et non à un paiement direct pour "jouer". |
| **Décision / action** | S'assurer que le code ticket est bien remis en caisse suite à un achat de produit, jamais vendu séparément ; documenter ce parcours dans le règlement. |
| **Responsable** | Chef de projet / référent boutique |
| **Échéance** | Avant la génération des 500 000 codes |

---

## Fiche 8 — Vigilance sur la mécanique "100% gagnant"

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Risque de requalification en pratique commerciale déloyale/agressive pour les loteries "100% gagnant" |
| **Date** | 06/07/2026 |
| **Source** | [https://www.lemondedudroit.fr/decryptages/5176-des-loteries-q100-gagnantq-si-elles-sont-100-gratuites.html](https://www.lemondedudroit.fr/decryptages/5176-des-loteries-q100-gagnantq-si-elles-sont-100-gratuites.html) et [https://livv.eu/glossaire/loteries-publicitaires](https://livv.eu/glossaire/loteries-publicitaires) |
| **Information clé** | La CJUE (arrêt du 18 octobre 2012) qualifie de pratique commerciale agressive le fait d'annoncer à un consommateur qu'il a gagné alors qu'il découvre ensuite devoir engager une dépense pour obtenir son gain. Le risque vise le cas où la condition est cachée ou révélée après l'annonce du gain. Un mécanisme où l'achat est annoncé clairement avant la participation reste licite (article L.121-20 Code conso), à condition que les gains restent proportionnés. |
| **Impact projet** | Le site et la communication doivent annoncer la condition d'achat en boutique avant toute mention de gain, sur tous les supports (site, réseaux sociaux, PLV boutique). La répartition des lots (60/20/10/6/4 %) doit rester lisible et proportionnée. |
| **Décision / action** | Vérifier avec le client/juriste que la mention "achat obligatoire en boutique pour participer" figure clairement sur toutes les communications avant toute mention de gain. |
| **Responsable** | Référent conformité / marketing |
| **Échéance** | Avant lancement de la campagne de communication (section D) |

---

## Fiche 9 — Distinction entre code de participation et preuve d'achat

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Séparation entre bulletin de participation et document d'achat/bancaire |
| **Date** | 06/07/2026 |
| **Source** | [https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html](https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html) |
| **Information clé** | Le bulletin de participation (ici : le code ticket) doit rester distinct de tout bon de commande, ticket de caisse ou document bancaire, afin de ne pas créer de confusion entre l'acte d'achat et l'acte de participation. |
| **Impact projet** | Le code ticket remis en boutique doit être un support séparé (carte, flyer, impression dédiée) du ticket de caisse, même s'il est délivré au moment de l'achat. |
| **Décision / action** | Concevoir un support physique dédié au code ticket, non confondu avec le ticket de caisse ; le préciser dans le cahier des charges boutique et dans le règlement. |
| **Responsable** | Référent opérations boutique / UX |
| **Échéance** | Avant validation du parcours "remise en boutique" (use case 2) |

---

## Fiche 10 — Information consommateur sur les produits alimentaires (lots thé/infusions)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Réglementation d'information sur les denrées alimentaires appliquée aux lots offerts |
| **Date** | 06/07/2026 |
| **Source** | [https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32011R1169](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32011R1169) (Règlement UE n°1169/2011 dit INCO) |
| **Information clé** | Les lots remis dans le cadre du concours étant des produits alimentaires (thé/infusions), leur présentation sur le site (visuels, descriptifs, allégations) doit respecter les règles d'information du consommateur : dénomination correcte, origine si mise en avant, absence d'allégations de santé non autorisées. |
| **Impact projet** | Les fiches produits/lots affichées sur la page concours ne doivent pas comporter d'allégations santé non validées (ex : "bon pour la santé", "détox") sans base réglementaire. |
| **Décision / action** | Faire relire les textes de présentation des lots par le référent marketing client avant publication, en excluant toute allégation de santé non certifiée. |
| **Responsable** | Référent marketing client / rédaction |
| **Échéance** | Avant publication de la page d'accueil concours |

---

## Synthèse actionnable globale

- **Sécurité/traçabilité** : renforcer l'authentification et journaliser les actions sensibles côté API (fiche 1).
- **Cookies** : bannière conforme CNIL, CMP à intégrer avant mise en ligne (fiche 2).
- **Règlement du concours** : rédaction, dépôt chez l'huissier et accessibilité en ligne à sécuriser en priorité haute (fiches 3 et 5).
- **Légalité de l'obligation d'achat** : mécanisme autorisé depuis 2011, à condition que la participation ne soit jamais payante en elle-même (fiche 7).
- **Transparence en amont** : la condition d'achat doit être annoncée avant toute mention de gain, sur tous les supports (fiches 6 et 8).
- **Séparation des supports** : le code ticket ne doit jamais être confondu avec le ticket de caisse (fiche 9).
- **Proportionnalité des gains** : la répartition 60/20/10/6/4 % doit rester lisible pour écarter tout risque de requalification (fiche 8).
- **Produits alimentaires** : les visuels et descriptifs des lots doivent respecter les règles d'information du consommateur (fiche 10).

---

## Sources de référence (toutes fiches)

- CNIL — Règles cookies et traceurs : [https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles)
- CNIL — Refuser les cookies aussi simple que l'accepter : [https://cnil.fr/fr/refuser-les-cookies-doit-etre-aussi-simple-quaccepter-mise-en-conformite-de-tous-les-organismes](https://cnil.fr/fr/refuser-les-cookies-doit-etre-aussi-simple-quaccepter-mise-en-conformite-de-tous-les-organismes)
- Les Échos Solutions — Nouveautés RGPD 2026 : [https://solutions.lesechos.fr/juridique/loi-conformite/nouveautes-rgpd-2026-comment-adapter-sa-conformite-des-maintenant/](https://solutions.lesechos.fr/juridique/loi-conformite/nouveautes-rgpd-2026-comment-adapter-sa-conformite-des-maintenant/)
- Legalstart — Jeu concours : règlement et procédure : [https://www.legalstart.fr/fiches-pratiques/astuces-entrepreneurs/jeu-concours/](https://www.legalstart.fr/fiches-pratiques/astuces-entrepreneurs/jeu-concours/)
- Two Birds — Jeux-concours en ligne, vers un cadre juridique plus clair : [https://www.twobirds.com/fr/insights/2025/france/jeuxconcours-en-ligne--vers-un-cadre-juridique-plus-clair](https://www.twobirds.com/fr/insights/2025/france/jeuxconcours-en-ligne--vers-un-cadre-juridique-plus-clair)
- Commissaire de Justice — Pourquoi faire appel à un commissaire de justice pour un jeu-concours : [https://commissaire-justice.fr/blog-juridique/jeux-concours-en-ligne-pourquoi-faire-appel-a-un-commissaire-de-justice](https://commissaire-justice.fr/blog-juridique/jeux-concours-en-ligne-pourquoi-faire-appel-a-un-commissaire-de-justice)
- Solvoxia Avocats — Quelles règles pour organiser un jeu-concours en ligne : [https://www.solvoxia-avocats.com/fiches-juridiques/quelles-regles-pour-organiser-un-jeu-concours-en-ligne/](https://www.solvoxia-avocats.com/fiches-juridiques/quelles-regles-pour-organiser-un-jeu-concours-en-ligne/)
- Règlement de Jeu — Jeu ou concours avec obligation d'achat : [https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html](https://www.reglementdejeu.com/jeux-concours/jeu-obligation-achat.html)
- Le Monde du Droit — Des loteries "100% gagnant" si elles sont 100% gratuites : [https://www.lemondedudroit.fr/decryptages/5176-des-loteries-q100-gagnantq-si-elles-sont-100-gratuites.html](https://www.lemondedudroit.fr/decryptages/5176-des-loteries-q100-gagnantq-si-elles-sont-100-gratuites.html)
- LIVV — Glossaire loteries publicitaires : [https://livv.eu/glossaire/loteries-publicitaires](https://livv.eu/glossaire/loteries-publicitaires)
- EUR-Lex — Règlement (UE) n°1169/2011 (INCO) : [https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32011R1169](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32011R1169)
