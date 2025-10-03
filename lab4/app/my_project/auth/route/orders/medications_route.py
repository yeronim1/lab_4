from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import medications_controller
from lab4.app.my_project.auth.domain import Medications

medications_bp = Blueprint('medications', __name__, url_prefix='/medications')


@medications_bp.get('')
def get_all_medications() -> Response:
    """
    Get all medications
    ---
    tags:
      - Medications
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
                        name:
                            type: string
                            example: Albuterol
                        description:
                            type: string
                            example: Inhaler for asthma
                        dosage:
                            type: string
                            example: 2 puffs every 4-6 hours
    """
    return make_response(jsonify(medications_controller.find_all()), HTTPStatus.OK)


@medications_bp.post('')
def create_medications() -> Response:
    """
    Create a new medication
    ---
    tags:
      - Medications
    parameters:
      - name: medication
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Albuterol
                description:
                    type: string
                    example: Inhaler for asthma
                dosage:
                    type: string
                    example: 2 puffs every 4-6 hours
    responses:
        201:
            description: Medication created
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
                        example: Albuterol
                    description:
                        type: string
                        example: Inhaler for asthma
                    dosage:
                        type: string
                        example: 2 puffs every 4-6 hours
        500:
            description: Internal server error
    """
    content = request.get_json()
    medications = Medications.create_from_dto(content)
    medications_controller.create(medications)
    return make_response(jsonify(medications.put_into_dto()), HTTPStatus.CREATED)


@medications_bp.get('/<int:medications_id>')
def get_medications(medications_id: int) -> Response:
    """
    Get a medication by ID
    ---
    tags:
      - Medications
    parameters:
      - name: medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A medication object
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
                        example: Albuterol
                    description:
                        type: string
                        example: Inhaler for asthma
                    dosage:
                        type: string
                        example: 2 puffs every 4-6 hours
        404:
            description: Medication not found
    """
    return make_response(jsonify(medications_controller.find_by_id(medications_id)), HTTPStatus.OK)


@medications_bp.put('/<int:medications_id>')
def update_medications(medications_id: int) -> Response:
    """
    Update a medication by ID
    ---
    tags:
      - Medications
    parameters:
      - name: medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: medication
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Albuterol
                description:
                    type: string
                    example: Updated description for the medication
                dosage:
                    type: string
                    example: Updated dosage instructions
    responses:
        200:
            description: Medication updated
        404:
            description: Medication not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    medications = Medications.create_from_dto(content)
    medications_controller.update(medications_id, medications)
    return make_response("Medication updated", HTTPStatus.OK)


@medications_bp.patch('/<int:medications_id>')
def patch_medications(medications_id: int) -> Response:
    """
    Partially update a medication by ID
    ---
    tags:
      - Medications
    parameters:
      - name: medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: medication
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
            description: Medication updated
        404:
            description: Medication not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    medications_controller.patch(medications_id, content)
    return make_response("Medication updated", HTTPStatus.OK)


@medications_bp.delete('/<int:medications_id>')
def delete_medications(medications_id: int) -> Response:
    """
    Delete a medication by ID
    ---
    tags:
      - Medications
    parameters:
      - name: medications_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Medication deleted
        404:
            description: Medication not found
        500:
            description: Internal server error
    """
    medications_controller.delete(medications_id)
    return make_response("Medication deleted", HTTPStatus.OK)
