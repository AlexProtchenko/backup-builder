import os

from flask import Blueprint, jsonify

builder_service = Blueprint("api-builder", __name__)


@builder_service.route('/build', methods=['GET'])
def build():
    os.system("./../../build.sh")
    return jsonify("started")
