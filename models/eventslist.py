from models.event import *


event1 = Event("28/10/2021", "Halloween", 13, "CodeClan", "A Spooky Spectacle",False)
event2 = Event("25/12/2021", "Christmas", 8, "Home", "A Jolly Jolly Time", True)
events = [event1, event2]

def add_new_event(event):
    events.append(event)