# coding: utf-8

# import modules

# import additional code
import Variables as Var
import Utilities.Utilities as Util
import Utilities.RichConsole as RC
import Utilities.DBUtil as DB

# import models
from Models.Animal import Animal
from Models.Type import Type
from Models.Country import Country


# functions
def InitializeData():
    """
        Initialize data (collections)
    """

    # load data from DB in collections
    Var.Types = LoadData(Var.Types, Type)
    Var.Animals = LoadData(Var.Animals, Animal, "animal.name")   
    Var.Countries = LoadData(Var.Countries, Country)


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
    MyResult = DB.ExecuteQuery(MyQuery)

    # create collection
    MyCollection = CreateCollection(MyResult, MyCollection, MyModel)
    
    # specific for recursive model
    if MyModel is Type:
        # get parents (recursivity)
        for Element in MyCollection:
            Element.GetParent(MyCollection)

    # return collection
    return MyCollection
