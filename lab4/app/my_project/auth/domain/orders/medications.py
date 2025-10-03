from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Medications(db.Model, IDto):

    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(255), nullable=False)


    def __repr__(self) -> str:
        return f"Battery {self.id} {self.name} {self.description} {self.dosage}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'dosage': self.dosage
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Medications:
        obj = Medications(**dto_dict)
        return obj
