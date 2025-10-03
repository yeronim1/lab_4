from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import diagnoses_controller
from lab4.app.my_project.auth.domain import Diagnoses

diagnoses_bp = Blueprint('diagnoses', __name__, url_prefix='/diagnoses')


@diagnoses_bp.get('')
def get_all_diagnoses() -> Response:
    """
    Get all diagnoses
    ---
    tags:
      - Diagnoses
    responses:
        200:
            description: A list of diagnoses
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
                            example: Asthma
                        description:
                            type: string
                            example: Chronic lung disease that inflames and narrows the airways.
    """
    return make_response(jsonify(diagnoses_controller.find_all()), HTTPStatus.OK)


@diagnoses_bp.post('')
def create_diagnoses() -> Response:
    """
    Create a new diagnosis
    ---
    tags:
      - Diagnoses
    parameters:
      - name: diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Asthma
                description:
                    type: string
                    example: Chronic lung disease that inflames and narrows the airways.
    responses:
        201:
            description: Diagnosis created
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
                        example: Asthma
                    description:
                        type: string
                        example: Chronic lung disease that inflames and narrows the airways.
        500:
            description: Internal server error
    """
    content = request.get_json()
    diagnoses = Diagnoses.create_from_dto(content)
    diagnoses_controller.create(diagnoses)
    return make_response(jsonify(diagnoses.put_into_dto()), HTTPStatus.CREATED)


@diagnoses_bp.get('/<int:diagnoses_id>')
def get_diagnoses(diagnoses_id: int) -> Response:
    """
    Get a diagnosis by ID
    ---
    tags:
      - Diagnoses
    parameters:
      - name: diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A diagnosis object
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
                        example: Asthma
                    description:
                        type: string
                        example: Chronic lung disease that inflames and narrows the airways.
        404:
            description: Diagnosis not found
    """
    return make_response(jsonify(diagnoses_controller.find_by_id(diagnoses_id)), HTTPStatus.OK)


@diagnoses_bp.put('/<int:diagnoses_id>')
def update_diagnoses(diagnoses_id: int) -> Response:
    """
    Update a diagnosis by ID
    ---
    tags:
      - Diagnoses
    parameters:
      - name: diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Asthma
                description:
                    type: string
                    example: Updated description for the diagnosis.
    responses:
        200:
            description: Diagnosis updated
        404:
            description: Diagnosis not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    diagnoses = Diagnoses.create_from_dto(content)
    diagnoses_controller.update(diagnoses_id, diagnoses)
    return make_response("Diagnosis updated", HTTPStatus.OK)


@diagnoses_bp.patch('/<int:diagnoses_id>')
def patch_diagnoses(diagnoses_id: int) -> Response:
    """
    Partially update a diagnosis by ID
    ---
    tags:
      - Diagnoses
    parameters:
      - name: diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: diagnosis
        in: body
        required: true
        schema:
            type: object
            properties:
                description:
                    type: string
                    example: Partially updated description for the diagnosis.
    responses:
        200:
            description: Diagnosis updated
        404:
            description: Diagnosis not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    diagnoses_controller.patch(diagnoses_id, content)
    return make_response("Diagnosis updated", HTTPStatus.OK)


@diagnoses_bp.delete('/<int:diagnoses_id>')
def delete_diagnoses(diagnoses_id: int) -> Response:
    """
    Delete a diagnosis by ID
    ---
    tags:
      - Diagnoses
    parameters:
      - name: diagnoses_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Diagnosis deleted
        404:
            description: Diagnosis not found
        500:
            description: Internal server error
    """
    diagnoses_controller.delete(diagnoses_id)
    return make_response("Diagnosis deleted", HTTPStatus.OK)
