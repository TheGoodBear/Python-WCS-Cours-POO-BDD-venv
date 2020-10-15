# coding: utf-8

# import additional code

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal


class Animal_Delete(VM.ViewModel):
    """
        View model for delete CRUD action on Animal model
    """

    # class properties
    Title = f"Suppression d'un animal"
    UserDataList = [
        {
            "Message" : "Quel animal voulez-vous supprimer : ",
            "ValueType" : "int",
            "Minimum" : 1,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        },
        {
            "Message" : "\nConfirmez-vous la suppression ? ",
            "ValueType" : "bool",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : False
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

        # search specified animal in collection
        AnimalID = cls.AskData(0, 0)[0]
        MyAnimal, cls.ContentList = Animal.GetData(AnimalID)

        # print content
        cls.PrintContent()
        print()
        
        if MyAnimal is not None:
            # ask user confirmation
            Confirm = cls.AskData(1, 1)[0]
            if Confirm:
                # delete animal
                cls.ContentList.append(MyAnimal.Delete())
                # print result
                cls.PrintContent(len(cls.ContentList) - 1)

        # return to home view
        VM.ViewModel.ReturnToHome()
