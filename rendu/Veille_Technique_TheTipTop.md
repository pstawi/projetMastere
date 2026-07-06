# Veille Technique — Site Jeu-Concours Thé Tip Top

**Projet :** Thé Tip Top — Objectif n°2 (site jeu-concours)
**Type de veille :** Veille technique (API/webapp, sécurité, accessibilité, performance)
**Stack retenue :** API back en Symfony (API Platform) + Front en React
**Fréquence :** Hebdomadaire (synthèse consolidée en fin de sprint)
**Diffusion :** Équipe projet + référent client
**Dernière mise à jour :** 06/07/2026

---

## Objectifs de cette veille

- Sécuriser et fiabiliser l'architecture API Symfony / front React retenue pour le projet.
- Suivre les bonnes pratiques d'authentification, de performance et d'accessibilité applicables aux deux couches.
- Anticiper les risques techniques propres à la volumétrie du projet (500 000 codes, pics de trafic).

---

## Fiche 1 — API Platform sur Symfony 7 : bonnes pratiques 2026

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Bonnes pratiques de construction d'API avec Symfony 7 et API Platform |
| **Date** | 06/07/2026 |
| **Source** | [https://sharpskill.dev/fr/blog/symfony/symfony-7-api-platform-bonnes-pratiques](https://sharpskill.dev/fr/blog/symfony/symfony-7-api-platform-bonnes-pratiques) |
| **Information clé** | API Platform sur Symfony 7 permet de générer rapidement des ressources API avec des groupes de sérialisation dédiés (`normalization_context`/`denormalization_context`), une documentation OpenAPI automatique, et une gestion fine des filtres/pagination sur les collections. |
| **Impact projet** | Utiliser API Platform accélère le développement des endpoints (codes tickets, gains, participations) tout en générant une documentation Swagger exploitable comme preuve technique pour le jury. |
| **Décision / action** | Adopter API Platform comme couche d'exposition des ressources métier (`TicketCode`, `Prize`, `Participation`), avec des groupes de sérialisation distincts pour les vues participant/admin/boutique. |
| **Responsable** | Lead technique |
| **Échéance** | Avant le début du développement de l'API (lot 4 du WBS) |

---

## Fiche 2 — Authentification API sécurisée avec JWT (LexikJWTAuthenticationBundle)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Authentification stateless par JWT sur API Symfony |
| **Date** | 06/07/2026 |
| **Source** | [https://api-platform.com/docs/symfony/jwt/](https://api-platform.com/docs/symfony/jwt/) |
| **Information clé** | Le bundle LexikJWTAuthenticationBundle reste la référence pour sécuriser une API Symfony de façon stateless : génération d'un couple de clés RSA, firewall dédié `^/api` avec `stateless: true`, endpoint `/api/login_check` retournant un token signé contenant les rôles utilisateur. |
| **Impact projet** | Ce mécanisme convient parfaitement à la logique multi-acteurs du projet (participant, admin, employé boutique) : chaque rôle peut être encodé dans le JWT pour restreindre l'accès aux endpoints sensibles (validation code, remise de lot). |
| **Décision / action** | Installer `lexik/jwt-authentication-bundle`, générer des clés distinctes en environnement de démo/production, définir un `access_control` par rôle (`ROLE_PARTICIPANT`, `ROLE_ADMIN`, `ROLE_BOUTIQUE`). |
| **Responsable** | Lead technique |
| **Échéance** | Avant le développement des endpoints d'authentification |

---

## Fiche 3 — Sécurisation des endpoints sensibles (rate limiting et validation)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Protection contre les abus sur les endpoints de validation de code (brute force, scripts automatisés) |
| **Date** | 06/07/2026 |
| **Source** | [https://symfony.com/doc/current/the-fast-track/en/26-api.html](https://symfony.com/doc/current/the-fast-track/en/26-api.html) |
| **Information clé** | Symfony propose un composant `RateLimiter` natif permettant de limiter le nombre de requêtes par IP/utilisateur sur une fenêtre de temps donnée, utile pour empêcher le brute force sur l'endpoint de soumission de code ticket. |
| **Impact projet** | L'endpoint `/api/participer` (soumission de code) est le plus exposé du projet : sans limitation, un script pourrait tester massivement des combinaisons de codes parmi les 500 000 générés. |
| **Décision / action** | Configurer le composant `RateLimiter` de Symfony sur l'endpoint de soumission de code (ex : 5 tentatives / minute / IP), avec réponse HTTP 429 en cas de dépassement, et logguer les tentatives suspectes dans `AuditLog`. |
| **Responsable** | Lead technique |
| **Échéance** | Avant la mise en recette (lot 6 du WBS) |

---

## Fiche 4 — React : gestion d'état et architecture de composants (2026)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Bonnes pratiques d'architecture front React pour une webapp transactionnelle |
| **Date** | 06/07/2026 |
| **Source** | À enrichir avec la documentation officielle React (react.dev) — veille à poursuivre sur les Server Components et la gestion d'état (Context API vs bibliothèques dédiées) |
| **Information clé** | Pour une application avec des parcours courts et transactionnels (inscription, saisie de code, historique), une architecture à base de composants réutilisables (formulaires, boutons, badges de statut) et une gestion d'état légère (Context API ou bibliothèque dédiée) suffit sans complexifier inutilement le projet. |
| **Impact projet** | Le front React du site concours doit prioriser la simplicité et la performance mobile plutôt qu'une architecture d'état complexe, cohérent avec les conclusions du benchmark (priorité UX : réduire les étapes du parcours). |
| **Décision / action** | Documenter dans le cahier technique le choix de gestion d'état retenu (Context API en priorité, sauf besoin avéré d'une librairie plus lourde) et la liste des composants réutilisables prévus (boutons, formulaires, statuts). |
| **Responsable** | Développeur front / Lead technique |
| **Échéance** | Avant le développement de la webapp (lot 5 du WBS) |

---

## Fiche 5 — Accessibilité et performance (RGAA/WCAG, Lighthouse)

| Champ | Contenu |
| --- | --- |
| **Sujet de veille** | Outils et référentiels de contrôle accessibilité/performance à appliquer sur l'API et le front |
| **Date** | 06/07/2026 |
| **Source** | Outils déjà identifiés dans le cahier technique : Lighthouse, WAVE, validateur HTML/CSS (section F.2 du cahier client) |
| **Information clé** | Le niveau WCAG AA est visé sur les écrans clés du parcours (accueil, inscription, saisie de code, historique des gains). Lighthouse permet d'auditer simultanément performance, accessibilité, bonnes pratiques et SEO sur chaque page React générée. |
| **Impact projet** | Chaque écran critique du front doit être audité avec Lighthouse avant recette, avec captures d'écran conservées comme preuve jury (RGAA/accessibilité étant une exigence explicite du référentiel RNCP). |
| **Décision / action** | Intégrer un contrôle Lighthouse dans le pipeline CI (ou a minima en local avant chaque livraison de sprint), avec seuil minimum à définir (ex : score accessibilité > 90). |
| **Responsable** | QA / accessibilité |
| **Échéance** | Avant chaque fin de sprint (recette continue) |

---

## Synthèse actionnable

- **Sécurité API** : JWT stateless avec rôles distincts (participant/admin/boutique) via LexikJWTAuthenticationBundle, couplé à un rate limiting strict sur l'endpoint de soumission de code.
- **Architecture API** : API Platform pour accélérer le développement des ressources métier et générer une documentation OpenAPI exploitable comme preuve.
- **Front React** : privilégier une architecture simple (Context API, composants réutilisables) cohérente avec l'objectif UX de parcours court.
- **Qualité continue** : audits Lighthouse réguliers sur les écrans critiques pour garantir le niveau WCAG AA visé et disposer de preuves jury.
- **Anti-abus** : traçabilité des tentatives suspectes dans l'`AuditLog` déjà prévu au modèle de données.

---

## Sources de référence

- SharpSkill — Symfony 7 API Platform, bonnes pratiques 2026 : [https://sharpskill.dev/fr/blog/symfony/symfony-7-api-platform-bonnes-pratiques](https://sharpskill.dev/fr/blog/symfony/symfony-7-api-platform-bonnes-pratiques)
- API Platform — JWT Authentication with Symfony : [https://api-platform.com/docs/symfony/jwt/](https://api-platform.com/docs/symfony/jwt/)
- Symfony Docs — Exposing an API with API Platform : [https://symfony.com/doc/current/the-fast-track/en/26-api.html](https://symfony.com/doc/current/the-fast-track/en/26-api.html)
- dev.to — Securing API With JWT In Symfony : [https://dev.to/jszutkowski/securing-api-with-jwt-in-symfony-36dk](https://dev.to/jszutkowski/securing-api-with-jwt-in-symfony-36dk)
- Cahier client Thé Tip Top — section F.2 Outils projet (Lighthouse, WAVE, validateur HTML/CSS)
