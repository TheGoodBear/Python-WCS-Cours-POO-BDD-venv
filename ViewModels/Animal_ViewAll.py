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
    Title = f"Liste des {Animal.CollectionTitle}"
    ContentList = [f"\nVoici la liste de tous les {Animal.CollectionTitle} de la base."]
    UserDataList = [
        {
            "Message" : "\nAppuyez sur Entrée pour revenir au menu...",
            "ValueType" : "str",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        }
    ]
    DataList = [Animal]


    # class method
    @classmethod
    def Show(cls):
        """
            Show view
        """

        # show content
        cls.PrintHeader()
        cls.PrintContent()
        cls.PrintDataList()

        # return to home view
        cls.AskData()
        Var.CurrentView = "Home"
