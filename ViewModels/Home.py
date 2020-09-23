# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC

# import generic view model
import ViewModels.GenericVM as VM

class Home(VM.ViewModel):
    """
        View model for Home view
    """

    # class properties

    # literal content
    Title = "Liste des données de la base"
    Body = (
        "1 - Voir les données de toutes les tables\n" +
        "2 - Voir les animaux\n" + 
        "3 - Modifier un animal\n" + 
        "4 - Ajouter un animal\n" + 
        "0 - Quitter l'application")
    UserChoiceMessage = "\nSélectionnez votre choix : "
    UserChoiceValueType = "int"
    UserChoicePossibleValues = [1, 2, 3, 4, 0]
