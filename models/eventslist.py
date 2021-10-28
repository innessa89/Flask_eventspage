from models.event import *


event1 = Event("2021-10-28", "Halloween", 13, "CodeClan", "A Spooky Spectacle",False)
event2 = Event("2021-12-25", "Christmas", 8, "Home", "A Jolly Jolly Time", True)
events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_event_in_list(event_name):
    for event in events:
        if event_name.upper() == event.event_name.upper():
            events.remove(event)