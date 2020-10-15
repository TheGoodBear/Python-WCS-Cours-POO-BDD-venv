# coding: utf-8

# import additional code
import Variables as Var

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal


class Animal_ViewAll(VM.ViewModel):
    """
        View model for Read all CRUD action on Animal model
    """

    # class properties
    Title = f"Liste des {Animal.CollectionTitle}"
    ContentList = []
    DataList = [Animal]


    # class method
    @classmethod
    def Show(cls):
        """
            Show view
        """

        # show content
        cls.PrintHeader()
            
        cls.ContentList = [f"Voici la liste des {len(Var.Animals)} {Animal.CollectionTitle} de la base."]
        cls.PrintContent()

        cls.PrintDataList()

        # return to home view
        VM.ViewModel.ReturnToHome()
