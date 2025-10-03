from lab4.app.my_project.auth.service import hospitals_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class HospitalsController(GeneralController):

    _service = hospitals_service
