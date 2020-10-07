# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC
import Utilities.Utilities as Util
import Utilities.DBUtil as DB
import Utilities.ApplicationUtilities as App

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal
from Models.Type import Type


class Animal_Edit(VM.ViewModel):
    """
        View model for update CRUD action on Animal model
    """

    # class properties
    Title = f"Modification d'un animal"
    UserDataList = [
        {
            "Message" : "\nQuel animal voulez-vous modifier : ",
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
        print()

        if MyAnimal is not None:
            # ask updated data
            cls.UserDataList[1]["DefaultValue"] = MyAnimal.name
            cls.UserDataList[2]["PossibleValues"] = [Type.id for Type in Var.Types]
            cls.UserDataList[2]["DefaultValue"] = MyAnimal.id_type
            MyAnimal.name, MyAnimal.id_type = tuple(cls.AskData(1, 2))

            # update data in DB
            SQLQuery = f"UPDATE {Animal.TableName} "
            SQLQuery += "SET name = %s, id_type = %s "
            SQLQuery += "WHERE id = %s"
            SQLValues = (MyAnimal.name, MyAnimal.id_type, MyAnimal.id)
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # confirm update
            cls.ContentList.append(f"\nL'animal numéro {MyAnimal.id} a été modifié.")
            cls.PrintContent(len(cls.ContentList) - 1)

        # refresh collections from DB
        App.InitializeData()

        # return to home view
        cls.AskData(len(cls.UserDataList) - 1)
        Var.CurrentView = "Home"
