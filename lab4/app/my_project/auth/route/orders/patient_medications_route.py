from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from lab4.app.my_project.auth.controller import patient_medications_controller
from lab4.app.my_project.auth.domain import PatientMedications

patient_medications_bp = Blueprint('patient_medications', __name__, url_prefix='/patient-medications')


@patient_medications_bp.get('')
def get_all_patient_medications() -> Response:
    """
    Get all patient medications
    ---
    tags:
      - Patient Medications
    responses:
        200:
            description: A list of patient medications
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
                        medication_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        dosage:
                            type: string
                            example: 2 puffs every 4-6 hours
                        start_date:
                            type: string
                            example: Tue, 12 Nov 2024 00:00:00 GMT
                        end_date:
                            type: string
                            example: Tue, 19 Nov 2024 00:00:00 GMT
    """
    return make_response(jsonify(patient_medications_controller.find_all()), HTTPStatus.OK)


@patient_medications_bp.post('')
def create_patient_medications() -> Response:
    """
    Create a new patient medication
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_medication
        in: body
        required: true
        schema:
            type: object
            properties:
                medication_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
                dosage:
                    type: string
                    example: 2 puffs every 4-6 hours
                start_date:
                    type: string
                    example: Tue, 12 Nov 2024 00:00:00 GMT
                end_date:
                    type: string
                    example: Tue, 19 Nov 2024 00:00:00 GMT
    responses:
        201:
            description: Patient medication created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    medication_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
                    dosage:
                        type: string
                        example: 2 puffs every 4-6 hours
                    start_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    end_date:
                        type: string
                        example: Tue, 19 Nov 2024 00:00:00 GMT
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_medications = PatientMedications.create_from_dto(content)
    patient_medications_controller.create(patient_medications)
    return make_response(jsonify(patient_medications.put_into_dto()), HTTPStatus.CREATED)


@patient_medications_bp.get('/<int:patient_medications_id>')
def get_patient_medications(patient_medications_id: int) -> Response:
    """
    Get a patient medication by ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A patient medication object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    medication_id:
                        type: integer
                        example: 1
                    patient_id:
                        type: integer
                        example: 1
                    dosage:
                        type: string
                        example: 2 puffs every 4-6 hours
                    start_date:
                        type: string
                        example: Tue, 12 Nov 2024 00:00:00 GMT
                    end_date:
                        type: string
                        example: Tue, 19 Nov 2024 00:00:00 GMT
        404:
            description: Patient medication not found
    """
    return make_response(jsonify(patient_medications_controller.find_by_id(patient_medications_id)), HTTPStatus.OK)


@patient_medications_bp.put('/<int:patient_medications_id>')
def update_patient_medications(patient_medications_id: int) -> Response:
    """
    Update a patient medication by ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_medication
        in: body
        required: true
        schema:
            type: object
            properties:
                medication_id:
                    type: integer
                    example: 1
                patient_id:
                    type: integer
                    example: 1
                dosage:
                    type: string
                    example: Updated dosage instructions
                start_date:
                    type: string
                    example: Updated start date
                end_date:
                    type: string
                    example: Updated end date
    responses:
        200:
            description: Patient medication updated
        404:
            description: Patient medication not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_medications = PatientMedications.create_from_dto(content)
    patient_medications_controller.update(patient_medications_id, patient_medications)
    return make_response("Patient medication updated", HTTPStatus.OK)


@patient_medications_bp.patch('/<int:patient_medications_id>')
def patch_patient_medications(patient_medications_id: int) -> Response:
    """
    Partially update a patient medication by ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient_medication
        in: body
        required: true
        schema:
            type: object
            properties:
                dosage:
                    type: string
                    example: Partially updated dosage instructions
    responses:
        200:
            description: Patient medication updated
        404:
            description: Patient medication not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patient_medications_controller.patch(patient_medications_id, content)
    return make_response("Patient medication updated", HTTPStatus.OK)


@patient_medications_bp.delete('/<int:patient_medications_id>')
def delete_patient_medications(patient_medications_id: int) -> Response:
    """
    Delete a patient medication by ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Patient medication deleted
        404:
            description: Patient medication not found
        500:
            description: Internal server error
    """
    patient_medications_controller.delete(patient_medications_id)
    return make_response("Patient medication deleted", HTTPStatus.OK)


@patient_medications_bp.get('/get-patients-after-medication/<int:medication_id>')
def get_patients_after_medication(medication_id: int) -> Response:
    """
    Get patients after a specific medication ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: medication_id
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
                        medication_id:
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
    return make_response(jsonify(patient_medications_controller.get_patients_after_medication(medication_id)), HTTPStatus.OK)


@patient_medications_bp.get('/get-medications-after-patient/<int:patient_id>')
def get_medications_after_patient(patient_id: int) -> Response:
    """
    Get medications after a specific patient ID
    ---
    tags:
      - Patient Medications
    parameters:
      - name: patient_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of medications
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
                        medication_id:
                            type: integer
                            example: 1
                        patient_id:
                            type: integer
                            example: 1
                        medication_name:
                            type: string
                            example: Albuterol
                        medication_description:
                            type: string
                            example: Inhaler for asthma
                        medication_dosage:
                            type: string
                            example: 2 puffs every 4-6 hours
        404:
            description: Medications not found
    """
    return make_response(jsonify(patient_medications_controller.get_medications_after_patient(patient_id)), HTTPStatus.OK)
