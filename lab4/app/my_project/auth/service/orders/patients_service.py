from typing import List

from lab4.app.my_project.auth.dao import patients_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PatientsService(GeneralService):
    _dao = patients_dao

    def get_patients_after_hospital(self, hospital_id) -> List[object]:
        return self._dao.get_patients_after_hospital(hospital_id)
