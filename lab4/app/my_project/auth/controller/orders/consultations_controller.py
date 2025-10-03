from typing import List

from lab4.app.my_project.auth.service import consultations_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ConsultationsController(GeneralController):

    _service = consultations_service

    def get_consultations_after_patient(self, patient_id) -> List[object]:
        return self._service.get_consultations_after_patient(patient_id)

    def get_consultations_after_doctor(self, doctor_id) -> List[object]:
        return self._service.get_consultations_after_doctor(doctor_id)
