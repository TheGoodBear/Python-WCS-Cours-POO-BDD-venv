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

        # ask data
        cls.UserDataList[1]["PossibleValues"] = [Type.id for Type in Var.Types]
        AnimalName, AnimalIdType = tuple(cls.AskData(0, 1))

        # create data in DB
        SQLQuery = f"INSERT INTO {Animal.TableName} "
        SQLQuery += "(name, id_type) "
        SQLQuery += "VALUES (%s, %s) "
        SQLValues = (AnimalName, AnimalIdType)
        DB.ExecuteQuery(SQLQuery, SQLValues, True)

        # confirm create
        cls.ContentList = [f"\nL'animal a été ajouté."]
        cls.PrintContent()

        # refresh collections from DB
        App.InitializeData()

        # return to home view
        cls.AskData(len(cls.UserDataList) - 1)
        Var.CurrentView = "Home"
