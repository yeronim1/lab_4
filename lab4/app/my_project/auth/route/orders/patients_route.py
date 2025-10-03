from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patients_controller
from lab4.app.my_project.auth.domain import Patients

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')


@patients_bp.get('')
def get_all_patients() -> Response:
    return make_response(jsonify(patients_controller.find_all()), HTTPStatus.OK)


@patients_bp.post('')
def create_patients() -> Response:
    content = request.get_json()
    patients = Patients.create_from_dto(content)
    patients_controller.create(patients)
    return make_response(jsonify(patients.put_into_dto()), HTTPStatus.CREATED)


@patients_bp.get('/<int:patients_id>')
def get_patients(patients_id: int) -> Response:
    return make_response(jsonify(patients_controller.find_by_id(patients_id)), HTTPStatus.OK)


@patients_bp.put('/<int:patients_id>')
def update_patients(patients_id: int) -> Response:
    content = request.get_json()
    patients = Patients.create_from_dto(content)
    patients_controller.update(patients_id, patients)
    return make_response("Patients updated", HTTPStatus.OK)


@patients_bp.patch('/<int:patients_id>')
def patch_patients(patients_id: int) -> Response:
    content = request.get_json()
    patients_controller.patch(patients_id, content)
    return make_response("Patients updated", HTTPStatus.OK)


@patients_bp.delete('/<int:patients_id>')
def delete_patients(patients_id: int) -> Response:
    patients_controller.delete(patients_id)
    return make_response("Patients deleted", HTTPStatus.OK)


@patients_bp.get('/get-patients-after-hospital/<int:hospital_id>')
def get_patients_after_hospital(hospital_id: int) -> Response:
    return make_response(jsonify(patients_controller.get_patients_after_hospital(hospital_id)), HTTPStatus.OK)
