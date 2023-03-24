# Pluto Calendar and Sun Interface

Pluto: A calendar project made for learning how to use API and Sockets. This will be written in Ruby.
Sun : A project to make a useful and customizable interface for the user. It is unknown what this will be written in yet.


_Table of Contents_
* [How it works](# Current Design)
* [Installation and Usage](# Installation and Usage)
  * [Dependencies](## Dependencies)
* [Configuration Guide](# Configuration)

# Current Design

Pluto is the back end project that manages the calendar databases.
- Pluto connects to a network socket (for now, socket 12000).
  - FUTURE: support for unix sockets and the customization of which is being used.
- Pluto loads and manages the various XML files containing the calendar events.
  - To be decided if this is just XML files or another database).
  - currently looking towards SQL and MongoDB
- Pluto will send to the gui software alerts that a notification should be sent.
- Pluto will have to provide security mechanisms so that multiple users can use, but not access each others calendar information.
  - Would be nice to not have to worry about multiple users, but if one instance of Pluto is running, how will the gui tell which instance to connect to?
- Pluto will have 3 main lists of tasks available, each stored in a separate file:
  - Deadline  -- tasks that have an upcoming date attached to them, or have not been marked completed.
  - Backlog   -- tasks that are not set for a specific date.
  - Archived  -- tasks that have been marked as completed. On the first of each month, these will be archived to a new file.


Sun will be the primary gui project for Pluto, Though anyone should be able to make their own gui interface. This should be as system agnostic as possible.
- Sun will connect to network socket and request calendar information from Pluto, as well as provide new data for Pluto.
- Sun will handle import/export of events, and transmit the data to Pluto to inset to the list.
- Sun will have 4 display modes:
  - Weekly calendar view.
  - Kanban/Board view (showing nested tasks and tasks following a certain chain).
  - Backlog tasks   -- tasks that are not set to be due on a specific date.
  - Everything view -- two columns, listing by date the events as well as the backlog events. (maybe show a line connecting parent/child events?).
- Sun will handle sending notifications to the system.
- Sun can import/export icalendar version 2.0 events.
- Sun will handle further import/export functionalities as they get requested.
- Settings will allow customizability of several things:
  - Color schemes.
  - What day the week starts on (default Saturday).



The databases are split in 3: dated events, backlog, and completed.

# Installation and Usage

## Dependencies
iCalendar

# Configuration
