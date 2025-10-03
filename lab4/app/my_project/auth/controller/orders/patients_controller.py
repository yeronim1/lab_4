from typing import List

from lab4.app.my_project.auth.service import patients_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PatientsController(GeneralController):

    _service = patients_service

    def get_patients_after_hospital(self, hospital_id) -> List[object]:
        return self._service.get_patients_after_hospital(hospital_id)
