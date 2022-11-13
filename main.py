from datetime import date

from console.ui import Console
from domain.validators import EventValidator
from repository.events_repo import FileEventRepo
from service.events_service import EventsService

Events_repo=FileEventRepo('data/events')
Validator=EventValidator()
Events_service=EventsService(Events_repo,Validator)
ui=Console(Events_service)

ui.show_ui()
