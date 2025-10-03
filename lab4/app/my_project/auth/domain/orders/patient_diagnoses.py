from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PatientDiagnoses(db.Model, IDto):

    __tablename__ = 'patient_diagnoses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patients', backref=db.backref('patient_diagnoses'))
    diagnosis_id = db.Column(db.Integer, db.ForeignKey('diagnoses.id'), nullable=False)
    diagnosis = db.relationship('Diagnoses', backref=db.backref('patient_diagnoses'))
    diagnosis_date = db.Column(db.Date, nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.patient_id} {self.diagnosis_id} {self.diagnosis_date}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'diagnosis_id': self.diagnosis_id,
            'diagnosis_date': self.diagnosis_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PatientDiagnoses:
        obj = PatientDiagnoses(**dto_dict)
        return obj
