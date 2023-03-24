import typing
import sqlite3

import pluto_classes

def initialize_sqlite3() -> bool:
    return False

def

def file_load(filename: str) -> typing.Tuple[event_list, list[Board]]:
    """
    Loads a data file, and extracts the content into the appropriate lists.
    @param filename : str                    -- name of file to load
    @returns        : (event_list, [boards]) -- the boards and events generated
    """

    boardlist = []

    tmp = event_list(edited = False)
    return (tmp, boardlist)

def file_save(filename: str, pluto: Pluto) -> typing.Tuple[bool, str]:
    """
    Writes the current events to a specific data file. Currently planned to be using s-expressions.
    @param filename : str                       -- name of file to be saved to.
    @param type     : (event_list, list[board]) -- the items to save to the file. will recurse through them looking for edited/new objects.
    @returns        : (bool, str)               -- true for save success, false for save fail -- str for failure message.
    """
    # code to find only the events that have been edited
    with file as open(filename, "r+"):
        # code to append && edit existing events
    return
