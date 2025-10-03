from typing import List

from lab4.app.my_project.auth.dao import patient_medications_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PatientMedicationsService(GeneralService):
    _dao = patient_medications_dao

    def get_patients_after_medication(self, medication_id) -> List[object]:
        return self._dao.get_patients_after_medication(medication_id)

    def get_medications_after_patient(self, patient_id) -> List[object]:
        return self._dao.get_medications_after_patient(patient_id)
