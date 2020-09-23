# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC

# import generic view model
import ViewModels.GenericVM as VM

# import models
from Models.Animal import Animal
from Models.Type import Type
from Models.Country import Country


class TablesData(VM.ViewModel):
    """
        View model for Tables data view
    """

    # class properties

    # literal content
    Title = "Gestion des observations d'animaux"
    Body = "Voici la liste de toutes les données de la base."
    UserChoiceMessage = "\nAppuyez sur Entrée pour revenir au menu..."

    # dynamic data
    DataList = [Type, Animal, Country]
