##--------------------------------------
## Pluto Calendar
## Written by mcsalter
##--------------------------------------

import typing
import icalendar
import atexit
import yaml
import os

import pluto_classes
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
    #pluto_sqlite.file_save()

def load_config() -> pluto_classes.Pluto:

    config_file_name: str = "./pluto.yaml"
    Pluto = pluto_classes.Pluto
    # check if the default config file exists
    # it should exist in the same directory as pluto for now
    # TODO: set up Pluto to load the config from $XDG_CONFIG_HOME (and set sane settings if X_C_H is not set)
    os.path.exists(config_file_name)

    # load the yaml file into a dict
    with open(config_file_name, 'r') as config_file:
        data: dict = list(yaml.load_all(config_file, Loader=yaml.loader.SafeLoader))[0]

    # generate the pluto config object
    config:pluto_classes.pluto_config = pluto_classes.class_from_dict(pluto_classes.config_information, data)

    Pluto.pluto_config = config
    return Pluto

def main() -> int:
    """ """
    Pluto = load_config()
    return

atexit.register(save_on_quit)

if __name__ == "__main__":
    main()
