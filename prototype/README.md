# Mini-prototype : analyser les commits et leurs critères

Ce prototype propose un modèle expérimental, transparent et reproductible pour comparer un historique GitHub avec un compteur externe comme Guild. Il ne prétend pas reproduire les règles privées de Guild.

## Périmètre CryptoAstuce

Les cas de référence couvrent les quatre axes du profil : Base, Hyperliquid, ZK et FHE. Le domaine est conservé comme métadonnée pour comparer les familles de travaux ; la décision commune vérifie visibilité publique, auteur, branche et fichiers modifiés.

## Utilisation

Avec Python 3.10 ou supérieur, depuis ce dossier :

    python -m unittest -v test_commit_classifier.py

Aucune dépendance externe n’est nécessaire. Les tests ne modifient ni GitHub ni le dépôt.

## Donnée d’entrée minimale

    {"sha":"abc123","author":"CryptoAstuce","visibility":"public","branch":"main","files":["docs/base.md"],"domain":"Base","is_merge":false}

## Lecture des résultats

Le moteur renvoie les SHA acceptés et, pour chaque rejet, une liste de raisons explicites. Une divergence avec Guild est un signal à étudier : critère différent, fenêtre temporelle, identité d’auteur ou cache du service. Elle ne doit pas être corrigée en ajoutant des commits artificiels.

## Limites

Le prototype ne se connecte pas à l’API GitHub, ne vérifie pas les e-mails et n’exécute aucune logique de Guild. Pour une étape ultérieure, on pourra ajouter un export JSON manuel de commits déjà observés, en conservant SHA, auteur, branche, visibilité et fichiers modifiés.
