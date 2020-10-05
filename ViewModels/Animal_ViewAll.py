# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC
import Utilities.Utilities as Util
import Utilities.ApplicationUtilities as App

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal
from Models.Type import Type


class Animal_ViewAll(VM.ViewModel):
    """
        View model for Read all CRUD action on Animal model
    """

    # class properties

    # literal content
    Title = f"Liste des {Animal.CollectionTitle}"
    Body = f"Voici la liste de tous les {Animal.CollectionTitle} de la base."
    UserChoices = [
        {
            "Message" : "\nAppuyez sur Entrée pour revenir au menu...",
            "ValueType" : "str",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        }
    ]

    # dynamic data
    DataList = [Animal]


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

        # show each collection
        for Data in cls.DataList:
            App.PrintCollection(eval(f"Var.{Data.CollectionObject}"), Data)

        UserValue = 0
        for UserChoice in cls.UserChoices:
            UserValue = Util.GetUserInput(
                UserChoice["Message"], 
                UserChoice["ValueType"], 
                UserChoice["Minimum"], 
                UserChoice["Maximum"], 
                UserChoice["PossibleValues"], 
                UserChoice["DefaultValue"])

        # return to home view
        Var.CurrentView = "Home"
        