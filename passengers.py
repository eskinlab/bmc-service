# passengers.py

from flask import abort, make_response
import pandas as pd
import json

DATA = pd.read_csv('titanic.csv')


# Get the list of all passengers
def get_all_passengers():
    passengers = DATA.to_dict(orient='records')
    return passengers


# Get passenger data by PassengerId
def get_passenger(passenger_id):
    passenger = DATA[DATA['PassengerId'] == passenger_id].to_dict(orient='records')
    return passenger


# Get requested attribute list from passenger data by PassengerId
def get_passenger_attributes(passenger_id, attributes):
    passenger = DATA[DATA['PassengerId'] == passenger_id][attributes].to_dict(orient='records')
    return passenger

