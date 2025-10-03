from typing import List

from lab4.app.my_project.auth.service import patient_diagnoses_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PatientDiagnosesController(GeneralController):

    _service = patient_diagnoses_service

    def get_patients_after_diagnosis(self, diagnosis_id) -> List[object]:
        return self._service.get_patients_after_diagnosis(diagnosis_id)

    def get_diagnosis_after_patient(self, patient_id) -> List[object]:
        return self._service.get_diagnosis_after_patient(patient_id)
