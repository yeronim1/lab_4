from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import medications_controller
from lab4.app.my_project.auth.domain import Medications

medications_bp = Blueprint('medications', __name__, url_prefix='/medications')


@medications_bp.get('')
def get_all_medications() -> Response:
    return make_response(jsonify(medications_controller.find_all()), HTTPStatus.OK)


@medications_bp.post('')
def create_medications() -> Response:
    content = request.get_json()
    medications = Medications.create_from_dto(content)
    medications_controller.create(medications)
    return make_response(jsonify(medications.put_into_dto()), HTTPStatus.CREATED)


@medications_bp.get('/<int:medications_id>')
def get_medications(medications_id: int) -> Response:
    return make_response(jsonify(medications_controller.find_by_id(medications_id)), HTTPStatus.OK)


@medications_bp.put('/<int:medications_id>')
def update_medications(medications_id: int) -> Response:
    content = request.get_json()
    medications = Medications.create_from_dto(content)
    medications_controller.update(medications_id, medications)
    return make_response("Medications updated", HTTPStatus.OK)


@medications_bp.patch('/<int:medications_id>')
def patch_medications(medications_id: int) -> Response:
    content = request.get_json()
    medications_controller.patch(medications_id, content)
    return make_response("Medications updated", HTTPStatus.OK)


@medications_bp.delete('/<int:medications_id>')
def delete_medications(medications_id: int) -> Response:
    medications_controller.delete(medications_id)
    return make_response("Medications deleted", HTTPStatus.OK)
