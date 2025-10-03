from lab4.app.my_project.auth.service import trackers_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class TrackersController(GeneralController):

    _service = trackers_service
