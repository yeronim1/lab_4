from lab4.app.my_project.auth.service import medications_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MedicationsController(GeneralController):

    _service = medications_service
