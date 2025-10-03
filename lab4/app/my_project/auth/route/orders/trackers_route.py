from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import trackers_controller
from lab4.app.my_project.auth.domain import Trackers

trackers_bp = Blueprint('trackers', __name__, url_prefix='/trackers')


@trackers_bp.get('')
def get_all_trackers() -> Response:
    """
    Get all trackers
    ---
    tags:
      - Trackers
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
                        name:
                            type: string
                            example: Blood Pressure
                        unit:
                            type: string
                            example: mmHg
    """
    return make_response(jsonify(trackers_controller.find_all()), HTTPStatus.OK)


@trackers_bp.post('')
def create_trackers() -> Response:
    """
    Create a new tracker
    ---
    tags:
      - Trackers
    parameters:
      - name: tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Blood Pressure
                unit:
                    type: string
                    example: mmHg
    responses:
        201:
            description: Tracker created
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
                        example: Blood Pressure
                    unit:
                        type: string
                        example: mmHg
        500:
            description: Internal server error
    """
    content = request.get_json()
    trackers = Trackers.create_from_dto(content)
    trackers_controller.create(trackers)
    return make_response(jsonify(trackers.put_into_dto()), HTTPStatus.CREATED)


@trackers_bp.get('/<int:trackers_id>')
def get_trackers(trackers_id: int) -> Response:
    """
    Get a tracker by ID
    ---
    tags:
      - Trackers
    parameters:
      - name: trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: A tracker object
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
                        example: Blood Pressure
                    unit:
                        type: string
                        example: mmHg
        404:
            description: Tracker not found
    """
    return make_response(jsonify(trackers_controller.find_by_id(trackers_id)), HTTPStatus.OK)


@trackers_bp.put('/<int:trackers_id>')
def update_trackers(trackers_id: int) -> Response:
    """
    Update a tracker by ID
    ---
    tags:
      - Trackers
    parameters:
      - name: trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                    example: Updated name
                unit:
                    type: string
                    example: Updated unit
    responses:
        200:
            description: Tracker updated
        404:
            description: Tracker not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    trackers = Trackers.create_from_dto(content)
    trackers_controller.update(trackers_id, trackers)
    return make_response("Tracker updated", HTTPStatus.OK)


@trackers_bp.patch('/<int:trackers_id>')
def patch_trackers(trackers_id: int) -> Response:
    """
    Partially update a tracker by ID
    ---
    tags:
      - Trackers
    parameters:
      - name: trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
      - name: tracker
        in: body
        required: true
        schema:
            type: object
            properties:
                unit:
                    type: string
                    example: Partially updated unit
    responses:
        200:
            description: Tracker updated
        404:
            description: Tracker not found
        500:
            description: Internal server error
    """
    content = request.get_json()
    trackers_controller.patch(trackers_id, content)
    return make_response("Tracker updated", HTTPStatus.OK)


@trackers_bp.delete('/<int:trackers_id>')
def delete_trackers(trackers_id: int) -> Response:
    """
    Delete a tracker by ID
    ---
    tags:
      - Trackers
    parameters:
      - name: trackers_id
        in: path
        required: true
        schema:
            type: integer
            example: 1
    responses:
        200:
            description: Tracker deleted
        404:
            description: Tracker not found
        500:
            description: Internal server error
    """
    trackers_controller.delete(trackers_id)
    return make_response("Tracker deleted", HTTPStatus.OK)


