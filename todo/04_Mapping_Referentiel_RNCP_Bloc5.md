# Mapping avec le référentiel officiel RNCP - Bloc 5 / Épreuve n°7

Source : `Referentiel_RNCP_ExpertStrategieTransformationDigitale_extrait.txt` (PDF officiel IEF2i - RNCP Expert en stratégie et transformation digitale, Niveau 7).

## Pourquoi ce document

Le référentiel officiel définit 6 blocs de compétences. La validation de la certification exige les **3 blocs communs (1, 2, 3)** + **1 bloc optionnel au choix parmi 3 (4, 5, 6)**. Le projet Furious Ducks (workflow, Objectif 1) + Thé Tip Top (site jeu-concours, Objectif 2) est positionné comme preuve du **Bloc 5 (optionnel n°2) : « Piloter le développement technique d'une solution digitale ou la refonte d'une plateforme e-business »**, évalué par l'**Épreuve n°7 (compétences C29 à C35)**.

Ce tableau croise chaque compétence exigée avec l'état réel de nos livrables (`rendu/` pour l'Objectif 1, `Objectif2_ABC_Cahier_Client_TheTipTop.md` pour l'Objectif 2) afin de vérifier qu'aucun critère officiel n'est oublié.

⚠️ Les Blocs 1, 2 et 3 (communs, obligatoires) ne sont **pas couverts par ce mapping** : ils portent sur la stratégie marketing globale, le brand/UX et le management d'équipe au sens large, et relèvent probablement d'autres preuves/évaluations que ce seul projet. À vérifier séparément avec l'école si ce projet doit aussi servir de preuve pour ces blocs communs.

## Épreuve n°7 - Production attendue

D'après le référentiel, la mise en situation professionnelle doit présenter :

| # | Élément attendu | Où il doit se trouver | Statut |
| --- | --- | --- | --- |
| 1 | Le cahier des charges du projet | `Objectif2_ABC_Cahier_Client_TheTipTop.md` (sections A à E) | [x] Rédigé (à finaliser, cf. `02_Objectif2_Reste_A_Faire.md`) |
| 2 | Les spécifications techniques | Section F du cahier Objectif 2 | [x] Rédigées (stack à valider définitivement) |
| 3 | L'ensemble des tâches à accomplir | Section I (MoSCoW/Eisenhower/planning) | [ ] Méthode posée, contenu à compléter |
| 4 | Le pilotage de l'intégration des textes et images | — | [ ] Non traité explicitement (à ajouter : qui valide le contenu éditorial/visuel avant mise en ligne, avec quelles règles RGAA) |
| 5 | La conception de la solution digitale | Section G (UX/UI) + développement effectif | [ ] Maquettes/wireframes non produits, développement non commencé |
| 6 | La sécurisation des bases de données | Section F (sécurité), E.5 (MLD) | [~] Principes posés, pas de preuve technique concrète |
| 7 | Soutenance orale devant jury | — | [ ] À préparer (`Objectif2_Soutenance_Condensee.md` est une base) |

## Détail par compétence (C29 à C35)

| Compétence | Intitulé résumé | Critères d'évaluation officiels | État actuel | Gap / action à prévoir |
| --- | --- | --- | --- | --- |
| C29 | Rédiger le cahier des charges (objectifs, moyens, contraintes qualité/coût/délai/RSE) | Contraintes client respectées ; cahier exhaustif ; **dimension RSE prise en compte** ; résultats présentés de façon précise et structurée | Cahier des charges existant et structuré, mais la **dimension RSE (éco-conception, Green IT) n'est posée que comme critère d'audit concurrent**, pas comme exigence appliquée au propre site Thé Tip Top | Ajouter un paragraphe RSE/éco-conception explicite dans le cahier des charges Thé Tip Top (ex. sobriété numérique, poids des pages, hébergement) |
| C30 | Traduire en spécifications techniques | Spécifications rédigées et argumentées ; ensemble des tâches défini | Section F présente une stack proposée | Argumenter les choix techniques (pourquoi cette stack) si pas déjà fait ; lister exhaustivement les tâches (lien avec section I) |
| C31 | Définir les contenus de chaque page (hiérarchisation, accessibilité) | Besoins client répertoriés et hiérarchisés ; contenus définis respectant l'accessibilité | Arborescence webapp posée (E.2) | Produire les zonings/wireframes avec le contenu par page (déjà identifié comme manquant dans `02_Objectif2_Reste_A_Faire.md` section 4) |
| C32 | Piloter l'intégration des textes et images | Typographie définie ; contenu conforme **RGAA** ; effets graphiques contrôlés ; cohérence avec le cahier des charges vérifiée | Non traité | Ajouter une checklist RGAA explicite (pas seulement "WCAG AA" mentionné pour les contrastes) + qui valide l'intégration |
| C33 | Piloter la conception (maquette, navigation, contenus) | Maquette graphique analysée ; **schéma de navigation cohérent et conforme aux règles d'ergonomie W3C** ; typographie/effets graphiques intégrés | Arborescence posée, mais pas de schéma de navigation formalisé ni de maquettes | Produire un schéma de navigation (sitemap détaillé) + wireframes/maquettes (déjà en todo section 4 de l'Objectif 2) |
| C34 | Développer une solution digitale sécurisée | **Accès aux bases de données en langage de programmation contrôlé** ; données identifiées ; **méthodes de modélisation exposées** | MLD simplifié posé (E.5), principes de sécurité listés (F) | Développement effectif non commencé ; à défaut de dev complet, produire au minimum le schéma de contrôle d'accès BDD et exposer la méthode de modélisation utilisée (Merise, UML, etc.) |
| C35 | Améliorer une solution digitale (cycle de vie, nouvelles exigences réglementaires) | Une ou plusieurs évolutions fonctionnelles proposées pour répondre à de nouveaux besoins/réglementations | Une ligne "maintenance évolutive post-concours" existe (fin du cahier) | Étoffer en un vrai paragraphe : quelles évolutions envisagées (V2), quelle veille réglementaire (RGPD, RGAA) déclenche une mise à jour |

## Recommandation

Les todo déjà identifiés dans `02_Objectif2_Reste_A_Faire.md` (sections 3, 4, 7) couvrent la majorité de ces manques (wireframes, maquettes, diagrammes, développement effectif). Les points **spécifiquement révélés par le référentiel officiel** et à ajouter aux todo existants sont :

1. Paragraphe RSE/éco-conception explicite dans le cahier des charges (C29).
2. Checklist RGAA (pas seulement WCAG) pour l'intégration des contenus (C32).
3. Schéma de navigation formalisé, distinct de l'arborescence (C33).
4. Exposer la méthode de modélisation des données utilisée, en plus du MLD (C34).
5. Paragraphe structuré sur l'amélioration continue / cycle de vie post-lancement (C35).
