from flask import render_template, request
from app import app
from models.eventslist import events, add_new_event, remove_event_in_list
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/events', methods=["POST"])
def add_event():
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    event_guests = request.form["event_guests"]
    event_location= request.form["event_location"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, False)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

@app.route('/events/delete/<event_name>')
def remove_event(event_name):
    remove_event_in_list(event_name)
    return render_template('index.html', title="Home", events=events)