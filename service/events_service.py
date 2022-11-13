from domain.entities import Eveniment
from exceptions.validation_exceptions import ValidationExceptions


class EventsService:
    """
    Clasa ce se ocupa cu realizarea legaturii dintre memorie si interfata utilizatorului
    """

    def __init__(self, repo_name,validator):
        self.__repo = repo_name
        self.__validator=validator

    def get_events(self):
        """
        Functie ce returneaza evenimentele din memorie sub forma de lista
        :return: lisat cu evenimente
        :rtype list
        """
        return self.__repo.get_events

    def find_today(self):
        """
        Functie ce se ocupa de aflarea evenimentelor ce au loc intr-o zi
        :return:lista cu evenimentele din ziua actuala
        :rtype list
        """
        return self.__repo.find_today()

    def add_event(self,date,hour,year):
        try :
            event=Eveniment(date,hour,year)
            self.__validator.validare(event)
            self.__repo.add_event(event)
        except ValidationExceptions :
            raise ValidationExceptions

    def find_by_date(self,date):
        return self.__repo.find_by_date(date)

    def sort_by_str(self,str):
        """
        Functie ce se ocupa cu sortarea elementelor in functie de data si ora
        :param str: stringul ce vrem sa il gasim
        :return:o  lista sortata
        """
        events_list=self.__repo.find_by_str(str)
        events_list.sort(key=lambda x: (x.get_data(), x.get_ora()))
        return events_list

    def create_file_by_string(self,file_name,list_to_put):
        with open(file_name,'w') as f:
            for event in list_to_put:
                event_str = str(event.get_data()) + ';' + str(event.get_ora()) + ';' + str(event.get_descriere()) + '\n'
                f.write(event_str)
        f.close()