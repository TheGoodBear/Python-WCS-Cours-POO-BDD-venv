# coding: utf-8

# import additional code
import Variables as Var

# import generic view model
import ViewModels.GenericVM as VM


class Home(VM.ViewModel):
    """
        View model for Home view
    """

    # class properties
    Title = "Gestion des observations d'animaux"
    ContentList = [Menu["Label"] for Menu in Var.MenuEntries]
    UserDataList = [
        {
            "Message" : "\nSélectionnez votre choix : ",
            "ValueType" : "int",
            "Minimum" : None,
            "Maximum" : None,
            "PossibleValues" : [int(Menu["Value"]) for Menu in Var.MenuEntries],
            "DefaultValue" : None
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
        cls.PrintContent()

        # ask user menu choice
        MenuNumber = cls.AskData()[0]
        # get matching menu view
        MenuView = [Menu["View"] for Menu in Var.MenuEntries if Menu["Value"] == MenuNumber][0]
        # execute user action        
        if MenuView is None:
            # quit program
            Var.ApplicationRun = False
        else:
            # go to choosen view
            Var.CurrentView = MenuView
