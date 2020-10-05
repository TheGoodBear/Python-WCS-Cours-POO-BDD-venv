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

    # literal content
    Title = f"Création d'un animal"

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

        # print body
        cls.PrintBody()
        print()

        # ask updated data
        AnimalName = Util.GetUserInput(
            "Nom de l'animal : ", 
            "str", 
            2, 
            30, 
            None)
        AnimalIdType = Util.GetUserInput(
            "Type de l'animal : ", 
            "int", 
            None, 
            None, 
            [Type.id for Type in Var.Types])

        # create data in DB
        SQLQuery = f"INSERT INTO {Animal.TableName} "
        SQLQuery += "(name, id_type) "
        SQLQuery += "VALUES (%s, %s) "
        SQLValues = (AnimalName, AnimalIdType)
        DB.ExecuteQuery(SQLQuery, SQLValues, True)

        # confirm update
        cls.Body = f"\nL'animal a été ajouté."
        cls.PrintBody()

        # refresh collections from DB
        App.InitializeData()

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
        