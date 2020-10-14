# coding: utf-8

# import additional code
import Variables as Var

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal


class Animal_Add(VM.ViewModel):
    """
        View model for create CRUD action on Animal model
    """

    # class properties
    Title = f"Création d'un animal"
    UserDataList = [
        {
            "Message" : "Nom de l'animal : ",
            "ValueType" : "str",
            "Minimum" : 2,
            "Maximum" : 30,
            "PossibleValues" : None,
            "DefaultValue" : None
        },
        {
            "Message" : "Type de l'animal : ",
            "ValueType" : "int",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : None,
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

        # complete user data
        cls.UserDataList[1]["PossibleValues"] = [Type.id for Type in Var.Types]

        # ask data
        # create new temporary animal (with primary key = None)
        MyAnimal = Animal((None, ) + tuple(cls.AskData(0, 1)))
        
        # create animal
        cls.ContentList.append(MyAnimal.Add())
        # print result
        cls.PrintContent()

        # return to home view
        VM.ViewModel.ReturnToHome()
