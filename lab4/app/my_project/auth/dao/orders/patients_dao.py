from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Patients


class PatientsDAO(GeneralDAO):
    _domain_type = Patients

    def get_patients_after_hospital(self, hospital_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_patients_after_hospital(:p1)"),
                                       {'p1': hospital_id}).mappings().all()
        return [dict(row) for row in result]
