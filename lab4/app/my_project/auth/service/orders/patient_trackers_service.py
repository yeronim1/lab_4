from typing import List

from lab4.app.my_project.auth.dao import patient_trackers_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PatientTrackersService(GeneralService):
    _dao = patient_trackers_dao

    def get_patients_after_tracker(self, tracker_id) -> List[object]:
        return self._dao.get_patients_after_tracker(tracker_id)

    def get_trackers_after_patient(self, patient_id) -> List[object]:
        return self._dao.get_trackers_after_patient(patient_id)
