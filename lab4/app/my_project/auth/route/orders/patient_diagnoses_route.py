from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patient_diagnoses_controller
from lab4.app.my_project.auth.domain import PatientTrackers

patient_diagnoses_bp = Blueprint('patient_diagnoses', __name__, url_prefix='/patient-diagnoses')


@patient_diagnoses_bp.get('')
def get_all_patient_diagnoses() -> Response:
    return make_response(jsonify(patient_diagnoses_controller.find_all()), HTTPStatus.OK)


@patient_diagnoses_bp.post('')
def create_patient_diagnoses() -> Response:
    content = request.get_json()
    patient_diagnoses = PatientTrackers.create_from_dto(content)
    patient_diagnoses_controller.create(patient_diagnoses)
    return make_response(jsonify(patient_diagnoses.put_into_dto()), HTTPStatus.CREATED)


@patient_diagnoses_bp.get('/<int:patient_diagnoses_id>')
def get_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    return make_response(jsonify(patient_diagnoses_controller.find_by_id(patient_diagnoses_id)), HTTPStatus.OK)


@patient_diagnoses_bp.put('/<int:patient_diagnoses_id>')
def update_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    content = request.get_json()
    patient_diagnoses = PatientTrackers.create_from_dto(content)
    patient_diagnoses_controller.update(patient_diagnoses_id, patient_diagnoses)
    return make_response("PatientTrackers updated", HTTPStatus.OK)


@patient_diagnoses_bp.patch('/<int:patient_diagnoses_id>')
def patch_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    content = request.get_json()
    patient_diagnoses_controller.patch(patient_diagnoses_id, content)
    return make_response("PatientTrackers updated", HTTPStatus.OK)


@patient_diagnoses_bp.delete('/<int:patient_diagnoses_id>')
def delete_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    patient_diagnoses_controller.delete(patient_diagnoses_id)
    return make_response("PatientTrackers deleted", HTTPStatus.OK)


@patient_diagnoses_bp.get('/get-diagnosis-after-patient/<int:patient_id>')
def get_diagnosis_after_patient(patient_id: int) -> Response:
    return make_response(jsonify(patient_diagnoses_controller.get_diagnosis_after_patient(patient_id)),
                         HTTPStatus.OK)


@patient_diagnoses_bp.get('/get-patients-after-diagnosis/<int:diagnosis_id>')
def get_patients_after_diagnosis(diagnosis_id: int) -> Response:
    return make_response(jsonify(patient_diagnoses_controller.get_patients_after_diagnosis(diagnosis_id)),
                         HTTPStatus.OK)
