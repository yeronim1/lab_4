from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import consultations_controller
from lab4.app.my_project.auth.domain import Consultations

consultations_bp = Blueprint('consultations', __name__, url_prefix='/consultations')


@consultations_bp.get('')
def get_all_consultations() -> Response:
    return make_response(jsonify(consultations_controller.find_all()), HTTPStatus.OK)


@consultations_bp.post('')
def create_consultations() -> Response:
    content = request.get_json()
    consultations = Consultations.create_from_dto(content)
    consultations_controller.create(consultations)
    return make_response(jsonify(consultations.put_into_dto()), HTTPStatus.CREATED)


@consultations_bp.get('/<int:consultations_id>')
def get_consultations(consultations_id: int) -> Response:
    return make_response(jsonify(consultations_controller.find_by_id(consultations_id)), HTTPStatus.OK)


@consultations_bp.put('/<int:consultations_id>')
def update_consultations(consultations_id: int) -> Response:
    content = request.get_json()
    consultations = Consultations.create_from_dto(content)
    consultations_controller.update(consultations_id, consultations)
    return make_response("Consultations updated", HTTPStatus.OK)


@consultations_bp.patch('/<int:consultations_id>')
def patch_consultations(consultations_id: int) -> Response:
    content = request.get_json()
    consultations_controller.patch(consultations_id, content)
    return make_response("Consultations updated", HTTPStatus.OK)


@consultations_bp.delete('/<int:consultations_id>')
def delete_consultations(consultations_id: int) -> Response:
    consultations_controller.delete(consultations_id)
    return make_response("Consultations deleted", HTTPStatus.OK)


@consultations_bp.get('/get-consultations-after-patient/<int:patient_id>')
def get_consultations_after_patient(patient_id: int) -> Response:
    return make_response(jsonify(consultations_controller.get_consultations_after_patient(patient_id)), HTTPStatus.OK)


@consultations_bp.get('/get-consultations-after-doctor/<int:doctor_id>')
def get_consultations_after_doctor(doctor_id: int) -> Response:
    return make_response(jsonify(consultations_controller.get_consultations_after_doctor(doctor_id)), HTTPStatus.OK)
