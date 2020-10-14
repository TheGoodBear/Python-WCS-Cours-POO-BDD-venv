# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC
import Utilities.Utilities as Util
import Utilities.ApplicationUtilities as App

# import generic view model
import ViewModels.GenericVM as VM


class Home(VM.ViewModel):
    """
        View model for Home view
    """

    # class properties
    Title = "Gestion des observations d'animaux"
    ContentList = [
        "1 - Voir les données de toutes les tables",
        "2 - Voir les animaux",
        "3 - Voir un animal",
        "4 - Modifier un animal",
        "5 - Ajouter un animal", 
        "6 - Supprimer un animal",
        "0 - Quitter l'application"]
    UserDataList = [
        {
            "Message" : "\nSélectionnez votre choix : ",
            "ValueType" : "int",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : [1, 2, 3, 4, 5, 6, 0],
            "DefaultValue" : None
        }
    ]


    # class method
    @classmethod
    def Show(cls):
        """
            Show view
        """

        # show content
        cls.PrintHeader()
        cls.PrintContent()
        Result = cls.AskData()[0]

        # manage user data
        if Result == 1:
            Var.CurrentView = "AllTablesData"
        elif Result == 2:
            Var.CurrentView = "Animal_ViewAll"
        elif Result == 3:
            Var.CurrentView = "Animal_ViewOne"
        elif Result == 4:
            Var.CurrentView = "Animal_Update"
        elif Result == 5:
            Var.CurrentView = "Animal_Add"
        elif Result == 6:
            Var.CurrentView = "Animal_Delete"
        elif Result == 0:
            Var.ApplicationRun = False
