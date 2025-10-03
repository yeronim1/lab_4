from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PatientMedications(db.Model, IDto):

    __tablename__ = 'patient_medications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patients', backref=db.backref('patient_medications'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    medication = db.relationship('Medications', backref=db.backref('patient_medications'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    dosage = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Battery {self.id} {self.patient_id} {self.medication_id} {self.start_date} {self.end_date} {self.dosage}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'medication_id': self.medication_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'dosage': self.dosage
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PatientMedications:
        obj = PatientMedications(**dto_dict)
        return obj
