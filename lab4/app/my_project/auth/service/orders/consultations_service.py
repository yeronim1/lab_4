from typing import List

from lab4.app.my_project.auth.dao import consultations_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ConsultationsService(GeneralService):
    _dao = consultations_dao

    def get_consultations_after_patient(self, patient_id) -> List[object]:
        return self._dao.get_consultations_after_patient(patient_id)

    def get_consultations_after_doctor(self, doctor_id) -> List[object]:
        return self._dao.get_consultations_after_doctor(doctor_id)
