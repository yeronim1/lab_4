from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.consultations_route import consultations_bp
    from .orders.diagnoses_route import diagnoses_bp
    from .orders.doctors_route import doctors_bp
    from .orders.hospitals_route import hospitals_bp
    from .orders.medications_route import medications_bp
    from .orders.patient_diagnoses_route import patient_diagnoses_bp
    from .orders.patient_medications_route import patient_medications_bp
    from .orders.patients_route import patients_bp
    from .orders.patient_trackers_route import patient_trackers_bp
    from .orders.trackers_route import trackers_bp

    app.register_blueprint(consultations_bp)
    app.register_blueprint(diagnoses_bp)
    app.register_blueprint(doctors_bp)
    app.register_blueprint(hospitals_bp)
    app.register_blueprint(medications_bp)
    app.register_blueprint(patient_diagnoses_bp)
    app.register_blueprint(patient_medications_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(patient_trackers_bp)
    app.register_blueprint(trackers_bp)
    
