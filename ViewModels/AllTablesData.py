# coding: utf-8

# import additional code

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal
from Models.Type import Type
from Models.Country import Country


class AllTablesData(VM.ViewModel):
    """
        View model for AllTablesData view
    """

    # class properties
    Title = "Liste de toutes les données de la base"
    ContentList = ["Voici la liste de toutes les données de la base."]
    DataList = [Type, Animal, Country]


    # class method
    @classmethod
    def Show(cls):
        """
            Show view
        """

        # show content
        cls.PrintHeader()
        cls.PrintContent()
        cls.PrintDataList()

        # return to home view
        VM.ViewModel.ReturnToHome()
