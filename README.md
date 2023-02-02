# Datathon BCG GAMMA x Polytechnique

Repo de l'équipe **Alpha Team** composée d'Etienne du Fayet, Gaspard de Fommervault, Sacha Braun et Quentin Lao. Notre équipe avons fini **2ème du classement** final. L'évaluation prenait en compte :
* les performances de nos prédictions (RSME)
* l'aspect business (qualité des livrables, de la soutenance finale, des solutions proposées, etc.)

## Présentation

![Front page datathon](img/front_page.jpg)

### Le client

* LivraisonCo est une entreprise française privée de livraison opérant principalement en région parisienne
* Le CEO de LivraisonCo souhaite optimiser son processus de livraison (e.g. livrer plus de colis en un temps réduit, en limitant les coûts et son empreinte
carbone) d’une semaine sur l’autre
* Selon le CEO, connaître à l’avance l’état du trafic serait un premier élément clé pour mieux définir ses créneaux de livraison pour la semaine suivante

### La mission

* Le développement d’un algorithme de prédiction du trafic routier sur différents axes à Paris (Les Champs-Elysées, la rue de la Convention et la rue des Saints-Pères)
* Une présentation expliquant l’approche et les résultats de l’algorithme de prédiction du trafic routier, ainsi qu’une feuille de route de la suite du projet

## Arborescence des fichiers

L'annexe finale avec tout notre code et analyses expliquées sont présents dans le notebook Python `annexe_livrable_alpha_team`.

Toutes les données sont stockées dans le dossier `data`. Si le dossier est venu à changer de nom ou les données déplacées, alors il faut modifier la variable `path` dans la première cellule du notebook.

Le fichier csv avec les submissions est rangé directement à la racine sous le nom de `livrable_alpha_team.csv`.

Nous avons en plus créé une interface user-friendly utile pour le client pour visualiser le traffic : `API.py`. Utiliser la commande `pip install -r requirements.txt` pour installer les libraries.

Notre présentation finale se trouve directement à la racine `Présentation finale.pdf`.
