from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patient_trackers_controller
from lab4.app.my_project.auth.domain import PatientTrackers

patient_trackers_bp = Blueprint('patient_trackers', __name__, url_prefix='/patient-trackers')


@patient_trackers_bp.get('')
def get_all_patient_trackers() -> Response:
    """
    Get all patient trackers
    ---
    tags:
      - Patient Trackers
    responses:
        200:
            description: A list of patient trackers
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            example: 1
                        tracker_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        measurement_date:
                            type: string
                            example: Tue, 12 Nov 2024 00:00:00 GMT
                        measurement_value:
                            type: number
                            format: float
                            example: 120.0
    """
    return make_response(jsonify(patient_trackers_controller.find_all()), HTTPStatus.OK)


@patient_trackers_bp.post('')
def create_patient_trackers() -> Response:
    """
    Create a new patient tracker
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                tracker_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
                measurement_date:
                    type: string
                    example: Tue, 12 Nov 2024 00:00:00 GMT
                measurement_value:
                    type: number
                    format: float
                    example: 120.0
    responses:
        201:
            description: Patient tracker created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    tracker_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
                    measurement_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    measurement_value:
                        type: number
                        format: float
                        example: 120.0
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_trackers = PatientTrackers.create_from_dto(content)
    patient_trackers_controller.create(patient_trackers)
    return make_response(jsonify(patient_trackers.put_into_dto()), HTTPStatus.CREATED)


@patient_trackers_bp.get('/<int:patient_trackers_id>')
def get_patient_trackers(patient_trackers_id: int) -> Response:
    """
    Get a patient tracker by ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A patient tracker object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    tracker_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
                    measurement_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    measurement_value:
                        type: number
                        format: float
                        example: 120.0
        404:
            description: Patient tracker not found
    """
    return make_response(jsonify(patient_trackers_controller.find_by_id(patient_trackers_id)), HTTPStatus.OK)


@patient_trackers_bp.put('/<int:patient_trackers_id>')
def update_patient_trackers(patient_trackers_id: int) -> Response:
    """
    Update a patient tracker by ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                tracker_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
                measurement_date:
                    type: string
                    example: Updated measurement date
                measurement_value:
                    type: number
                    format: float
                    example: Updated measurement value
    responses:
        200:
            description: Patient tracker updated
        404:
            description: Patient tracker not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_trackers = PatientTrackers.create_from_dto(content)
    patient_trackers_controller.update(patient_trackers_id, patient_trackers)
    return make_response("Patient tracker updated", HTTPStatus.OK)


@patient_trackers_bp.patch('/<int:patient_trackers_id>')
def patch_patient_trackers(patient_trackers_id: int) -> Response:
    """
    Partially update a patient tracker by ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                measurement_value:
                    type: number
                    format: float
                    example: Partially updated measurement value
    responses:
        200:
            description: Patient tracker updated
        404:
            description: Patient tracker not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_trackers_controller.patch(patient_trackers_id, content)
    return make_response("Patient tracker updated", HTTPStatus.OK)


@patient_trackers_bp.delete('/<int:trackers_id>')
def delete_patient_trackers(patient_trackers_id: int) -> Response:
    """
    Delete a patient tracker by ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Patient tracker deleted
        404:
            description: Patient tracker not found
        500:
            description: Internal server error
    """
    patient_trackers_controller.delete(patient_trackers_id)
    return make_response("Patient tracker deleted", HTTPStatus.OK)


@patient_trackers_bp.get('/get-trackers-after-patient/<int:patient_id>')
def get_trackers_after_patient(patient_id: int) -> Response:
    """
    Get trackers after a specific patient ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: patient_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of trackers
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            example: 1
                        tracker_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        tracker_name:
                            type: string
                            example: Blood Pressure
                        tracker_unit:
                            type: string
                            example: mmHg
        404:
            description: Trackers not found
    """
    return make_response(jsonify(patient_trackers_controller.get_trackers_after_patient(patient_id)), HTTPStatus.OK)


@patient_trackers_bp.get('/get-patients-after-tracker/<int:tracker_id>')
def get_patients_after_tracker(tracker_id: int) -> Response:
    """
    Get patients after a specific tracker ID
    ---
    tags:
      - Patient Trackers
    parameters:
      - name: tracker_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of patients
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            example: 1
                        tracker_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        patient_name:
                            type: string
                            example: John Doe
                        patient_gender:
                            type: string
                            example: Male
                        patient_date_of_birth:
                            type: string
                            example: Mon, 20 May 1985 00:00:00 GMT
                        patient_contact_info:
                            type: string
                            example: johndoe@example.com
        404:
            description: Patients not found
    """
    return make_response(jsonify(patient_trackers_controller.get_patients_after_tracker(tracker_id)), HTTPStatus.OK)
