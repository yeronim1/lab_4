from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import trackers_controller
from lab4.app.my_project.auth.domain import Trackers

trackers_bp = Blueprint('trackers', __name__, url_prefix='/trackers')


@trackers_bp.get('')
def get_all_trackers() -> Response:
    return make_response(jsonify(trackers_controller.find_all()), HTTPStatus.OK)


@trackers_bp.post('')
def create_trackers() -> Response:
    content = request.get_json()
    trackers = Trackers.create_from_dto(content)
    trackers_controller.create(trackers)
    return make_response(jsonify(trackers.put_into_dto()), HTTPStatus.CREATED)


@trackers_bp.get('/<int:trackers_id>')
def get_trackers(trackers_id: int) -> Response:
    return make_response(jsonify(trackers_controller.find_by_id(trackers_id)), HTTPStatus.OK)


@trackers_bp.put('/<int:trackers_id>')
def update_trackers(trackers_id: int) -> Response:
    content = request.get_json()
    trackers = Trackers.create_from_dto(content)
    trackers_controller.update(trackers_id, trackers)
    return make_response("Trackers updated", HTTPStatus.OK)


@trackers_bp.patch('/<int:trackers_id>')
def patch_trackers(trackers_id: int) -> Response:
    content = request.get_json()
    trackers_controller.patch(trackers_id, content)
    return make_response("Trackers updated", HTTPStatus.OK)


@trackers_bp.delete('/<int:trackers_id>')
def delete_trackers(trackers_id: int) -> Response:
    trackers_controller.delete(trackers_id)
    return make_response("Trackers deleted", HTTPStatus.OK)


