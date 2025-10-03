from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import PatientTrackers


class PatientTrackersDAO(GeneralDAO):
    _domain_type = PatientTrackers

    def get_patients_after_tracker(self, tracker_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_patients_after_tracker(:p1)"),
                                       {'p1': tracker_id}).mappings().all()
        return [dict(row) for row in result]

    def get_trackers_after_patient(self, patient_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_trackers_after_patient(:p1)"),
                                       {'p1': patient_id}).mappings().all()
        return [dict(row) for row in result]
