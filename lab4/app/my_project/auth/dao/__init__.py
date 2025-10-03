from .orders.consultations_dao import ConsultationsDAO
from .orders.diagnoses_dao import DiagnosesDAO
from .orders.doctors_dao import DoctorsDAO
from .orders.hospitals_dao import HospitalsDAO
from .orders.medications_dao import MedicationsDAO
from .orders.patient_diagnoses_dao import PatientDiagnosesDAO
from .orders.patient_medications_dao import PatientMedicationsDAO
from .orders.patients_dao import PatientsDAO
from .orders.patient_trackers_dao import PatientTrackersDAO
from .orders.trackers_dao import TrackersDAO

consultations_dao = ConsultationsDAO()
diagnoses_dao = DiagnosesDAO()
doctors_dao = DoctorsDAO()
hospitals_dao = HospitalsDAO()
medications_dao = MedicationsDAO()
patient_diagnoses_dao = PatientDiagnosesDAO()
patient_medications_dao = PatientMedicationsDAO()
patients_dao = PatientsDAO()
patient_trackers_dao = PatientTrackersDAO()
trackers_dao = TrackersDAO()
