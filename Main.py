# coding: utf-8

import psycopg2

import Variables as Var
from Models.Animal import Animal
from Models.Type import Type


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

def CreateAnimalCollection(
    MyResult,
    ResetCollection = True):
    """
        Create Animals collection from query result
    """
    if ResetCollection:
        Var.Animals = []
    
    # create Animals collection
    for MyAnimal in MyResult:
        # print(f"({Animal[0]}) {Animal[1]} - {Animal[2]}")
        # add an new instance of animal to Animals (collection of animals)
        # this means each line in animal table (DB)
        #    equals one instance of animal class 
        Var.Animals.append(
            Animal(
                MyAnimal[0], 
                MyAnimal[1], 
                MyAnimal[2]))
    
def CreateTypeCollection(
    MyResult,
    ResetCollection = True):
    """
        Create Types collection from query result
        and return collection
    """
    if ResetCollection:
        Var.Types = []
    
    # create Animals collection
    for MyType in MyResult:
        Var.Types.append(
            Type(
                MyType[0], 
                MyType[1], 
                MyType[2]))

def PrintAnimalCollection():
    """ 
        print Animals
    """    
    # print collection
    print(f"\n Liste des animaux :")
    for MyAnimal in Var.Animals:
        print(f"({MyAnimal.id}) {MyAnimal.name} - {MyAnimal.type} ({MyAnimal.id_type})")

def PrintTypeCollection():
    """
        Print Types
    """
    # print collection
    print(f"\n Liste des types d'animaux :")
    for MyType in Var.Types:
        print(f"({MyType.id}) {MyType.name} - {MyType.id_parent}")


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
    CreateTypeCollection(MyResult)
    # print collection
    PrintTypeCollection()

    # execute query
    MyQuery = (
        "SELECT * " +
        "FROM animal " +
        "ORDER BY animal.name")
    MyResult = ExecuteQuery(MyConnection, MyQuery)
    # print query result
    # print(f"\n Résultat de la requête : {MyResult}")
    # create Animals collection
    CreateAnimalCollection(MyResult)
    # print collection
    PrintAnimalCollection()
    
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