# Quatre exemples techniques vérifiables

Ces exemples montrent comment relier un domaine à une hypothèse contrôlable. Les liens pointent vers les parcours documentaires ; ils ne remplacent pas la lecture de la version source citée.

## Base — preuve et finalisation

- Parcours : [base/docs/fr](https://github.com/CryptoAstuce/base/tree/main/docs/fr)
- Références locales : [METHODOLOGIE-RECHERCHE.md](../METHODOLOGIE-RECHERCHE.md), [SECURITY.md](../SECURITY.md)
- Question vérifiable : la chaîne préimage → worker → preuve → contestation est-elle documentée sans confondre attestation et finalité ?

## Hyperliquid — provenance des métriques

- Parcours : [hyperliquid-stats-web/docs/fr](https://github.com/CryptoAstuce/hyperliquid-stats-web/tree/main/docs/fr)
- Référence locale : [README.md](../README.md), section « Focus Base et HyperEVM »
- Question vérifiable : chaque métrique conserve-t-elle sa source, sa transformation, son unité et son état de fraîcheur ?

## ZK — contraintes et vérification

- Parcours : [halo2-lib/docs/fr](https://github.com/CryptoAstuce/halo2-lib/tree/main/docs/fr)
- Référence locale : [METHODOLOGIE-RECHERCHE.md](../METHODOLOGIE-RECHERCHE.md)
- Question vérifiable : les entrées publiques, contraintes, engagements et vérificateur sont-ils distingués dans l’explication ?

## FHE — calcul et frontières de confiance

- Parcours : [SEAL-Embedded/docs/fr](https://github.com/CryptoAstuce/SEAL-Embedded/tree/main/docs/fr)
- Référence locale : [SECURITY.md](../SECURITY.md)
- Question vérifiable : les clés, le chiffrement, le calcul homomorphe et la restitution du résultat ont-ils des responsabilités séparées ?

## Règle de traçabilité

Une affirmation est considérée comme exploitable seulement si elle possède un dépôt, une branche ou un tag, un chemin de fichier et, lorsque le code est cité, un symbole confirmé dans cette version. Les quatre exemples sont des points d’entrée documentaires : ils n’inventent pas de noms de fonctions non vérifiés.
