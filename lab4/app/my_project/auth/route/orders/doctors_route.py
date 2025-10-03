from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import doctors_controller
from lab4.app.my_project.auth.domain import Doctors

doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')


@doctors_bp.get('')
def get_all_doctors() -> Response:
    """
    Get all doctors
    ---
    tags:
      - Doctors
    responses:
        200:
            description: A list of doctors
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
                        name:
                            type: string
                            example: Dr. Alan Brown
                        email:
                            type: string
                            example: alanbrown@example.com
                        phone:
                            type: string
                            example: 555-8765
                        specialization:
                            type: string
                            example: Pulmonology
                        hospital_id:
                            type: integer
                            example: 1
    """
    return make_response(jsonify(doctors_controller.find_all()), HTTPStatus.OK)


@doctors_bp.post('')
def create_doctors() -> Response:
    """
    Create a new doctor
    ---
    tags:
      - Doctors
    parameters:
      - name: doctor
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Dr. Alan Brown
                email:
                    type: string
                    example: alanbrown@example.com
                phone:
                    type: string
                    example: 555-8765
                specialization:
                    type: string
                    example: Pulmonology
                hospital_id:
                    type: integer
                    example: 1
    responses:
        201:
            description: Doctor created
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: Dr. Alan Brown
                    email:
                        type: string
                        example: alanbrown@example.com
                    phone:
                        type: string
                        example: 555-8765
                    specialization:
                        type: string
                        example: Pulmonology
                    hospital_id:
                        type: integer
                        example: 1
        500:
            description: Internal server error
    """
    content = request.get_json()
    doctors = Doctors.create_from_dto(content)
    doctors_controller.create(doctors)
    return make_response(jsonify(doctors.put_into_dto()), HTTPStatus.CREATED)


@doctors_bp.get('/<int:doctors_id>')
def get_doctors(doctors_id: int) -> Response:
    """
    Get a doctor by ID
    ---
    tags:
      - Doctors
    parameters:
      - name: doctors_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A doctor object
            content:
            application/json:
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    name:
                        type: string
                        example: Dr. Alan Brown
                    email:
                        type: string
                        example: alanbrown@example.com
                    phone:
                        type: string
                        example: 555-8765
                    specialization:
                        type: string
                        example: Pulmonology
                    hospital_id:
                        type: integer
                        example: 1
        404:
            description: Doctor not found
    """
    return make_response(jsonify(doctors_controller.find_by_id(doctors_id)), HTTPStatus.OK)


@doctors_bp.put('/<int:doctors_id>')
def update_doctors(doctors_id: int) -> Response:
    """
    Update a doctor by ID
    ---
    tags:
      - Doctors
    parameters:
      - name: doctors_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: doctor
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Dr. Alan Brown
                email:
                    type: string
                    example: alanbrown@example.com
                phone:
                    type: string
                    example: 555-8765
                specialization:
                    type: string
                    example: Updated specialization
                hospital_id:
                    type: integer
                    example: 1
    responses:
        200:
            description: Doctor updated
        404:
            description: Doctor not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    doctors = Doctors.create_from_dto(content)
    doctors_controller.update(doctors_id, doctors)
    return make_response("Doctor updated", HTTPStatus.OK)


@doctors_bp.patch('/<int:doctors_id>')
def patch_doctors(doctors_id: int) -> Response:
    """
    Partially update a doctor by ID
    ---
    tags:
      - Doctors
    parameters:
      - name: doctors_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: doctor
        in: body
        required: true
        schema:
            type: object
            properties:
                specialization:
                    type: string
                    example: Partially updated specialization
    responses:
        200:
            description: Doctor updated
        404:
            description: Doctor not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    doctors_controller.patch(doctors_id, content)
    return make_response("Doctor updated", HTTPStatus.OK)


@doctors_bp.delete('/<int:doctors_id>')
def delete_doctors(doctors_id: int) -> Response:
    """
    Delete a doctor by ID
    ---
    tags:
      - Doctors
    parameters:
      - name: doctors_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Doctor deleted
        404:
            description: Doctor not found
        500:
            description: Internal server error
    """
    doctors_controller.delete(doctors_id)
    return make_response("Doctor deleted", HTTPStatus.OK)


@doctors_bp.get("/get-doctors-after-hospital/<int:hospital_id>")
def get_doctors_after_hospital(hospital_id: int) -> Response:
    """
    Get doctors after a specific hospital ID
    ---
    tags:
      - Doctors
    parameters:
      - name: hospital_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A list of doctors
            content:
            application/json:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        doctors_id:
                            type: integer
                            example: 1
                        doctor_name:
                            type: string
                            example: Dr. Alan Brown
                        doctor_email:
                            type: string
                            example: alanbrown@example.com
                        doctor_phone:
                            type: string
                            example: 555-8765
                        doctor_specialization:
                            type: string
                            example: Pulmonology
                        hospitals_id:
                            type: integer
                            example: 1
        404:
            description: Doctors not found
    """
    return make_response(jsonify(doctors_controller.get_doctors_after_hospital(hospital_id)), HTTPStatus.OK)
