# coding: utf-8

# import modules
import psycopg2

# functions
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
    Values = None,
    MustCommit = False,
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
        MyCursor.execute(MyQuery, Values)
        if not MustCommit:
            # get result
            MyResult = MyCursor.fetchall()
        else:
            # commit to DB
            MyConnection.commit()
        # close cursor
        MyCursor.close()

    if CloseConnection:
        # close resources if specified
        MyConnection.close()

    return MyResult
