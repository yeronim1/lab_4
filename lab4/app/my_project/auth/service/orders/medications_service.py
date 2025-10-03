from lab4.app.my_project.auth.dao import medications_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MedicationsService(GeneralService):
    _dao = medications_dao
