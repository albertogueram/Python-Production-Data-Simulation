# Production Log - Data Simulation ##
import pyodbc


def connect():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CDN63N6Q\\SQLEXPRESS;"
        "DATABASE=Dexion_Laubach_Database;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    return cursor


def machines():
    cursor = connect()
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
    cursor = connect()
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
    cursor = connect()
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


def write_db(machine_id, production_datetime, shift_id, operator_id,
             good_units, bad_units, cycle, temperature, energy):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CDN63N6Q\\SQLEXPRESS;"
        "DATABASE=Dexion_Laubach_Database;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Production_log (
            Machine_id,
            Production_datetime,
            Shift_id,
            Operator_id,
            Good_units,
            Bad_units,
            Cycle_time_ms,
            Temperature_c,
            Energy_kwh
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, machine_id, production_datetime, shift_id, operator_id,
                   good_units, bad_units, cycle, temperature, energy)

    conn.commit()
    conn.close()
