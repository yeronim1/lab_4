from typing import List

from lab4.app.my_project.auth.dao import doctors_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class DoctorsService(GeneralService):
    _dao = doctors_dao

    def get_doctors_after_hospital(self, hospital_id) -> List[object]:
        return self._dao.get_doctors_after_hospital(hospital_id)
