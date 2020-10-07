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

        RC.ClearConsole()
        print(cls.Title)
        cls._UnderlineTitle()


    @classmethod
    def PrintContent(cls, 
        Start = 0,
        End = None):
        """
            Print body content (subset of ContentList)
        """

        ListSubset = cls.ContentList[Start:] if End is None else cls.ContentList[Start:End + 1]

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

        ListSubset = cls.UserDataList[Start:] if End is None else cls.UserDataList[Start:End + 1]

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

        return ResultList


    @classmethod
    def PrintDataList(cls):
        """
            Print data list
        """

        # print each collection
        for Data in cls.DataList:
            App.PrintCollection(eval(f"Var.{Data.CollectionObject}"), Data)


    @classmethod
    def _UnderlineTitle(cls):
        """
            Print dashes under title
            _ private method
        """

        print("\n".rjust(len(cls.Title) + 1, "-"))