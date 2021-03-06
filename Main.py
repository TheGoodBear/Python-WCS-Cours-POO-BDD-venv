# coding: utf-8

# import modules

# import additional code
import Variables as Var
import Utilities.ApplicationUtilities as App

# import view models
from ViewModels.Home import Home
from ViewModels.AllTablesData import AllTablesData
from ViewModels.Animal_ViewAll import Animal_ViewAll
from ViewModels.Animal_ViewOne import Animal_ViewOne
from ViewModels.Animal_Edit import Animal_Edit
from ViewModels.Animal_Add import Animal_Add
from ViewModels.Animal_Delete import Animal_Delete


# functions
def Main():
    """
        Program entry
    """

    # load data from DB in collections
    App.InitializeData()

    # main apllication loop
    while Var.ApplicationRun:
        # Show current view
        eval(f"{Var.CurrentView}").Show()

    print("\nAu revoir.\n")


# code entry point
if __name__ == "__main__":
    Main()