from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import PatientDiagnoses


class PatientDiagnosesDAO(GeneralDAO):
    _domain_type = PatientDiagnoses

    def get_patients_after_diagnosis(self, diagnosis_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_patients_after_diagnosis(:p1)"),
                                       {'p1': diagnosis_id}).mappings().all()
        return [dict(row) for row in result]

    def get_diagnosis_after_patient(self, patient_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_diagnosis_after_patient(:p1)"),
                                       {'p1': patient_id}).mappings().all()
        return [dict(row) for row in result]
