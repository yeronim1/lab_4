from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import doctors_controller
from lab4.app.my_project.auth.domain import Doctors

doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')


@doctors_bp.get('')
def get_all_doctors() -> Response:
    return make_response(jsonify(doctors_controller.find_all()), HTTPStatus.OK)


@doctors_bp.post('')
def create_doctors() -> Response:
    content = request.get_json()
    doctors = Doctors.create_from_dto(content)
    doctors_controller.create(doctors)
    return make_response(jsonify(doctors.put_into_dto()), HTTPStatus.CREATED)


@doctors_bp.get('/<int:doctors_id>')
def get_doctors(doctors_id: int) -> Response:
    return make_response(jsonify(doctors_controller.find_by_id(doctors_id)), HTTPStatus.OK)


@doctors_bp.put('/<int:doctors_id>')
def update_doctors(doctors_id: int) -> Response:
    content = request.get_json()
    doctors = Doctors.create_from_dto(content)
    doctors_controller.update(doctors_id, doctors)
    return make_response("Doctors updated", HTTPStatus.OK)


@doctors_bp.patch('/<int:doctors_id>')
def patch_doctors(doctors_id: int) -> Response:
    content = request.get_json()
    doctors_controller.patch(doctors_id, content)
    return make_response("Doctors updated", HTTPStatus.OK)


@doctors_bp.delete('/<int:doctors_id>')
def delete_doctors(doctors_id: int) -> Response:
    doctors_controller.delete(doctors_id)
    return make_response("Doctors deleted", HTTPStatus.OK)


@doctors_bp.get("/get-doctors-after-hospital/<int:hospital_id>")
def get_doctors_after_hospital(hospital_id: int) -> Response:
    return make_response(jsonify(doctors_controller.get_doctors_after_hospital(hospital_id)), HTTPStatus.OK)
