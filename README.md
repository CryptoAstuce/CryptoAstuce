# CryptoAstuce

Recherche appliquée et documentation technique francophone sur les systèmes blockchain, avec une attention particulière portée aux hypothèses de sécurité et aux limites opérationnelles.

## Axes de travail

- **ZK, STARK et zk-rollups** — AIR, hachages algébriques, arbres authentifiés et preuves récursives.
- **SNARK et zkEVM** — Halo2, range checks, arithmétique non native, engagements et vérification EVM.
- **FHE** — BFV/BGV/CKKS, chiffrement embarqué, gestion des clés et frontières de confiance.
- **Base L2** — OP Stack, comptes, paiements, précompiles, ponts et fault proofs.
- **Hyperliquid / HyperEVM** — données, métriques, intégrations EVM et qualité des sources.

## Contributions récentes

- [Miden Crypto — primitives STARK](https://github.com/CryptoAstuce/crypto/tree/next/docs/fr)
- [halo2-lib — circuits SNARK et EVM](https://github.com/CryptoAstuce/halo2-lib/tree/main/docs/fr)
- [SEAL-Embedded — FHE sur appareils contraints](https://github.com/CryptoAstuce/SEAL-Embedded/tree/main/docs/fr)
- [Hyperliquid Stats Web — provenance et fraîcheur des métriques](https://github.com/CryptoAstuce/hyperliquid-stats-web/tree/main/docs/fr)
- [Base — bibliothèque documentaire](https://github.com/CryptoAstuce/base-std/tree/main/docs/fr)

## Méthode

Chaque parcours part du code et de la documentation du dépôt source. Les chapitres distinguent les garanties réellement fournies, les hypothèses externes, les risques de mauvaise intégration et les vérifications à reproduire. Aucun résultat de compilation ou de test n’est revendiqué sans exécution observée.

*Open source, cryptographie appliquée et pédagogie technique en français.*

## Focus Base et HyperEVM

- [Système de preuves Base](https://github.com/CryptoAstuce/base/tree/main/docs/fr) — préimages, workers, backend ZK, TEE, soumission et contestation.
- [Sécurité HyperEVM](https://github.com/CryptoAstuce/hyperevm-safety/tree/main/docs/fr) — fraîcheur des oracles, décimales, solvabilité, liquidations et invariants adverses.
- [Traçabilité Hyperliquid](https://github.com/CryptoAstuce/hyperliquid-stats-web/tree/main/docs/fr) — chaîne source-transformation-affichage, précision et états dégradés.

## Parcours de lecture

Les 99 fiches de [`docs/fr`](docs/fr/README.md) (STARK, FHE, Base, HyperEVM, Hyperliquid, invariants de risque, sécurité) sont regroupées par thème dans un [sommaire](docs/fr/README.md), avec pour chaque groupe le prototype correspondant.

## Prototype reproductible

Le [mini-prototype de classification des commits](prototype/) fournit un moteur transparent et des tests sans dépendance externe pour comparer les critères publics avec un compteur externe comme Guild. Il couvre Base, Hyperliquid, ZK et FHE. Le même dossier contient les prototypes pédagogiques cités dans les fiches (trace et FRI STARK, budget de bruit FHE, disponibilité des données, provenance Hyperliquid, invariants de risque) ; la CI exécute tous leurs tests.
