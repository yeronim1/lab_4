from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Patients(db.Model, IDto):

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'), nullable=False)
    hospital = db.relationship('Hospitals', backref=db.backref('patients'))
    name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.hospital_id} {self.name} {self.date_of_birth} {self.contact_info}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'hospital_id': self.hospital_id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            "gender": self.gender,
            'contact_info': self.contact_info
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Patients:
        obj = Patients(**dto_dict)
        return obj
