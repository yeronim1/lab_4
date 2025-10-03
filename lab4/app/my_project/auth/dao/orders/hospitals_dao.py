from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Hospitals


class HospitalsDAO(GeneralDAO):
    _domain_type = Hospitals
