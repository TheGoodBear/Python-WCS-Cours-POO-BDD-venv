# coding: utf-8

# import modules
import psycopg2

# import additional code
import Variables as Var
import Utilities.Utilities as Util
import Utilities.RichConsole as RC

# import view models
from ViewModels.Home import Home
from ViewModels.TablesData import TablesData

# import models
from Models.Animal import Animal
from Models.Type import Type
from Models.Country import Country


def DBConnect():
    """
        Connect to Database
    """
    MyConnection = None

    try:
        MyConnection = psycopg2.connect(
            host="localhost",
            database="dojo_animal",
            user="postgres",
            password="PG20"
        )
    except(Exception, psycopg2.DatabaseError) as Error:
        # error
        print(f"\nCannot connect to specified DB :\n{Error}")

    return MyConnection


def ExecuteQuery(
    MyQuery,
    MyConnection = None,
    CloseConnection = True):
    """
        Execute Specified SQL query
        return query result
    """

    if MyConnection is None:
        # connect to DB if connexion does not exist yet
        MyConnection = DBConnect()

    MyResult = None

    if MyConnection is not None:
        # create DB cursor
        MyCursor = MyConnection.cursor()
        # execute query
        MyCursor.execute(MyQuery)
        # get result
        MyResult = MyCursor.fetchall()
        # close cursor
        MyCursor.close()

    if CloseConnection:
        # close resources if specified
        MyConnection.close()

    return MyResult


def CreateCollection(
    MyResult,
    MyCollection,
    MyModel,
    ResetCollection = True):
    """
        Create generic collection from query result
    """
    if ResetCollection:
        MyCollection = []
    
    # create MyCollection collection
    for Element in MyResult:
        # add an new instance of model to collection
        # this means each line in MyResult (DB table)
        #    equals one instance of MyModel class 
        MyCollection.append(
            MyModel(Element))
    
    return MyCollection


def PrintCollection(
    MyCollection, 
    MyModel):
    """ 
        Print Collection
    """    

    # print collection title
    print(f"\nListe des {MyModel.CollectionTitle} :")

    # print collection items
    for MyElement in MyCollection:
        print(MyElement)


def LoadData(
    MyCollection, 
    MyModel, 
    OrderBy = None):
    """
        Loads data for a specific model
        from database matching table
        Store it in appropriate collection
        And print collection
    """

    # create query
    MyQuery = f"SELECT * FROM {MyModel.TableName}"
    if OrderBy is not None:
        MyQuery += f" ORDER BY {OrderBy}"
    
    # execute query
    MyResult = ExecuteQuery(MyQuery)

    # create collection
    MyCollection = CreateCollection(MyResult, MyCollection, MyModel)
    
    # specific for recursive model
    if MyModel is Type:
        # get parents (recursivity)
        for Element in MyCollection:
            Element.GetParent(MyCollection)

    # print collection
    # PrintCollection(MyCollection, MyModel)

    # return collection
    return MyCollection


def InitializeData():
    """
        Initialize data (collections)
    """

    # load data from DB in collections
    Var.Types = LoadData(Var.Types, Type)
    Var.Animals = LoadData(Var.Animals, Animal, "animal.name")   
    Var.Countries = LoadData(Var.Countries, Country)


def HomeView():
    """
        Show home view
    """

    # show content
    Home.PrintHeader()
    Home.PrintBody()
    UserChoice = Util.GetUserInput(
        Home.UserChoiceMessage, 
        Home.UserChoiceValueType, 
        PossibleValues=Home.UserChoicePossibleValues)

    # manage data
    if UserChoice == 1:
        TablesDataView()
    elif UserChoice == 0:
        Var.ApplicationRun = False


def TablesDataView():
    """
        Show tables data view
    """

    # show content
    TablesData.PrintHeader()
    TablesData.PrintBody()

    # show each collection
    for Data in TablesData.DataList:
        PrintCollection(eval(f"Var.{Data.CollectionObject}"), Data)

    # return to home view
    UserChoice = Util.GetUserInput(
        TablesData.UserChoiceMessage, 
        DefaultValue=TablesData.UserChoiceDefaultValue)


def Main():
    """
        Program entry
    """

    # load data from DB in collections
    InitializeData()

    while Var.ApplicationRun:
        # Show home view
        HomeView()

    print("\nAu revoir.\n")


# code entry point
if __name__ == "__main__":
    Main()