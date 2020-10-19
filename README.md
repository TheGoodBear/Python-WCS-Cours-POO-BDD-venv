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


---------------------------
Fonctionnement du programme
---------------------------

--- Menu utilisé dans le vue Home :
Il est défini dans variables.py par une liste de dictionnaires MenuEntries
→ Value : entrée attendue par l'utilisateur pour accéder à la vue
→ Label : label du menu à afficher
→ View : chaine de caractère représentant le nom de la vue (fichier .py du dossier ViewModels)

--- Définition des models de données
Un fichier .py par table de la BDD (modèle) dans le dossier Models contenant une classe de même nom hétitant da la classe générique Model (fichier GenericM.py)
La liste Fields des champs (colonnes) du modèle est définie par une liste de dictionnaires dans chaque modèle
→ Name : le nom du champ (identique à la BDD)
→ Label : le nom imprimable du champ
→ Native : True - le champ est dans la table de la BDD, False - il s'agit d'une propriété calculée
→ Key : None - le champ n'est pas une clé, Primary - il s'agit de la clé primare du modèle, Le nom d'un autre modèle - il s'agit d'une clé étrangère vers ce modèle
→ Add : True - le champ doit être inclus dans une requête INSERT INTO
→ Update : True - le champ doit être inclus dans une requête UPDATE
→ Print : True - le champ est imprimé lors de la visualisation d'une instance

--- Définition des modèles de vues
Un fichier .py par vue dans le dossier ViewModels contenant une classe de même nom hétitant da la classe générique ViewModel (fichier GenericVM.py)
→ Title : titre de la vue
→ ContentList : liste de chaines à afficher dans la vue (grâce à un slice Start/End passé à la méthode PrintContent)
→ UserDataList : liste de dictionnaires d'informtions à demander à l'utilisateur dans la vue (grâce à un slice Start/End passé à la méthode AskData)
→ DataList : list de modèles dont les instances doivent être affichées par la méthode PrintDataList
