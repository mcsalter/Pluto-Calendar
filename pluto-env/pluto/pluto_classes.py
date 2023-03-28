##--------------------------------------
## Pluto Calendar classes module
## Written by mcsalter
##--------------------------------------

from dataclasses import dataclass, fields
import socket
import icalendar

event_completion_enum = ["not started", "in progress" , "complete"]
event_status_enum = ["has due date", "backlog", "compelete"]

@dataclass(frozen = True)
class config_information:
    sqlite3_initialized: bool = False
    sqlite3_file_name: str = "pluto_sql.db"
    respect_XDG: bool = True
    default_socket: str = "AF_INET"
    default_socket_name: str = "120.0.1.1"
    default_socket_address: int = 12000

@dataclass(order = True)
class pluto_event:
    ## pluto event class
    ## the information about the specific event
    ## having a `child_event_id` means that an event has subtasks that must be completed
    ## having a c_e_i of 0 means that it has no child events
    event_id: int
    child_event_id: int
    calendar_data: icalendar.Calendar
    event_status: enumerate
    event_completion: enumerate
    notes: str
    edited: bool = True

@dataclass
class event_list:
    event_type: enumerate
    list_of_events: list[pluto_event]

@dataclass
class Board:
    ## The board objects will have the list of main level tasks, which then can
    ## populate subtasks when looking at said tasks
    name: str
    list_of_tasks: list[pluto_event]
    completion_status: enumerate
    notes: str
    edited: bool = True

@dataclass
class Pluto:
    pluto_config: config_information

    list_of_due_date_events: event_list
    list_of_backlog_events: event_list
    list_of_completed_events: event_list

    list_of_boards: list[Board]


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
##
## Pluto
## |--pluto_config
## |  |--sqlite_configuration_status
## |  |--sqlite_file_name


# script taken from stackoverflow to generate a
def class_from_dict(className, argDict: dict):
        fieldSet = {f.name for f in fields(className) if f.init}
        filteredArgDict = {k : v for k, v in argDict.items() if k in fieldSet}
        return className(**filteredArgDict)
