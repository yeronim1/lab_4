from lab4.app.my_project.auth.service import diagnoses_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class DiagnosesController(GeneralController):

    _service = diagnoses_service
