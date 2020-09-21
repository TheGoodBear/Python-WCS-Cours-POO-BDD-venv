# coding: utf-8

import psycopg2

import Variables as Var
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
    ListTable,
    NameTable,
    ResetCollection = True):
    """
        Create generic collection from query result
    """
    if ResetCollection:
        ListTable = []
    
    # create Countries collection
    for element in MyResult:
        # print(f"({Country[0]}) {Country[1]}")
        # add an new instance of animal to Countries (collection of Countries)
        # this means each line in animal table (DB)
        #    equals one instance of Country class 
        ListTable.append(
            NameTable(element))
    return ListTable

def PrintCollection(MyCollection, ModelName):
    """ 
        print Collection
    """    
    # print collection
    print(f"\n Liste des {ModelName} :")
    for MyElement in MyCollection:
        print(MyElement)

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

    # execute query
    MyQuery = (
        "SELECT * " +
        "FROM type")
    MyResult = ExecuteQuery(MyConnection, MyQuery)
    # create Types collection
    Var.Types = CreateCollection(MyResult, Var.Types, Type)
    # Get the type parents
    for type in Var.Types:
        type.get_parent()
    # print collection
    PrintCollection(Var.Types, "types d'animaux")

    # execute query
    MyQuery = (
        "SELECT * " +
        "FROM animal " +
        "ORDER BY animal.name")
    MyResult = ExecuteQuery(MyConnection, MyQuery)
    # print query result
    # print(f"\n Résultat de la requête : {MyResult}")
    # create Animals collection
    Var.Animals = CreateCollection(MyResult, Var.Animals, Animal)
    # print collection
    PrintCollection(Var.Animals, "animaux")
    
    # execute query
    MyQuery = (
        "SELECT * " +
        "FROM country")
    MyResult = ExecuteQuery(MyConnection, MyQuery)
    # create Types collection
    Var.Countries = CreateCollection(MyResult, Var.Countries, Country)
    # print collection
    PrintCollection(Var.Countries, "pays")


    # methods to get type name
    # method 1 : use INNER JOIN
    # MyQuery = (
    #     "SELECT animal.id, animal.name, type.name " +
    #     "FROM animal " +
    #     "INNER JOIN type ON type.id = animal.id_type " +
    #     "ORDER BY animal.name")
    # MyResult = ExecuteQuery(MyConnection, MyQuery)

    # method 2 : use additional query in animal
    # see comments in Animal model

    # method 3 : create and use collection of Types
    # see model Type



    # close resources
    MyConnection.close()


# code entry point
if __name__ == "__main__":
    Main()