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

    # literal content
    Title = f"Modification d'un animal"

    UserChoicesBefore = [
        {
            "Message" : "\nQuel animal voulez-vous modifier : ",
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
            MyAnimal = MyAnimal[0]
            cls.Body = f"\nID → {MyAnimal.id}"
            cls.Body += f"\nNom → {MyAnimal.name}"
            cls.Body += f"\nType → {MyAnimal.type}"
        else:
            cls.Body = f"\nL'animal numéro {UserValue} n'existe pas."

        # print body
        cls.PrintBody()
        print()

        # ask updated data
        MyAnimal.name = Util.GetUserInput(
            "Nom de l'animal : ", 
            "str", 
            2, 
            30, 
            None, 
            MyAnimal.name)
        MyAnimal.id_type = Util.GetUserInput(
            "Type de l'animal : ", 
            "int", 
            None, 
            None, 
            [Type.id for Type in Var.Types], 
            MyAnimal.id_type)

        # update data in DB
        SQLQuery = f"UPDATE {Animal.TableName} "
        SQLQuery += "SET name = %s, id_type = %s "
        SQLQuery += "WHERE id = %s"
        SQLValues = (MyAnimal.name, MyAnimal.id_type, MyAnimal.id)
        DB.ExecuteQuery(SQLQuery, SQLValues, True)

        # confirm update
        cls.Body = f"\nL'animal numéro {MyAnimal.id} a été modifié."
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
        