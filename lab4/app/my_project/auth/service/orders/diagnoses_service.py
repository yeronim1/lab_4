from lab4.app.my_project.auth.dao import diagnoses_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class DiagnosesService(GeneralService):
    _dao = diagnoses_dao
