# Parcours français — sommaire

Les 99 fiches de `docs/fr`, regroupées par thème. Plusieurs séries partagent les mêmes numéros (par exemple `01-cadre-recherche` et `01-trace-etat`) : ce sommaire sert de point d'entrée unique. Chaque fiche est une lecture statique ; aucun audit n'est revendiqué.

## Méthode de recherche et traçabilité des contributions

Cadre, lecture des sources et critères publics d'un historique de commits (voir `prototype/commit_classifier.py`).

- [Cadre de recherche](01-cadre-recherche.md)
- [Lecture source-grounded](02-lecture-source.md)
- [Classification des commits](03-classification-commits.md)
- [Fixtures publiques](04-fixtures-publics.md)
- [Reproductibilité](05-reproductibilite.md)
- [Traçabilité par domaine](06-traceabilite-domaines.md)
- [Attribution d’auteur](15-commit-author.md)
- [Visibilité publique](16-public-visibility.md)
- [Intégrité de branche](17-branch-integrity.md)

## STARK : vue d'ensemble

Notes de synthèse sur les briques d'un système STARK et d'un rollup.

- [Trace STARK](07-stark-trace.md)
- [Contraintes STARK](08-stark-constraints.md)
- [Engagement de trace](09-trace-commitment.md)
- [Pliage FRI](10-fri-fold.md)
- [Vérificateur STARK](11-proof-verifier.md)
- [Liaison au transcript](12-transcript-binding.md)
- [Authentification Merkle](13-merkle-authentication.md)
- [Preuves récursives](14-recursive-proofs.md)
- [Disponibilité des données rollup](18-data-availability.md)
- [Frontières d’un rollup](19-rollup-boundaries.md)

## STARK pas à pas avec les prototypes

Trace, contraintes, engagement, FRI, vérification et transcript, chapitre par chapitre.

- [Trace et état](01-trace-etat.md)
- [Colonnes de trace](02-colonnes-trace.md)
- [Encodage des valeurs](03-encodage-valeurs.md)
- [Relations de transition](04-transitions.md)
- [Contraintes de frontière](05-frontieres.md)
- [Composition des contraintes](06-composition.md)
- [Degré des contraintes](07-degre.md)
- [Engagement avant ouverture](08-engagement.md)
- [Racine Merkle](09-racine-merkle.md)
- [Chemins d’authentification](10-chemins.md)
- [Défi FRI](11-defi-fri.md)
- [Opération de pliage](12-pliage.md)
- [Transcript du FRI](13-transcript-fri.md)
- [Requêtes de vérification](14-requetes.md)
- [Ouvertures cohérentes](15-ouvertures.md)
- [Vérification globale](16-verification-globale.md)
- [Binding du transcript](17-binding.md)
- [Domaines de hachage](18-domaines-hachage.md)
- [Rejeu et fraîcheur](19-rejeu-preuve.md)

## FHE

Budget de bruit BFV/BGV/CKKS (voir `prototype/fhe_noise_budget.py`).

- [Modèle FHE](20-fhe-modele.md)
- [Bruit initial](21-bruit-initial.md)
- [Coût multiplication](22-multiplication.md)
- [Profondeur multiplicative](23-profondeur.md)
- [Rescaling CKKS](24-rescaling.md)
- [Paramètres FHE](25-parametres.md)
- [Budget de bruit](26-noise-budget.md)
- [Moment du déchiffrement](27-dechiffrement.md)
- [Confidentialité des entrées](28-confidentialite.md)
- [Sorties chiffrées](29-sorties-fhe.md)

## Base et HyperEVM : état et finalité

Frontière entre état observé et état finalisé (voir `prototype/hyperevm_state_boundary.py`).

- [État Base](20-base-state.md)
- [Finalité Base](21-base-finalite.md)
- [Lecture d’état](22-base-lecture.md)
- [Préconditions d’intégration](23-base-preconditions.md)
- [Dépendances externes](24-base-dependances.md)
- [Erreurs d’état](25-base-erreurs.md)
- [Snapshot reproductible](26-base-snapshot.md)
- [Réorganisation](27-base-reorg.md)
- [Frontières d’état](36-state-boundary.md)
- [Contexte de bloc](37-block-context.md)
- [Fraîcheur de l’état](38-state-freshness.md)

## Base : disponibilité des données

Publication, récupération et intégrité des lots (voir `prototype/rollup_data_availability.py`).

- [Indexation Base](28-base-indexation.md)
- [Publication des données](29-base-publication.md)
- [Récupération des données](30-base-recuperation.md)
- [Intégrité des données](31-base-integrite.md)
- [Latence de disponibilité](32-base-latence.md)
- [Donnée absente](33-base-absence.md)
- [Fenêtre d’observation](34-base-fenetre.md)
- [Responsabilités du rollup](35-base-responsabilites.md)
- [Preuve de disponibilité](36-base-preuve.md)
- [Limites du modèle](37-base-limites.md)
- [Audit Base](38-base-audit.md)

## EVM : erreurs et reverts

Décodage des données de revert (voir `prototype/evm_revert_decoder.py`).

- [Décodage revert](30-revert-selector.md)
- [Erreurs standardisées](31-errors-standards.md)
- [ABI des erreurs](32-abi-revert.md)
- [Revert inconnu](33-revert-inconnu.md)
- [Trace d’exécution](34-revert-trace.md)
- [Erreur et sécurité](35-erreur-securite.md)

## Hyperliquid : provenance et fraîcheur

Source, horodatage et conflits de données (voir `prototype/hyperliquid_provenance.py`).

- [Provenance des sources](39-provenance-source.md)
- [Source primaire](40-source-primaire.md)
- [Hash de donnée](41-hash-donnee.md)
- [Fenêtre temporelle](42-fenetre-source.md)
- [Donnée obsolète](43-stale-data.md)
- [Conflit de sources](44-conflit-sources.md)
- [Métadonnées](45-metadata.md)
- [Trace d’API](46-trace-api.md)
- [Limites de provenance](47-limites-provenance.md)

## Invariants de risque

Solvabilité, liquidation, prix et marge (voir `prototype/risk_invariants.py`).

- [Invariant de solvabilité](48-invariant-solvabilite.md)
- [Invariant de liquidation](49-invariant-liquidation.md)
- [Invariant de prix](50-invariant-prix.md)
- [Arrondis de risque](51-invariant-arrondi.md)
- [État de dette](52-invariant-dette.md)
- [État de collatéral](53-invariant-collateral.md)
- [Marge minimale](54-invariant-marge.md)
- [Liquidité disponible](55-invariant-liquidite.md)
- [Retrait de collatéral](56-invariant-retrait.md)
- [Audit Hyperliquid](57-audit-hyperliquid.md)

## Sécurité et revue

Revue, divulgation responsable, menaces et hypothèses.

- [Revue de sécurité](58-revue-securite.md)
- [Divulgation responsable](59-responsible-disclosure.md)
- [Modèle de menaces](60-menaces.md)
- [Registre des hypothèses](61-hypotheses.md)

[Retour au projet](../../README.md).
