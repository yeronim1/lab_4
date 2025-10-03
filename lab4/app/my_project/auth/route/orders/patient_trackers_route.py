from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patient_trackers_controller
from lab4.app.my_project.auth.domain import PatientTrackers

patient_trackers_bp = Blueprint('patient_trackers', __name__, url_prefix='/patient-trackers')


@patient_trackers_bp.get('')
def get_all_patient_trackers() -> Response:
    return make_response(jsonify(patient_trackers_controller.find_all()), HTTPStatus.OK)


@patient_trackers_bp.post('')
def create_patient_trackers() -> Response:
    content = request.get_json()
    patient_trackers = PatientTrackers.create_from_dto(content)
    patient_trackers_controller.create(patient_trackers)
    return make_response(jsonify(patient_trackers.put_into_dto()), HTTPStatus.CREATED)


@patient_trackers_bp.get('/<int:patient_trackers_id>')
def get_patient_trackers(patient_trackers_id: int) -> Response:
    return make_response(jsonify(patient_trackers_controller.find_by_id(patient_trackers_id)), HTTPStatus.OK)


@patient_trackers_bp.put('/<int:patient_trackers_id>')
def update_patient_trackers(patient_trackers_id: int) -> Response:
    content = request.get_json()
    patient_trackers = PatientTrackers.create_from_dto(content)
    patient_trackers_controller.update(patient_trackers_id, patient_trackers)
    return make_response("PatientTrackers updated", HTTPStatus.OK)


@patient_trackers_bp.patch('/<int:patient_trackers_id>')
def patch_patient_trackers(patient_trackers_id: int) -> Response:
    content = request.get_json()
    patient_trackers_controller.patch(patient_trackers_id, content)
    return make_response("PatientTrackers updated", HTTPStatus.OK)


@patient_trackers_bp.delete('/<int:trackers_id>')
def delete_patient_trackers(patient_trackers_id: int) -> Response:
    patient_trackers_controller.delete(patient_trackers_id)
    return make_response("PatientTrackers deleted", HTTPStatus.OK)


@patient_trackers_bp.get('/get-trackers-after-patient/<int:patient_id>')
def get_trackers_after_patient(patient_id: int) -> Response:
    return make_response(jsonify(patient_trackers_controller.get_trackers_after_patient(patient_id)),
                         HTTPStatus.OK)


@patient_trackers_bp.get('/get-patients-after-tracker/<int:tracker_id>')
def get_patients_after_tracker(tracker_id: int) -> Response:
    return make_response(jsonify(patient_trackers_controller.get_patients_after_tracker(tracker_id)),
                         HTTPStatus.OK)
