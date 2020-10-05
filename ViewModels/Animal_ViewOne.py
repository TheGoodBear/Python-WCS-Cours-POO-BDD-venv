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

    # literal content
    Title = f"Détail d'un animal"

    UserChoicesBefore = [
        {
            "Message" : "\nDe quel animal voulez-vous le détail : ",
            "ValueType" : "int",
            "Minimum" : 1,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        }
    ]
    UserChoicesAfter = [
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
    # DataList = [Animal]


    # class method
    @classmethod
    def Show(cls):
        """
            Show view
        """

        RC.ClearConsole()

        # show content
        cls.PrintHeader()

        # ask user data
        UserValue = 0
        for UserChoice in cls.UserChoicesBefore:
            UserValue = Util.GetUserInput(
                UserChoice["Message"], 
                UserChoice["ValueType"], 
                UserChoice["Minimum"], 
                UserChoice["Maximum"], 
                UserChoice["PossibleValues"], 
                UserChoice["DefaultValue"])

        # search specified animal in collection
        MyAnimal = [
            Animal 
            for Animal 
            in Var.Animals 
            if Animal.id == UserValue]
        if len(MyAnimal) == 1:
            cls.Body = f"\nID → {MyAnimal[0].id}"
            cls.Body += f"\nNom → {MyAnimal[0].name}"
            cls.Body += f"\nType → {MyAnimal[0].type}"
        else:
            cls.Body = f"\nL'animal numéro {UserValue} n'existe pas."

        # print body
        cls.PrintBody()

        # # show each collection
        # for Data in cls.DataList:
        #     App.PrintCollection(eval(f"Var.{Data.CollectionObject}"), Data)

        # ask user data
        UserValue = 0
        for UserChoice in cls.UserChoicesAfter:
            UserValue = Util.GetUserInput(
                UserChoice["Message"], 
                UserChoice["ValueType"], 
                UserChoice["Minimum"], 
                UserChoice["Maximum"], 
                UserChoice["PossibleValues"], 
                UserChoice["DefaultValue"])

        # return to home view
        Var.CurrentView = "Home"
        