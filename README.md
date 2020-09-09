# Python-WCS-Cours-POO-BDD-venv

-------------------------------------------------------------------------
Application de la POO au modèles de données avec interaction avec une BDD
-------------------------------------------------------------------------


Installation de l'environnement virtuel :
1 - Ouvrir un terminal (menu Terminal/Nouveau terminal)
2 - Exécuter "python -m venv env"
3 - Sélectionner l'environnement virtuel comme interprêteur
4 - Installer les packages nécessaires dans l'environement virtuel : 
    "pip install -r requirements.txt"
5 - L'environnement est prêt à fonctionner


Installation d'une base de données PostgreSQL à partir d'un script sql :
1 - Ouvrir DBeaver
2 - Ajouter une connexion à PostgreSQL si elle n'existe pas encore
3 - Clic droit sur la connexion créée puis menu Créer/Database
4 - Entrer le nom de la BDD (dojo_animal)
5 - Clic droit sur la BDD créée puis menu Outils/Execute script
6 - Dans Input file : sélectionner le fichier .sql désiré (dojo_animal.sql)
7 - Clic sur le bouton Client...
8 - Pour Native client, sélectionner "PostgreSQL binaries" puis OK
9 - Clic sur le bouton Démarrer
10 - La base est créée !
