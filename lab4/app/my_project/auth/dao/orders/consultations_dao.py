from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Consultations


class ConsultationsDAO(GeneralDAO):
    _domain_type = Consultations

    def get_consultations_after_patient(self, patient_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_consultations_after_patient(:p1)"),
                                       {'p1': patient_id}).mappings().all()
        return [dict(row) for row in result]

    def get_consultations_after_doctor(self, doctor_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_consultations_after_doctor(:p1)"),
                                       {'p1': doctor_id}).mappings().all()
        return [dict(row) for row in result]
