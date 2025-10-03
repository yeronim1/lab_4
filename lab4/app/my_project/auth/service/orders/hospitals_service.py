from lab4.app.my_project.auth.dao import hospitals_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class HospitalsService(GeneralService):

    _dao = hospitals_dao
    