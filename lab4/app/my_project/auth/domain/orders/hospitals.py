from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Hospitals(db.Model, IDto):

    __tablename__ = 'hospitals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    def __repr__(self) -> str:
        return f"Battery {self.id} {self.capacity} {self.installation_date} {self.station_id}"	

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Hospitals:
        obj = Hospitals(**dto_dict)
        return obj
