from datetime import date


class Event():

    def __init__(self,date,event_name,guests,location,description,recurring):
        self.date = date
        self.event_name=event_name
        self.guests=guests
        self.location=location
        self.description=description
        self.recurring=recurring