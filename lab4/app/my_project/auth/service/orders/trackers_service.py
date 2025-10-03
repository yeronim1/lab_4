from lab4.app.my_project.auth.dao import trackers_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class TrackersService(GeneralService):
    _dao = trackers_dao
