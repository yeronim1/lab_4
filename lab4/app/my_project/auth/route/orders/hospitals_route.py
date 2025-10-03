from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import hospitals_controller
from lab4.app.my_project.auth.domain import Hospitals

hospitals_bp = Blueprint('hospitals', __name__, url_prefix='/hospitals')


@hospitals_bp.get('')
def get_all_hospitals() -> Response:
    return make_response(jsonify(hospitals_controller.find_all()), HTTPStatus.OK)


@hospitals_bp.post('')
def create_hospitals() -> Response:
    content = request.get_json()
    hospitals = Hospitals.create_from_dto(content)
    hospitals_controller.create(hospitals)
    return make_response(jsonify(hospitals.put_into_dto()), HTTPStatus.CREATED)


@hospitals_bp.get('/<int:hospitals_id>')
def get_hospitals(hospitals_id: int) -> Response:
    return make_response(jsonify(hospitals_controller.find_by_id(hospitals_id)), HTTPStatus.OK)


@hospitals_bp.put('/<int:hospitals_id>')
def update_hospitals(hospitals_id: int) -> Response:
    content = request.get_json()
    hospitals = Hospitals.create_from_dto(content)
    hospitals_controller.update(hospitals_id, hospitals)
    return make_response("Hospitals updated", HTTPStatus.OK)


@hospitals_bp.patch('/<int:hospitals_id>')
def patch_hospitals(hospitals_id: int) -> Response:
    content = request.get_json()
    hospitals_controller.patch(hospitals_id, content)
    return make_response("Hospitals updated", HTTPStatus.OK)


@hospitals_bp.delete('/<int:hospitals_id>')
def delete_hospitals(hospitals_id: int) -> Response:
    hospitals_controller.delete(hospitals_id)
    return make_response("Hospitals deleted", HTTPStatus.OK)


