from typing import List

from lab4.app.my_project.auth.service import doctors_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class DoctorsController(GeneralController):

    _service = doctors_service

    def get_doctors_after_hospital(self, hospital_id) -> List[object]:
        return self._service.get_doctors_after_hospital(hospital_id)
