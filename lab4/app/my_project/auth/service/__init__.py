from .orders.consultations_service import ConsultationsService
from .orders.diagnoses_service import DiagnosesService
from .orders.doctors_service import DoctorsService
from .orders.hospitals_service import HospitalsService
from .orders.medications_service import MedicationsService
from .orders.patient_diagnoses_service import PatientDiagnosesService
from .orders.patient_medications_service import PatientMedicationsService
from .orders.patients_service import PatientsService
from .orders.patient_trackers_service import PatientTrackersService
from .orders.trackers_service import TrackersService

consultations_service = ConsultationsService()
diagnoses_service = DiagnosesService()
doctors_service = DoctorsService()
hospitals_service = HospitalsService()
medications_service = MedicationsService()
patient_diagnoses_service = PatientDiagnosesService()
patient_medications_service = PatientMedicationsService()
patients_service = PatientsService()
patient_trackers_service = PatientTrackersService()
trackers_service = TrackersService()
