from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import PatientMedications


class PatientMedicationsDAO(GeneralDAO):
    _domain_type = PatientMedications

    def get_patients_after_medication(self, medication_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_patients_after_medication(:p1)"),
                                       {'p1': medication_id}).mappings().all()
        return [dict(row) for row in result]

    def get_medications_after_patient(self, patient_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_medications_after_patient(:p1)"),
                                       {'p1': patient_id}).mappings().all()
        return [dict(row) for row in result]
