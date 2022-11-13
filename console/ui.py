from datetime import date

from exceptions.validation_exceptions import ValidationExceptions


class Console:
    def __init__(self, events_service):
        self.__events_service = events_service

    def __events_of_the_day(self):
        event_list = self.__events_service.find_today()
        print("Evenimentele ce au loc azi ", date.today(), " sunt: ")
        for event in event_list:
            print(str(event))
    def __add_event(self):
        try:
            date1=input("Introduceti data:")
            hour=input("Introduceti ora:")
            descriere=input("Introduceti descriere:")
            self.__events_service.add_event(date1,hour,descriere)
        except ValidationExceptions as ve:
            print(str(ve))

    def __show_events_by_date(self):
        date1=input("Introduceti data dorita: ")
        events=self.__events_service.find_by_date(date1)
        for event in events:
            print(str(event))

    def __find_by_string(self):
        string=input("Indroduceti stringul:")
        found_list=self.__events_service.sort_by_str(string)
        name=input("Introduceti numele fisierului:")
        self.__events_service.create_file_by_string(name,found_list)

    def show_ui(self):
        self.__events_of_the_day()
        while True:
            print("Welcome")
            print("Adauga")
            print("Afisare evenimente din data")
            print("Cauta string")
            option=input("optioune:")
            if option.lower()=='adauga':
                self.__add_event()
            if option.lower()=='data':
                self.__show_events_by_date()
            if option.lower()=='string':
                self.__find_by_string()


