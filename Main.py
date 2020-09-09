# coding: utf-8

import psycopg2

import Variables as Var
from Models.Animal import Animal
from Models.Type import Type
from Models.contact import Contact


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
            password="Formation2020-at"
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
        Var.animals = []
        print (f'\nliste animal vide : {Var.animals}') # ! to delete !!!!!
    
    # create Animals collection
    for MyAnimal in MyResult:
        # print(f"({Animal[0]}) {Animal[1]} - {Animal[2]}")
        # add an new instance of animal to Animals (collection of animals)
        # this means each line in animal table (DB)
        #    equals one instance of animal class 
        Var.animals.append(
            Animal(
                MyAnimal[0], 
                MyAnimal[1], 
                MyAnimal[2]))
    print (f'\nliste animal remplie : {Var.animals}') # ! to delete !!!!!
    
def CreateTypeCollection(
    MyResult,
    ResetCollection = True):
    """
        Create Types collection from query result
        and return collection
    """
    if ResetCollection:
        Var.types = []
    
    # create Animals collection
    for MyType in MyResult:
        Var.types.append(
            Type(
                MyType[0], 
                MyType[1], 
                MyType[2]))

def create_collection(MyResult, liste_table, ResetCollection = True):
    """
            Create a collection from query result
            and return collection
        """
    if ResetCollection:
        liste_table = []
        print(f'liste vide : {liste_table}')

    print(f'my result : {MyResult}')

    # create collection
    for my_value in MyResult:
        liste_table.append(
            Contact(
                my_value[0],
                my_value[1]))
    print(f'liste remplie : {liste_table}')

    return liste_table



def PrintAnimalCollection():
    """ 
        print Animals
    """    
    # print collection

    print(f"\n Liste des animaux :")
    for MyAnimal in Var.animals:
        print(f'\ntype : {MyAnimal.type}')   #! to delete !!!!!!
        print(f"\n({MyAnimal.id}) {MyAnimal.name} - {MyAnimal.type} ({MyAnimal.id_type})")

def PrintTypeCollection():
    """
        Print Types
    """
    # print collection
    print(f"\n Liste des types d'animaux :")
    for MyType in Var.types:
        print(f"({MyType.id}) {MyType.name} - {MyType.id_parent}")

def print_collection(collection):
    """
        Print collection
    """
    # print collection
    print(f'liste var.contacts : {collection}')
    print(f"\ liste -- nom de la table -- ici contacts : ")
    for my_value in Var.contacts:
        for index in range(len(Var.contacts)):
            print(f"({my_value[index][0]}) {my_value[index][1]}")


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

    # # execute query
    # MyQuery = (
    #     "SELECT * " +
    #     "FROM type")
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # create Types collection
    # CreateTypeCollection(MyResult)
    # # print collection
    # PrintTypeCollection()
    #
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

    # execute create and print collection
    MyQuery = ( "SELECT * FROM contact" )
    MyResult = ExecuteQuery(MyConnection, MyQuery)
    # create collection
    collection = create_collection(MyResult, Var.contacts)
    # print collection
    print_collection(collection)


    # close resources
    MyConnection.close()


# code entry point
if __name__ == "__main__":
    Main()