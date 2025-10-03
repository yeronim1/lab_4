from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from lab4.app.my_project.auth.controller import patient_diagnoses_controller
from lab4.app.my_project.auth.domain import PatientTrackers

patient_diagnoses_bp = Blueprint('patient_diagnoses', __name__, url_prefix='/patient-diagnoses')


@patient_diagnoses_bp.get('')
def get_all_patient_diagnoses() -> Response:
    """
    Get all patient diagnoses
    ---
    tags:
      - Patient Diagnoses
    responses:
        200:
            description: A list of patient diagnoses
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
                        diagnosis_date:
                            type: string
                            example: Tue, 12 Nov 2024 00:00:00 GMT
                        diagnosis_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(patient_diagnoses_controller.find_all()), HTTPStatus.OK)


@patient_diagnoses_bp.post('')
def create_patient_diagnoses() -> Response:
    """
    Create a new patient diagnosis
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                diagnosis_date:
                    type: string
                    example: Tue, 12 Nov 2024 00:00:00 GMT
                diagnosis_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
    responses:
        201:
            description: Patient diagnosis created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    diagnosis_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    diagnosis_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_diagnoses = PatientTrackers.create_from_dto(content)
    patient_diagnoses_controller.create(patient_diagnoses)
    return make_response(jsonify(patient_diagnoses.put_into_dto()), HTTPStatus.CREATED)


@patient_diagnoses_bp.get('/<int:patient_diagnoses_id>')
def get_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    """
    Get a patient diagnosis by ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A patient diagnosis object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    diagnosis_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    diagnosis_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
        404:
            description: Patient diagnosis not found
    """
    return make_response(jsonify(patient_diagnoses_controller.find_by_id(patient_diagnoses_id)), HTTPStatus.OK)


@patient_diagnoses_bp.put('/<int:patient_diagnoses_id>')
def update_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    """
    Update a patient diagnosis by ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                diagnosis_date:
                    type: string
                    example: Tue, 12 Nov 2024 00:00:00 GMT
                diagnosis_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Patient diagnosis updated
        404:
            description: Patient diagnosis not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_diagnoses = PatientTrackers.create_from_dto(content)
    patient_diagnoses_controller.update(patient_diagnoses_id, patient_diagnoses)
    return make_response("Patient diagnosis updated", HTTPStatus.OK)


@patient_diagnoses_bp.patch('/<int:patient_diagnoses_id>')
def patch_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    """
    Partially update a patient diagnosis by ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                diagnosis_date:
                    type: string
                    example: Partially updated diagnosis date
    responses:
        200:
            description: Patient diagnosis updated
        404:
            description: Patient diagnosis not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_diagnoses_controller.patch(patient_diagnoses_id, content)
    return make_response("Patient diagnosis updated", HTTPStatus.OK)


@patient_diagnoses_bp.delete('/<int:patient_diagnoses_id>')
def delete_patient_diagnoses(patient_diagnoses_id: int) -> Response:
    """
    Delete a patient diagnosis by ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Patient diagnosis deleted
        404:
            description: Patient diagnosis not found
        500:
            description: Internal server error
    """
    patient_diagnoses_controller.delete(patient_diagnoses_id)
    return make_response("Patient diagnosis deleted", HTTPStatus.OK)


@patient_diagnoses_bp.get('/get-diagnosis-after-patient/<int:patient_id>')
def get_diagnosis_after_patient(patient_id: int) -> Response:
    """
    Get diagnoses after a specific patient ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: patient_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of patient diagnoses
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
                        diagnosis_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        diagnoses_name:
                            type: string
                            example: Asthma
                        diagnoses_description:
                            type: string
                            example: Chronic lung disease that inflames and narrows the airways.
        404:
            description: Patient diagnoses not found
    """
    return make_response(jsonify(patient_diagnoses_controller.get_diagnosis_after_patient(patient_id)), HTTPStatus.OK)


@patient_diagnoses_bp.get('/get-patients-after-diagnosis/<int:diagnosis_id>')
def get_patients_after_diagnosis(diagnosis_id: int) -> Response:
    """
    Get patients after a specific diagnosis ID
    ---
    tags:
      - Patient Diagnoses
    parameters:
      - name: diagnosis_id
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
                        diagnosis_id:
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
    return make_response(jsonify(patient_diagnoses_controller.get_patients_after_diagnosis(diagnosis_id)), HTTPStatus.OK)
