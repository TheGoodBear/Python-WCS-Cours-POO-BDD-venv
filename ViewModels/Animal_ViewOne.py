# coding: utf-8

# import additional code

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal


class Animal_ViewOne(VM.ViewModel):
    """
        View model for Read one CRUD action on Animal model
    """

    # class properties
    Title = f"Détail d'un animal"
    UserDataList = [
        {
            "Message" : "De quel animal voulez-vous le détail : ",
            "ValueType" : "int",
            "Minimum" : 1,
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
        cls.ContentList = Animal.GetData(AnimalID)[1]

        # print content
        cls.PrintContent()

        # return to home view
        VM.ViewModel.ReturnToHome()
        