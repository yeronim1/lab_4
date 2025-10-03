from .orders.consultations_controller import ConsultationsController
from .orders.diagnoses_controller import DiagnosesController
from .orders.doctors_controller import DoctorsController
from .orders.hospitals_controller import HospitalsController
from .orders.medications_controller import MedicationsController
from .orders.patient_diagnoses_controller import PatientDiagnosesController
from .orders.patient_medications_controller import PatientMedicationsController
from .orders.patients_controller import PatientsController
from .orders.patient_trackers_controller import PatientTrackersController
from .orders.trackers_controller import TrackersController

consultations_controller = ConsultationsController()
diagnoses_controller = DiagnosesController()
doctors_controller = DoctorsController()
hospitals_controller = HospitalsController()
medications_controller = MedicationsController()
patient_diagnoses_controller = PatientDiagnosesController()
patient_medications_controller = PatientMedicationsController()
patients_controller = PatientsController()
patient_trackers_controller = PatientTrackersController()
trackers_controller = TrackersController()
