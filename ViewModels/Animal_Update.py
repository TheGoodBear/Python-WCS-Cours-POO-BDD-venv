# coding: utf-8

# import additional code
import Variables as Var

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal


class Animal_Update(VM.ViewModel):
    """
        View model for update CRUD action on Animal model
    """

    # class properties
    Title = f"Modification d'un animal"
    UserDataList = [
        {
            "Message" : "Quel animal voulez-vous modifier : ",
            "ValueType" : "int",
            "Minimum" : 1,
            "Maximum" : None,
            "PossibleValues" : None,
            "DefaultValue" : ""
        },
        {
            "Message" : "Nom de l'animal : ",
            "ValueType" : "str",
            "Minimum" : 2,
            "Maximum" : 30,
            "PossibleValues" : None,
            "DefaultValue" : ""
        },
        {
            "Message" : "Type de l'animal : ",
            "ValueType" : "int",
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

        # search specified animal in collection
        AnimalID = cls.AskData(0, 0)[0]
        MyAnimal, cls.ContentList = Animal.GetData(AnimalID)

        # print content
        cls.PrintContent()
        print()

        if MyAnimal is not None:
            # complete user data
            cls.UserDataList[1]["DefaultValue"] = MyAnimal.name
            cls.UserDataList[2]["PossibleValues"] = [Type.id for Type in Var.Types]
            cls.UserDataList[2]["DefaultValue"] = MyAnimal.id_type
            
            # ask updated data
            MyAnimal.name, MyAnimal.id_type = cls.AskData(1, 2)

            # update animal
            cls.ContentList.append(MyAnimal.Update())
            # print result
            cls.PrintContent(len(cls.ContentList) - 1)

        # return to home view
        VM.ViewModel.ReturnToHome()
