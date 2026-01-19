from DB_Connection import machines, shifts, operators, write_db
from event_shift import is_datetime_in_shift
from datetime import datetime
import random

# Get information from linked tables
machines = machines()
shifts = shifts()
operators = operators()

n_logs = int(input("Introduce number of logs to introduce in database: "))

while n_logs > 0:
    m = random.choice(machines)
    o = random.choice(operators)

    # Get current date & time
    production_datetime = datetime.now().replace(microsecond=0)

    # Assign proper shift id according to current time
    for shift in shifts.values():
        if is_datetime_in_shift(production_datetime, shift):
            s = shift
            break

    # Random values for Temperature, Energy, Good & Bad Units & Cycle time
    temperature = round(random.uniform(0, 100), 2)
    energy = random.randint(0, 1000)
    cycle = random.randint(1, 999)
    good_units = random.randint(50, 299)
    scrap = random.randint(1, 10)
    bad_units = round(good_units*scrap/100)

    # Insert new data in Production_Log table
    write_db(m['Machine_Id'], production_datetime, s['Shift_Id'], o['Operator_id'],
             good_units, bad_units, cycle, temperature, energy)

    n_logs -= 1
