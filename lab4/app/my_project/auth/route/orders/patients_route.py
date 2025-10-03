from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import patients_controller
from lab4.app.my_project.auth.domain import Patients

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')


@patients_bp.get('')
def get_all_patients() -> Response:
    """
    Get all patients
    ---
    tags:
      - Patients
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
                        hospital_id:
                            type: integer
                            example: 1
                        name:
                            type: string
                            example: John Doe
                        gender:
                            type: string
                            example: Male
                        date_of_birth:
                            type: string
                            example: Mon, 20 May 1985 00:00:00 GMT
                        contact_info:
                            type: string
                            example: johndoe@example.com
    """
    return make_response(jsonify(patients_controller.find_all()), HTTPStatus.OK)


@patients_bp.post('')
def create_patients() -> Response:
    """
    Create a new patient
    ---
    tags:
      - Patients
    parameters:
      - name: patient
        in: body
        required: true
        schema:
            type: object
            properties:
                hospital_id:
                    type: integer
                    example: 1
                name:
                    type: string
                    example: John Doe
                gender:
                    type: string
                    example: Male
                date_of_birth:
                    type: string
                    example: Mon, 20 May 1985 00:00:00 GMT
                contact_info:
                    type: string
                    example: johndoe@example.com
    responses:
        201:
            description: Patient created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    hospital_id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: John Doe
                    gender:
                        type: string
                        example: Male
                    date_of_birth:
                        type: string
                        example: Mon, 20 May 1985 00:00:00 GMT
                    contact_info:
                        type: string
                        example: johndoe@example.com
        500:
            description: Internal server error
    """
    content = request.get_json()
    patients = Patients.create_from_dto(content)
    patients_controller.create(patients)
    return make_response(jsonify(patients.put_into_dto()), HTTPStatus.CREATED)


@patients_bp.get('/<int:patients_id>')
def get_patients(patients_id: int) -> Response:
    """
    Get a patient by ID
    ---
    tags:
      - Patients
    parameters:
      - name: patients_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A patient object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    hospital_id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: John Doe
                    gender:
                        type: string
                        example: Male
                    date_of_birth:
                        type: string
                        example: Mon, 20 May 1985 00:00:00 GMT
                    contact_info:
                        type: string
                        example: johndoe@example.com
        404:
            description: Patient not found
    """
    return make_response(jsonify(patients_controller.find_by_id(patients_id)), HTTPStatus.OK)


@patients_bp.put('/<int:patients_id>')
def update_patients(patients_id: int) -> Response:
    """
    Update a patient by ID
    ---
    tags:
      - Patients
    parameters:
      - name: patients_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient
        in: body
        required: true
        schema:
            type: object
            properties:
                hospital_id:
                    type: integer
                    example: 1
                name:
                    type: string
                    example: Updated name
                gender:
                    type: string
                    example: Updated gender
                date_of_birth:
                    type: string
                    example: Updated date of birth
                contact_info:
                    type: string
                    example: Updated contact info
    responses:
        200:
            description: Patient updated
        404:
            description: Patient not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patients = Patients.create_from_dto(content)
    patients_controller.update(patients_id, patients)
    return make_response("Patient updated", HTTPStatus.OK)


@patients_bp.patch('/<int:patients_id>')
def patch_patients(patients_id: int) -> Response:
    """
    Partially update a patient by ID
    ---
    tags:
      - Patients
    parameters:
      - name: patients_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: patient
        in: body
        required: true
        schema:
            type: object
            properties:
                contact_info:
                    type: string
                    example: Partially updated contact info
    responses:
        200:
            description: Patient updated
        404:
            description: Patient not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    patients_controller.patch(patients_id, content)
    return make_response("Patient updated", HTTPStatus.OK)


@patients_bp.delete('/<int:patients_id>')
def delete_patients(patients_id: int) -> Response:
    """
    Delete a patient by ID
    ---
    tags:
      - Patients
    parameters:
      - name: patients_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Patient deleted
        404:
            description: Patient not found
        500:
            description: Internal server error
    """
    patients_controller.delete(patients_id)
    return make_response("Patient deleted", HTTPStatus.OK)


@patients_bp.get('/get-patients-after-hospital/<int:hospital_id>')
def get_patients_after_hospital(hospital_id: int) -> Response:
    """
    Get patients after a specific hospital ID
    ---
    tags:
      - Patients
    parameters:
      - name: hospital_id
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
                        patients_id:
                            type: integer
                            example: 1
                        hospitals_id:
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
    return make_response(jsonify(patients_controller.get_patients_after_hospital(hospital_id)), HTTPStatus.OK)
