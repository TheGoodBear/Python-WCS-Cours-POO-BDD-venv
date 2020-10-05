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

    # literal content
    Title = "Gestion des observations d'animaux"
    Body = (
        "1 - Voir les données de toutes les tables\n" +
        "2 - Voir les animaux\n" + 
        "3 - Voir un animal\n" + 
        "4 - Modifier un animal\n" + 
        "5 - Ajouter un animal\n" + 
        "6 - Supprimer un animal\n" + 
        "0 - Quitter l'application")
    UserChoices = [
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

        RC.ClearConsole()

        # show content
        cls.PrintHeader()
        cls.PrintBody()

        UserValue = 0
        for UserChoice in cls.UserChoices:
            UserValue = Util.GetUserInput(
                UserChoice["Message"], 
                UserChoice["ValueType"], 
                UserChoice["Minimum"], 
                UserChoice["Maximum"], 
                UserChoice["PossibleValues"], 
                UserChoice["DefaultValue"])

        # manage data
        if UserValue == 1:
            Var.CurrentView = "TablesData"
        elif UserValue == 2:
            Var.CurrentView = "Animal_ViewAll"
        elif UserValue == 3:
            Var.CurrentView = "Animal_ViewOne"
        elif UserValue == 4:
            Var.CurrentView = "Animal_Edit"
        elif UserValue == 5:
            Var.CurrentView = "Animal_Add"
        elif UserValue == 6:
            Var.CurrentView = "Animal_Delete"
        elif UserValue == 0:
            Var.ApplicationRun = False
