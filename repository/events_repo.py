from datetime import date

from domain.entities import Eveniment


class FileEventRepo:
    """
    Clasa pentru stocarea evenimentelor in memeorie
    """

    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        functie ce se ocupa cu aducerea elementelor din fisierul text
        :return:lista cu elemenete
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise ValueError
            # creeam eroare

        events = []
        lines = f.readlines()
        for line in lines:
            event_data, event_hour, event_descpritsion = [event.strip() for event in line.split(';')]
            event = Eveniment(event_data, event_hour, event_descpritsion)
            events.append(event)
        f.close()
        return events

    def __save_to_file(self, events_list):
        """
        Functie ce se ocupa cu salvarea evenimentelor in memorie sub forma de string
        :param events_list: lista ce vream sa o salvam in memorie
        :return:-
        """
        with open(self.__filename, 'w') as f:
            for event in events_list:
                event_str = str(event.get_data()) + ';' + str(event.get_ora()) + ';' + str(event.get_descriere()) + '\n'
                f.write(event_str)
        f.close()

    def get_events(self):
        """
        Functie ce returneaza evenimentele din memorie sub forma de lista
        :return: lisat cu evenimente
        :rtype list
        """
        events = self.__load_from_file()
        return events

    def find_today(self):
        """
        Functie ce se ocupa de aflarea evenimentelor ce au loc intr-o zi
        :return:lista cu evenimentele din ziua actuala
        :rtype list
        """
        events = self.__load_from_file()
        events_of_today = []
        today_str="";
        if date.today().day<=9:
            today_str='0'+str(date.today().day)+'.'+str(date.today().month)+'.'+str(date.today().year)
        if date.today().month<=9:
            today_str =  str(date.today().day) + '.' +'0' + str(date.today().month) + '.' + str(date.today().year)
        for event in events:
            if event.get_data() == today_str:
                events_of_today.append(event)

        return events_of_today

    def add_event(self,event):
        events=self.__load_from_file()
        events.append(event)
        self.__save_to_file(events)

    def find_by_date(self,date):
        events = self.__load_from_file()
        events_of_today = []
        for event in events:
            if event.get_data() == date:
                events_of_today.append(event)
        return events_of_today

    def find_by_str(self,string):
        events = self.__load_from_file()
        events_of_str = []
        for event in events:
            if string in event.get_descriere() :
                events_of_str.append(event)
        return events_of_str
