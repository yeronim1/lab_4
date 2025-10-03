from typing import List

from lab4.app.my_project.auth.service import patient_medications_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PatientMedicationsController(GeneralController):

    _service = patient_medications_service

    def get_patients_after_medication(self, medication_id) -> List[object]:
        return self._service.get_patients_after_medication(medication_id)

    def get_medications_after_patient(self, patient_id) -> List[object]:
        return self._service.get_medications_after_patient(patient_id)
