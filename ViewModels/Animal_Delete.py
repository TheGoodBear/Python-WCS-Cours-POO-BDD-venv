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


class Animal_Delete(VM.ViewModel):
    """
        View model for delete CRUD action on Animal model
    """

    # class properties
    Title = f"Suppression d'un animal"
    UserDataList = [
        {
            "Message" : "\nQuel animal voulez-vous supprimer : ",
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
            # ask user confirmation
            Confirm = cls.AskData(1, 1)
            if Confirm:
                # delete data in DB
                SQLQuery = f"DELETE FROM {Animal.TableName} "
                SQLQuery += "WHERE id = %s"
                SQLValues = (MyAnimal.id, )
                DB.ExecuteQuery(SQLQuery, SQLValues, True)

                # confirm delete
                cls.ContentList.append(f"\nL'animal numéro {MyAnimal.id} a été supprimé.")
                cls.PrintContent(len(cls.ContentList) - 1)

                # refresh collections from DB
                App.InitializeData()

        # return to home view
        cls.AskData(len(cls.UserDataList) - 1)
        Var.CurrentView = "Home"
