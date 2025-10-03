from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from lab4.app.my_project.auth.controller import hospitals_controller
from lab4.app.my_project.auth.domain import Hospitals

hospitals_bp = Blueprint('hospitals', __name__, url_prefix='/hospitals')


@hospitals_bp.get('')
def get_all_hospitals() -> Response:
    """
    Get all hospitals
    ---
    tags:
      - Hospitals
    responses:
        200:
            description: A list of hospitals
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
                            example: Central Hospital
                        address:
                            type: string
                            example: 123 Main St
                        phone:
                            type: string
                            example: 555-1234
    """
    return make_response(jsonify(hospitals_controller.find_all()), HTTPStatus.OK)


@hospitals_bp.post('')
def create_hospitals() -> Response:
    """
    Create a new hospital
    ---
    tags:
      - Hospitals
    parameters:
      - name: hospital
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Central Hospital
                address:
                    type: string
                    example: 123 Main St
                phone:
                    type: string
                    example: 555-1234
    responses:
        201:
            description: Hospital created
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
                        example: Central Hospital
                    address:
                        type: string
                        example: 123 Main St
                    phone:
                        type: string
                        example: 555-1234
        500:
            description: Internal server error
    """
    content = request.get_json()
    hospitals = Hospitals.create_from_dto(content)
    hospitals_controller.create(hospitals)
    return make_response(jsonify(hospitals.put_into_dto()), HTTPStatus.CREATED)


@hospitals_bp.get('/<int:hospitals_id>')
def get_hospitals(hospitals_id: int) -> Response:
    """
    Get a hospital by ID
    ---
    tags:
      - Hospitals
    parameters:
      - name: hospitals_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A hospital object
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
                        example: Central Hospital
                    address:
                        type: string
                        example: 123 Main St
                    phone:
                        type: string
                        example: 555-1234
        404:
            description: Hospital not found
    """
    return make_response(jsonify(hospitals_controller.find_by_id(hospitals_id)), HTTPStatus.OK)


@hospitals_bp.put('/<int:hospitals_id>')
def update_hospitals(hospitals_id: int) -> Response:
    """
    Update a hospital by ID
    ---
    tags:
      - Hospitals
    parameters:
      - name: hospitals_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: hospital
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Central Hospital
                address:
                    type: string
                    example: Updated address
                phone:
                    type: string
                    example: Updated phone number
    responses:
        200:
            description: Hospital updated
        404:
            description: Hospital not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    hospitals = Hospitals.create_from_dto(content)
    hospitals_controller.update(hospitals_id, hospitals)
    return make_response("Hospital updated", HTTPStatus.OK)


@hospitals_bp.patch('/<int:hospitals_id>')
def patch_hospitals(hospitals_id: int) -> Response:
    """
    Partially update a hospital by ID
    ---
    tags:
      - Hospitals
    parameters:
      - name: hospitals_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: hospital
        in: body
        required: true
        schema:
            type: object
            properties:
                address:
                    type: string
                    example: Partially updated address
    responses:
        200:
            description: Hospital updated
        404:
            description: Hospital not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    hospitals_controller.patch(hospitals_id, content)
    return make_response("Hospital updated", HTTPStatus.OK)


@hospitals_bp.delete('/<int:hospitals_id>')
def delete_hospitals(hospitals_id: int) -> Response:
    """
    Delete a hospital by ID
    ---
    tags:
      - Hospitals
    parameters:
      - name: hospitals_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Hospital deleted
        404:
            description: Hospital not found
        500:
            description: Internal server error
    """
    hospitals_controller.delete(hospitals_id)
    return make_response("Hospital deleted", HTTPStatus.OK)


