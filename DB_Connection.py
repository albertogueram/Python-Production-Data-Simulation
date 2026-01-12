## Production Log - Data Simulation ##
import pyodbc

def machines():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CDN63N6Q\\SQLEXPRESS;"
        "DATABASE=Dexion_Laubach_Database;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Machines")

    machine_dict = {}
    columns = [
        "Machine_Id",
        "Line_Id",
        "Machine_Name",
        "Model",
        "Location",
        "Year_Installed"
    ]
    for index, row in enumerate(cursor.fetchall()):
        machine = dict(zip(columns, row))
        machine_dict[index] = machine

    return machine_dict


def shifts():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CDN63N6Q\\SQLEXPRESS;"
        "DATABASE=Dexion_Laubach_Database;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Shift")

    shift_dict = {}
    columns = [
        "Shift_Id",
        "Shift_Name",
        "Start_time",
        "End_time"
    ]
    for index, row in enumerate(cursor.fetchall()):
        shift = dict(zip(columns, row))
        shift_dict[index] = shift

    return shift_dict


def operators():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CDN63N6Q\\SQLEXPRESS;"
        "DATABASE=Dexion_Laubach_Database;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Operators")

    operators_dict = {}
    columns = [
        "Operator_id",
        "Operator_name"
    ]

    for index, row in enumerate(cursor.fetchall()):
        operator = dict(zip(columns, row))
        operators_dict[index] = operator

    return operators_dict
