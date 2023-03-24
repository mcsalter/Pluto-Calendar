##--------------------------------------
## Pluto Calendar
## Written by mcsalter
##--------------------------------------

## Layout of how objects should be:
## Board
## |--name = ...
## |--event
## |--event [id = xyz, child_event_id = [yza, zab]]
## |  |--event [id = yza, ...]
## |  |--event [id = zab, child_event_id = abc, ...]
## |     |--event [id = abc, ...]
## |--status = ...
## |--notes = ...
##
## Event
## |--event_id = ...
## |--children_event_id = [...]
## |--calendar_data [...]
## |--event_status
## |--event_completion
## |--notes
## |--edited


import typing
import icalendar
import atexit

import pluto_socket
import pluto_sqlite


def import_ics():
    """ """
    return

def import_ical():
    """ """
    return

def export_ical():
    """ """
    return

def save_on_quit():
    """
    writes all items to database in preparation to quit.
    """
    pluto_sqlite.file_save()

def load_config():
    return

def main() -> int:
    """ """
    return

atexit.register(save_on_quit)

if __name__ == "__main__":
    main()
