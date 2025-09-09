#!/usr/bin/env python
"""
mascot: a microservice for serving mascot data
"""
import json
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

# Load mascot data from file
with open('data.json', 'r') as f:
    mascots = json.load(f)


@app.route('/', methods=['GET'])
def get_mascots():
    """
    Returns a list of mascot objects
    """
    return jsonify(mascots)


@app.route('/<guid>', methods=['GET'])
def get_mascot(guid):
    """
    Returns the mascot object with the given GUID
    """
    mascot = next((m for m in mascots if m.get('guid') == guid), None)
    if mascot:
        return jsonify(mascot)
    abort(404)


@app.errorhandler(404)
def not_found(error):
    """
    Returns HTTP 404 with error message
    """
    return make_response(jsonify({'error': str(error)}), 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
