# coding: utf-8

# import modules
import psycopg2

# import additional code
import Variables as Var

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
    MyConnection,
    MyQuery):
    """
        Execute Specified SQL query
        return query result
    """
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
    print(f"\n Liste des {MyModel.CollectionTitle} :")

    # print collection items
    for MyElement in MyCollection:
        print(MyElement)


def LoadData(
    MyConnection, 
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
    MyResult = ExecuteQuery(MyConnection, MyQuery)

    # create collection
    MyCollection = CreateCollection(MyResult, MyCollection, MyModel)
    
    # specific for recursive model
    if MyModel is Type:
        # get parents (recursivity)
        for Element in MyCollection:
            Element.GetParent(MyCollection)

    # print collection
    PrintCollection(MyCollection, MyModel)

    # return collection
    return MyCollection


def Main():
    """
        Program entry
    """

    # connect to DB
    MyConnection = DBConnect()

    # # try DB
    # MyQuery = "SELECT version()"
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # print query result
    # print(f"\n Résultat du test initial : {MyResult[0]}")

    # load data from DB in collections
    Var.Types = LoadData(MyConnection, Var.Types, Type)
    Var.Animals = LoadData(MyConnection, Var.Animals, Animal, "animal.name")   
    Var.Countries = LoadData(MyConnection, Var.Countries, Country)

    # close resources
    MyConnection.close()


# code entry point
if __name__ == "__main__":
    Main()