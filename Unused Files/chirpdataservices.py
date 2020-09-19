from enums import *
from user import User
from event import Event
from datetime import datetime, timedelta
import mysql.connector
import json

def create_connection():
    with open("configsettings.json", 'r') as config_file:
        config_settings= json.loads(config_file.read())
    cnx = mysql.connector.connect(user=config_settings['user'], password=config_settings['password'], 
    host=config_settings['host'], database=config_settings['database'], port=config_settings['port'])

    return cnx

def create_user(user):
    userCnx = create_connection()
    
    cursor = userCnx.cursor()
    
    reliability_score = 100 # need to sub this out
    create_user = "INSERT INTO Users (username, phone_number, reliability_score, base_latitude, base_longitude, preferences) \
        VALUES (\'" + user.name + "\'," + str(user.number) + "," + str(reliability_score) + "," + str(user.baseLocation[0]) \
            + "," + str(user.baseLocation[1]) + ");"

    cursor.execute(create_user)
    
    userCnx.commit()
    userCnx.close()

    return  "User " + str(user) + " created successfully."

def get_user(user_id):
    userCnx = create_connection()
    cursor = userCnx.create_connection()

    get_users = "SELECT * FROM Users WHERE user_id = " + user_id + ";" 

    cursor.execute(get_users)

    for (user_id, username, phone_number, reliability_score, base_latitude, base_longitude) in cursor:
        newUser = User(user_id, username, phone_number, reliability_score, [base_latitude, base_longitude])
    
    userCnx.close()
    return newUser

def create_event(event):
    eventCnx = create_connection()
    cursor = eventCnx.cursor()
    
    create_event = "INSERT INTO Events (headline, description, timestamp, event_type, latitude, longitude) \
        VALUES (\'" + event.headline + "\',\'" + event.description + "\',\'" + event.time + "\'," + \
            str(event.eventType) + "," + str(event.location[0]) + "," + str(event.location[1]) + ");"

    cursor.execute(create_event)
    
    eventCnx.commit()
    eventCnx.close()
   
    return  "Event " + str(event) + " created successfully."

def get_events():
    eventCnx = create_connection();
    cursor = eventCnx.cursor()
    
    last_hour_timestamp = str(datetime.now() - timedelta(hours=1))[:-7] # slicing removes milliseconds

    get_event = "SELECT * FROM Events WHERE timestamp >= " + "\'" + last_hour_timestamp + "\;'"
    cursor.execute(get_event)

    events = []
    for (event_id, headline, description, timestamp, event_type, latitude, longitude) in cursor:
        newEvent = Event(event_id, headline, description, timestamp, event_type, [latitude, longitude])
        events.append(newEvent)
    
    eventCnx.close()
    
    return events

def create_verification(event_id, user_id, verified):
    verificationCnx = create_connection()
    cursor = verificationCnx.cursor()

    create_verification = "INSERT INTO Verifications (event_id, user_id, verified) VALUES (" + str(event_id) + ", " \
        + str(user_id) + ", " +  str(verified) + ");"
    
    cursor.execute(create_verification)
    
    verificationCnx.commit()
    verificationCnx.close()

    return "Verification for event " + str(event_id) + " created successfully"