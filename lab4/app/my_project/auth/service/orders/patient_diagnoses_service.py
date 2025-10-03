from typing import List

from lab4.app.my_project.auth.dao import patient_diagnoses_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PatientDiagnosesService(GeneralService):
    _dao = patient_diagnoses_dao

    def get_patients_after_diagnosis(self, diagnosis_id) -> List[object]:
        return self._dao.get_patients_after_diagnosis(diagnosis_id)

    def get_diagnosis_after_patient(self, patient_id) -> List[object]:
        return self._dao.get_diagnosis_after_patient(patient_id)
