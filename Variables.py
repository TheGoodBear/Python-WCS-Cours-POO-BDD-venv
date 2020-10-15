# coding: utf-8

# global properties
ApplicationRun = True
CurrentView = "Home"
MenuEntries = [
    {
        "Value" : 1,
        "Label" : "1 - Voir les données de toutes les tables",
        "View" : "AllTablesData"
    },
    {
        "Value" : 2,
        "Label" : "2 - Voir les animaux",
        "View" : "Animal_ViewAll"
    },
    {
        "Value" : 3,
        "Label" : "3 - Voir un animal",
        "View" : "Animal_ViewOne"
    },
    {
        "Value" : 4,
        "Label" : "4 - Modifier un animal",
        "View" : "Animal_Update"
    },
    {
        "Value" : 5,
        "Label" : "5 - Ajouter un animal",
        "View" : "Animal_Add"
    },
    {
        "Value" : 6,
        "Label" : "6 - Supprimer un animal",
        "View" : "Animal_Delete"
    },
    {
        "Value" : 0,
        "Label" : "0 - Quitter l'application",
        "View" : None
    },
]

# collections
Animals = []
Types = []
Countries = []