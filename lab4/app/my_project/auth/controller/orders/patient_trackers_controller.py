from typing import List

from lab4.app.my_project.auth.service import patient_trackers_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PatientTrackersController(GeneralController):

    _service = patient_trackers_service

    def get_patients_after_tracker(self, tracker_id) -> List[object]:
        return self._service.get_patients_after_tracker(tracker_id)

    def get_trackers_after_patient(self, patient_id) -> List[object]:
        return self._service.get_trackers_after_patient(patient_id)
