from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Doctors(db.Model, IDto):

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'), nullable=False)
    hospital = db.relationship('Hospitals', backref=db.backref('doctors'))
    name = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(255), nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.hospital_id} {self.name} {self.specialization} {self.phone} {self.email}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'hospital_id': self.hospital_id,
            'name': self.name,
            'specialization': self.specialization,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Doctors:
        obj = Doctors(**dto_dict)
        return obj
