from dataclasses import dataclass
import socket

event_completion_enum = ["not started", "in progress" , "complete"]
event_status_enum = ["has due date", "backlog", "compelete"]

@dataclass
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
    list_of_due_date_events: event_list
    list_of_backlog_events: event_list
    list_of_completed_events: event_list

    list_of_boards: list[Board]


@dataclass
class config_information:
    sqlite3_initialized: bool = False
    sqlite3_file_name: str = "pluto_sql.db"
    default_socket: socket.AddressFamily = socket.IF_INET
    default_socket_address: int = 12000
