from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Consultations(db.Model, IDto):

    __tablename__ = 'consultations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patients', backref=db.backref('consultations'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    doctor = db.relationship('Doctors', backref=db.backref('consultations'))
    consultation_date = db.Column(db.Date, nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.String(255), nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.patient_id} {self.doctor_id} {self.consultation_date} {self.diagnosis} {self.notes}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'consultation_date': self.consultation_date,
            'diagnosis': self.diagnosis,
            'notes': self.notes
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Consultations:
        obj = Consultations(**dto_dict)
        return obj
