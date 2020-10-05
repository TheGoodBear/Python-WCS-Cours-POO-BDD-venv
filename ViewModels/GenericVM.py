# coding: utf-8

# import additional code
import Variables as Var
import Utilities.RichConsole as RC


class ViewModel():
    """
        Generic class for View Models
    """

    # class properties

    # literal content
    Title = ""
    Body = ""
    UserChoice = []


    @classmethod
    def PrintHeader(cls):
        """
            Print header
        """

        RC.ClearConsole()
        print(cls.Title)
        cls._UnderlineTitle()


    @classmethod
    def PrintBody(cls):
        """
            Print body
        """

        if cls.Body.strip() != "":
            print(cls.Body)


    @classmethod
    def _UnderlineTitle(cls):
        """
            Print dashes under title
            _ Private method
        """

        print("\n".rjust(len(cls.Title) + 1, "-"))