# Veille Concurrentielle — Site Jeu-Concours Thé Tip Top

**Projet :** Thé Tip Top — Objectif n°2 (site jeu-concours)
**Type de veille :** Veille concurrentielle (sites de thé, mécaniques de concours, gamification)
**Fréquence :** Hebdomadaire (synthèse consolidée en fin de sprint)
**Diffusion :** Équipe projet + référent client
**Dernière mise à jour :** 06/07/2026

---

## Objectifs de cette veille

- Étudier les mécaniques de concours utilisées par des marques de thé/infusions et de boissons comparables.
- Identifier les leviers de gamification les plus efficaces pour un dispositif "achat + participation".
- Comparer les parcours de participation existants pour en tirer des recommandations UX pour Thé Tip Top.

---

## Fiche 1 — Kusmi Tea : concours thé avec dotation récurrente + grand prix

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Mécanique de concours d'une marque de thé premium (dotation hebdomadaire + tirage au sort final) |
| **Date** | 06/07/2026 |
| **Source** | [http://www.my-cup-of-tea.fr/concours-the/](http://www.my-cup-of-tea.fr/concours-the/) |
| **Information clé** | Kusmi Tea a organisé un concours combinant une dotation récurrente (du thé et des accessoires chaque semaine) avec un grand prix final tiré au sort (voyage), ce qui entretient l'engagement sur toute la durée du concours plutôt qu'un tirage unique en fin de période. |
| **Impact projet** | Le concours Thé Tip Top est structuré en 100% gagnant (petits lots garantis) avec probablement un ou plusieurs gros lots par tirage complémentaire (60/20/10/6/4 %) — ce modèle hybride est directement comparable à celui de Kusmi Tea, qui valide la pertinence de cette structure pour maintenir l'intérêt. |
| **Décision / action** | Mettre en avant sur le site la distinction claire entre "lot garanti" et "gros lot à tirage" pour créer un effet d'anticipation similaire à celui observé chez Kusmi Tea. |
| **Responsable** | Référent marketing / UX |
| **Échéance** | Avant validation du parcours participant (use case 1) |

---

## Fiche 2 — Camellia Sinensis : concours thématique et interactif ("thé mystère")

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Concours thématique combinant énigme produit et participation en ligne |
| **Date** | 06/07/2026 |
| **Source** | [https://camellia-sinensis.com/fr/concours/concours-the-mystere-automne-2025](https://camellia-sinensis.com/fr/concours/concours-the-mystere-automne-2025) |
| **Information clé** | Camellia Sinensis propose un concours où le client reçoit un échantillon de "thé mystère" et doit deviner son identité pour participer au tirage, créant une interaction ludique directement liée au produit plutôt qu'un simple tirage au sort passif. |
| **Impact projet** | Ce type de mécanique interactive (deviner, quiz, énigme) pourrait enrichir le concours Thé Tip Top au-delà de la simple saisie de code, en ajoutant une couche de gamification légère sans complexifier le parcours technique. |
| **Décision / action** | Étudier avec le client la possibilité d'ajouter un mini-quiz optionnel sur le thé (facultatif, sans impact sur le gain) pour renforcer l'univers de marque sans alourdir le parcours principal. |
| **Responsable** | Référent marketing / UX |
| **Échéance** | Phase d'itération post-MVP (backlog optionnel) |

---

## Fiche 3 — Mont Roucous : gamification par roue de la chance liée à un achat (cas analogue boisson)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Étude de cas d'un jeu-concours gamifié avec roue de la chance, réservé aux acheteurs d'un produit |
| **Date** | 06/07/2026 |
| **Source** | [https://drimify.com/fr/success-stories/29k-participations-trimestre-mont-roucous-booste-ventes-grace-marketing-gamifie/](https://drimify.com/fr/success-stories/29k-participations-trimestre-mont-roucous-booste-ventes-grace-marketing-gamifie/) |
| **Information clé** | Mont Roucous (eau minérale) a mis en place une roue de la chance accessible uniquement aux clients ayant acheté un pack éligible, avec saisie d'un numéro de lot pour participer. Résultat : plus de 29 000 participations par trimestre. Point clé UX : le formulaire de participation initial est volontairement court (date + numéro de lot), et un second formulaire plus détaillé (coordonnées de livraison) n'est demandé qu'aux gagnants, pour ne pas décourager la participation. |
| **Impact projet** | Ce cas est le plus proche du mécanisme Thé Tip Top (achat obligatoire + code/numéro à saisir + gain immédiat). La bonne pratique du formulaire en deux temps est directement applicable. |
| **Décision / action** | Reprendre ce principe : un formulaire de participation minimal (code ticket uniquement) et ne demander les coordonnées complètes qu'après confirmation du gain, afin de maximiser le taux de complétion. |
| **Responsable** | UX/UI + lead technique |
| **Échéance** | Avant validation des wireframes (section G.5) |

---

## Fiche 4 — Gamification dans l'industrie alimentaire : chiffres et leviers

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Impact mesuré de la gamification sur l'engagement des consommateurs dans l'agroalimentaire |
| **Date** | 06/07/2026 |
| **Source** | [https://baanwanta.com/engagement-des-consommateurs-et-strategies-innovantes-dans-l-industrie-alimentaire/](https://baanwanta.com/engagement-des-consommateurs-et-strategies-innovantes-dans-l-industrie-alimentaire/) |
| **Information clé** | Selon les études citées, 72% des consommateurs participent plus activement aux campagnes intégrant un aspect ludique (défis, points, badges). La gamification transforme une simple transaction en expérience mémorable et améliore la richesse des données collectées, mais nécessite une transparence forte sur les conditions de participation et la protection des données personnelles. |
| **Impact projet** | Le concours Thé Tip Top peut renforcer son taux d'engagement en ajoutant des éléments ludiques légers (barre de progression, badge "participant", visuel de déballage du lot) sans compromettre la simplicité du parcours ni la transparence légale déjà identifiée en veille juridique. |
| **Décision / action** | Prévoir dans les wireframes un élément visuel gratifiant lors de la révélation du gain (animation de déballage, confettis) pour renforcer l'aspect mémorable de l'expérience. |
| **Responsable** | UX/UI |
| **Échéance** | Avant validation des maquettes (section G.5) |

---

## Fiche 5 — Panorama des plateformes de gamification pour jeux-concours

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Solutions existantes de gamification marketing (roue de la chance, quiz, instant gagnant) utilisées par les marques |
| **Date** | 06/07/2026 |
| **Source** | [https://www.blogdumoderateur.com/tools/marketing-digital/jeux-concours/](https://www.blogdumoderateur.com/tools/marketing-digital/jeux-concours/) |
| **Information clé** | Le marché propose de nombreux outils clé en main (type Drimify, Kontest) pour créer des mécaniques de jeu (roue de la chance, quiz, instant gagnant, grattage) sans développement complet. Ces solutions sont pertinentes pour des marques qui n'ont pas de développement interne, mais moins adaptées à un projet avec une API et un front sur-mesure comme Thé Tip Top. |
| **Impact projet** | Le projet ayant une stack dédiée (Symfony/React), ces outils ne seront pas utilisés directement, mais leurs mécaniques (roue, grattage, instant gagnant) restent une source d'inspiration UX à reproduire nativement dans le développement du front React. |
| **Décision / action** | S'inspirer des mécaniques visuelles de type "grattage" ou "instant gagnant" pour l'écran de révélation du gain, à développer nativement en React plutôt que via un outil tiers. |
| **Responsable** | UX/UI + développeur front |
| **Échéance** | Avant développement de l'écran de résultat |

---

## Synthèse actionnable

- **Structure hybride de gains** : lots garantis + gros lot à tirage complémentaire, validée par le cas Kusmi Tea, cohérente avec la répartition 60/20/10/6/4 %.
- **Formulaire en deux temps** : saisie minimale du code pour participer, coordonnées complètes demandées uniquement aux gagnants (cas Mont Roucous) — bonne pratique directement applicable.
- **Gamification légère** : animation de révélation du gain (déballage, confettis) pour renforcer l'expérience mémorable, sans alourdir le parcours technique.
- **Interaction produit optionnelle** : un mini-quiz ou une énigme liée au thé (cas Camellia Sinensis) pourrait enrichir l'expérience en itération post-MVP.
- **Développement natif** : s'inspirer des mécaniques des plateformes de gamification (roue, grattage) mais les recréer nativement en React plutôt que d'intégrer un outil tiers.

---

## Sources de référence

- My Cup of Tea — Concours thé (Kusmi Tea) : [http://www.my-cup-of-tea.fr/concours-the/](http://www.my-cup-of-tea.fr/concours-the/)
- Camellia Sinensis — Concours thé mystère : [https://camellia-sinensis.com/fr/concours/concours-the-mystere-automne-2025](https://camellia-sinensis.com/fr/concours/concours-the-mystere-automne-2025)
- Drimify — Étude de cas Mont Roucous, marketing gamifié : [https://drimify.com/fr/success-stories/29k-participations-trimestre-mont-roucous-booste-ventes-grace-marketing-gamifie/](https://drimify.com/fr/success-stories/29k-participations-trimestre-mont-roucous-booste-ventes-grace-marketing-gamifie/)
- Baanwanta — Engagement consommateurs et gamification alimentaire : [https://baanwanta.com/engagement-des-consommateurs-et-strategies-innovantes-dans-l-industrie-alimentaire/](https://baanwanta.com/engagement-des-consommateurs-et-strategies-innovantes-dans-l-industrie-alimentaire/)
- Blog du Modérateur — 13 outils pour créer des jeux marketing : [https://www.blogdumoderateur.com/tools/marketing-digital/jeux-concours/](https://www.blogdumoderateur.com/tools/marketing-digital/jeux-concours/)
