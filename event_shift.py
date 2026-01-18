from DB_Connection import shifts
from datetime import datetime, timedelta


def is_datetime_in_shift(production_datetime, shift):
    """
    shift = {
        'Shift_Id': int,
        'Start_time': datetime.time,
        'End_time': datetime.time
    }
    """
    shift_date = production_datetime.date()

    shift_start = datetime.combine(shift_date, shift['Start_time'])
    shift_end = datetime.combine(shift_date, shift['End_time'])

    if shift_end <= shift_start:
        shift_end += timedelta(days=1)

        if production_datetime.time() < shift['End_time']:
            shift_start -= timedelta(days=1)

    return shift_start <= production_datetime <= shift_end
