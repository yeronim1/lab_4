from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import consultations_controller
from lab4.app.my_project.auth.domain import Consultations

consultations_bp = Blueprint('consultations', __name__, url_prefix='/consultations')


@consultations_bp.get('')
def get_all_consultations() -> Response:
    """
    Get all consultations
    ---
    tags:
      - Consultations
    responses:
        200:
            description: A list of consultations
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            example: 8
                        consultation_date:
                            type: string
                            example: Tue, 19 Nov 2024 00:00:00 GMT
                        diagnosis:
                            type: string
                            example: Cancer
                        doctor_id:
                            type: integer
                            example: 8
                        notes:
                            type: string
                            example: Patient requires chemotherapy.
                        patient_id:
                            type: integer
                            example: 8
    """
    return make_response(jsonify(consultations_controller.find_all()), HTTPStatus.OK)


@consultations_bp.post('')
def create_consultations() -> Response:
    """
    Create a new consultation
    ---
    tags:
      - Consultations
    parameters:
      - name: consultation
        in: body
        required: true
        schema:
            type: object
            properties:
                consultation_date:
                    type: string
                    example: Tue, 19 Nov 2024 00:00:00 GMT
                diagnosis:
                    type: string
                    example: Cancer
                doctor_id:
                    type: integer
                    example: 8
                notes:
                    type: string
                    example: Patient requires chemotherapy.
                patient_id:
                    type: integer
                    example: 8
    responses:
        201:
            description: Consultation created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 8
                    consultation_date:
                        type: string
                        example: Tue, 19 Nov 2024 00:00:00 GMT
                    diagnosis:
                        type: string
                        example: Cancer
                    doctor_id:
                        type: integer
                        example: 8
                    notes:
                        type: string
                        example: Patient requires chemotherapy.
                    patient_id:
                        type: integer
                        example: 8
        500:
            description: Internal server error
    """
    content = request.get_json()
    consultations = Consultations.create_from_dto(content)
    consultations_controller.create(consultations)
    return make_response(jsonify(consultations.put_into_dto()), HTTPStatus.CREATED)


@consultations_bp.get('/<int:consultations_id>')
def get_consultations(consultations_id: int) -> Response:
    """
    Get a consultation by ID
    ---
    tags:
      - Consultations
    parameters:
      - name: consultations_id
        in: path
        required: true
        schema:
            type: integer
            example: 8
    responses:
        200:
            description: A consultation object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 8
                    consultation_date:
                        type: string
                        example: Tue, 19 Nov 2024 00:00:00 GMT
                    diagnosis:
                        type: string
                        example: Cancer
                    doctor_id:
                        type: integer
                        example: 8
                    notes:
                        type: string
                        example: Patient requires chemotherapy.
                    patient_id:
                        type: integer
                        example: 8
        404:
            description: Consultation not found
    """
    return make_response(jsonify(consultations_controller.find_by_id(consultations_id)), HTTPStatus.OK)


@consultations_bp.put('/<int:consultations_id>')
def update_consultations(consultations_id: int) -> Response:
    """
    Update a consultation by ID
    ---
    tags:
      - Consultations
    parameters:
      - name: consultations_id
        in: path
        required: true
        schema:
            type: integer
            example: 8
      - name: consultation
        in: body
        required: true
        schema:
            type: object
            properties:
                consultation_date:
                    type: string
                    example: Tue, 19 Nov 2024 00:00:00 GMT
                diagnosis:
                    type: string
                    example: Cancer
                doctor_id:
                    type: integer
                    example: 8
                notes:
                    type: string
                    example: Updated notes for consultation.
                patient_id:
                    type: integer
                    example: 8
    responses:
        200:
            description: Consultation updated
        404:
            description: Consultation not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    consultations = Consultations.create_from_dto(content)
    consultations_controller.update(consultations_id, consultations)
    return make_response("Consultation updated", HTTPStatus.OK)


@consultations_bp.patch('/<int:consultations_id>')
def patch_consultations(consultations_id: int) -> Response:
    """
    Partially update a consultation by ID
    ---
    tags:
      - Consultations
    parameters:
      - name: consultations_id
        in: path
        required: true
        schema:
            type: integer
            example: 8
      - name: consultation
        in: body
        required: true
        schema:
            type: object
            properties:
                notes:
                    type: string
                    example: Partially updated notes for consultation.
    responses:
        200:
            description: Consultation updated
        404:
            description: Consultation not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    consultations_controller.patch(consultations_id, content)
    return make_response("Consultation updated", HTTPStatus.OK)


@consultations_bp.delete('/<int:consultations_id>')
def delete_consultations(consultations_id: int) -> Response:
    """
    Delete a consultation by ID
    ---
    tags:
      - Consultations
    parameters:
      - name: consultations_id
        in: path
        required: true
        schema:
            type: integer
            example: 8
    responses:
        200:
            description: Consultation deleted
        404:
            description: Consultation not found
        500:
            description: Internal server error
    """
    consultations_controller.delete(consultations_id)
    return make_response("Consultation deleted", HTTPStatus.OK)


@consultations_bp.get('/get-consultations-after-patient/<int:patient_id>')
def get_consultations_after_patient(patient_id: int) -> Response:
    """
    Get consultations after a specific patient ID
    ---
    tags:
      - Consultations
    parameters:
      - name: patient_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of consultations
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        consultations_id:
                            type: integer
                            example: 1
                        consultation_date:
                            type: string
                            example: Tue, 12 Nov 2024 00:00:00 GMT
                        consultation_diagnosis:
                            type: string
                            example: Asthma
                        consultation_notes:
                            type: string
                            example: Patient has mild asthma symptoms.
                        patients_id:
                            type: integer
                            example: 1
        404:
            description: Consultations not found
    """
    return make_response(jsonify(consultations_controller.get_consultations_after_patient(patient_id)), HTTPStatus.OK)


@consultations_bp.get('/get-consultations-after-doctor/<int:doctor_id>')
def get_consultations_after_doctor(doctor_id: int) -> Response:
    """
    Get consultations after a specific doctor ID
    ---
    tags:
      - Consultations
    parameters:
      - name: doctor_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of consultations
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        consultations_id:
                            type: integer
                            example: 1
                        consultation_date:
                            type: string
                            example: Tue, 12 Nov 2024 00:00:00 GMT
                        consultation_diagnosis:
                            type: string
                            example: Asthma
                        consultation_notes:
                            type: string
                            example: Patient has mild asthma symptoms.
                        doctors_id:
                            type: integer
                            example: 1
        404:
            description: Consultations not found
    """
    return make_response(jsonify(consultations_controller.get_consultations_after_doctor(doctor_id)), HTTPStatus.OK)
