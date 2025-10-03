from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PatientTrackers(db.Model, IDto):

    __tablename__ = 'patient_trackers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patients', backref=db.backref('patient_trackers'))
    tracker_id = db.Column(db.Integer, db.ForeignKey('trackers.id'), nullable=False)
    tracker = db.relationship('Trackers', backref=db.backref('patient_trackers'))
    measurement_value = db.Column(db.Float, nullable=False)
    measurement_date = db.Column(db.Date, nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.patient_id} {self.tracker_id} {self.measurement_value} {self.measurement_date}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'tracker_id': self.tracker_id,
            'measurement_value': self.measurement_value,
            'measurement_date': self.measurement_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PatientTrackers:
        obj = PatientTrackers(**dto_dict)
        return obj
