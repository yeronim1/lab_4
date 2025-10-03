from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patient_medications_controller
from lab4.app.my_project.auth.domain import PatientMedications

patient_medications_bp = Blueprint('patient_medications', __name__, url_prefix='/patient-medications')


@patient_medications_bp.get('')
def get_all_patient_medications() -> Response:
    return make_response(jsonify(patient_medications_controller.find_all()), HTTPStatus.OK)


@patient_medications_bp.post('')
def create_patient_medications() -> Response:
    content = request.get_json()
    patient_medications = PatientMedications.create_from_dto(content)
    patient_medications_controller.create(patient_medications)
    return make_response(jsonify(patient_medications.put_into_dto()), HTTPStatus.CREATED)


@patient_medications_bp.get('/<int:patient_medications_id>')
def get_patient_medications(patient_medications_id: int) -> Response:
    return make_response(jsonify(patient_medications_controller.find_by_id(patient_medications_id)), HTTPStatus.OK)


@patient_medications_bp.put('/<int:patient_medications_id>')
def update_patient_medications(patient_medications_id: int) -> Response:
    content = request.get_json()
    patient_medications = PatientMedications.create_from_dto(content)
    patient_medications_controller.update(patient_medications_id, patient_medications)
    return make_response("PatientMedications updated", HTTPStatus.OK)


@patient_medications_bp.patch('/<int:patient_medications_id>')
def patch_patient_medications(patient_medications_id: int) -> Response:
    content = request.get_json()
    patient_medications_controller.patch(patient_medications_id, content)
    return make_response("PatientMedications updated", HTTPStatus.OK)


@patient_medications_bp.delete('/<int:patient_medications_id>')
def delete_patient_medications(patient_medications_id: int) -> Response:
    patient_medications_controller.delete(patient_medications_id)
    return make_response("PatientMedications deleted", HTTPStatus.OK)


@patient_medications_bp.get('/get-patients-after-medication/<int:medication_id>')
def get_patients_after_medication(medication_id: int) -> Response:
    return make_response(jsonify(patient_medications_controller.get_patients_after_medication(medication_id)),
                         HTTPStatus.OK)


@patient_medications_bp.get('/get-medications-after-patient/<int:patient_id>')
def get_medications_after_patient(patient_id: int) -> Response:
    return make_response(jsonify(patient_medications_controller.get_medications_after_patient(patient_id)),
                         HTTPStatus.OK)
