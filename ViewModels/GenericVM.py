# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC
import Utilities.Utilities as Util
import Utilities.ApplicationUtilities as App


class ViewModel():
    """
        Generic class for View Models
    """

    # class properties

    # literal content
    Title = ""
    ContentList = []
    UserDataList = []
    DataList = []


    @classmethod
    def PrintHeader(cls):
        """
            Print header
        """

        # clear console
        RC.ClearConsole()
        # print view title
        print(cls.Title)
        # underline title
        cls._UnderlineTitle()


    @classmethod
    def PrintContent(cls, 
        Start = 0,
        End = None):
        """
            Print body content (subset of ContentList)
        """

        # get slice of ContentList to be printed
        ListSubset = cls.ContentList[Start:] if End is None else cls.ContentList[Start:End + 1]

        # print each string in slice
        for Content in ListSubset:
            print(Content)


    @classmethod
    def AskData(cls, 
        Start = 0,
        End = None):
        """
            Ask data to user (subset of DataList)
            in a list of dictionaries containing data meta datas
            and return a list of results
        """

        # get slice of UserDataList to be inputed
        ListSubset = cls.UserDataList[Start:] if End is None else cls.UserDataList[Start:End + 1]

        # input each data in slice and store results in a new list
        ResultList = []
        for Data in ListSubset:
            Result = Util.GetUserInput(
                Data["Message"], 
                Data["ValueType"], 
                Data["Minimum"], 
                Data["Maximum"], 
                Data["PossibleValues"], 
                Data["DefaultValue"])
            ResultList.append(Result)

        # return results
        return ResultList


    @classmethod
    def PrintDataList(cls):
        """
            Print data list
        """

        # for each collection in data list
        for Data in cls.DataList:
            # print instances in collection
            App.PrintCollection(eval(f"Var.{Data.CollectionObject}"), Data)


    @classmethod
    def _UnderlineTitle(cls):
        """
            Print dashes under title
            _ private method
        """

        # create a string of - of same length as title and prints it to underline
        print("\n".rjust(len(cls.Title) + 1, "-"))


    @staticmethod
    def ReturnToHome():
        """
            Ask for user entry then return to home view
        """

        # ask user to type Enter key
        Util.GetUserInput(
            "\nAppuyez sur Entrée pour revenir au menu...", 
            DefaultValue = "")

        # return to home view
        Var.CurrentView = "Home"
