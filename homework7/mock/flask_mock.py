#!/usr/bin/env python3.9

import threading
import json
import requests

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

app_data = {}
SURNAME_DATA = {}
user_id_seq = 1


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


@app.route('/change_surname', methods=['PUT'])
def change_user_surname():
    name = json.loads(request.data)['name']
    if app_data.get(name):
        new_surname = json.loads(request.data)['new_surname']
        SURNAME_DATA[name] = new_surname
        data = {'name': name, 'surname': new_surname}
        return jsonify(data), 200
    else:
        return jsonify(f'user {name} does not exist'), 404


@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    name = json.loads(request.data)['name']
    if app_data.get(name):
        del app_data[name]
        del SURNAME_DATA[name]
        return jsonify(f'User {name} was deleted successfully'), 200
    else:
        return jsonify(f'User {name} does not exist'), 404


@app.route('/get_user/<name>', methods=['GET'])
def get_user_id_by_name(name):
    if user_id := app_data.get(name):
        surname = None

        response = requests.get(
            f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/get_user_surname/{name}')
        if response.status_code == 200:
            surname = response.json()
        else:
            print(f'No surname found for user {name}')

        data = {'user_id': user_id,
                'surname': surname
                }

        return jsonify(data), 200
    else:
        return jsonify(f'User_name {name} not found'), 404


@app.route('/add_user', methods=['POST'])
def create_user():
    global user_id_seq
    user_name = json.loads(request.data)["name"]
    # user_surname = json.loads(request.data)['surname']
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        # SURNAME_DATA[user_name] = user_surname
        user_id_seq += 1
        return jsonify({'user_id': app_data[user_name]}), 201

    else:
        return jsonify(f'User_name {user_name} already exists: id: {app_data[user_name]}'), 400


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server
