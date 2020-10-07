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


class Animal_ViewOne(VM.ViewModel):
    """
        View model for Read one CRUD action on Animal model
    """

    # class properties
    Title = f"Détail d'un animal"
    UserDataList = [
        {
            "Message" : "\nDe quel animal voulez-vous le détail : ",
            "ValueType" : "int",
            "Minimum" : 1,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        },
        {
            "Message" : "\nAppuyez sur Entrée pour revenir au menu...",
            "ValueType" : "str",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
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
        cls.PrintDataList()    

        # search specified animal in collection
        AnimalID = cls.AskData(0, 0)[0]
        AnimalList = [
            Animal 
            for Animal 
            in Var.Animals 
            if Animal.id == AnimalID]
        MyAnimal = AnimalList[0] if len(AnimalList) == 1 else None
        if MyAnimal is not None:
            cls.ContentList = [
                f"\nID → {MyAnimal.id}",
                f"Nom → {MyAnimal.name}",
                f"Type → {MyAnimal.type}"]
        else:
            cls.ContentList = [f"\nL'animal numéro {AnimalID} n'existe pas."]

        # print content
        cls.PrintContent()

        # return to home view
        cls.AskData(len(cls.UserDataList) - 1)
        Var.CurrentView = "Home"
        