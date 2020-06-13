from flask import jsonify

'''
There are two response builders to have a common response formatting across the api
'''


def response_builder(message, data, status_code):
    resp = {
        'status_code': status_code,
        'message': message,
        'loc': data,
    }
    return jsonify(resp)


def error_response_builder(message, status_code):
    resp = {
        'status_code': status_code,
        'message': message,
    }
    return jsonify(resp)
