class Eveniment:
    def __init__(self,data,ora,descriere):
        self.__data=data
        self.__ora=ora
        self.__descriere=descriere

    def get_data(self):
        return self.__data

    def get_ora(self):
        return self.__ora

    def get_descriere(self):
        return self.__descriere

    def __str__(self):
        return "Data: "+str(self.get_data())+" Ora: "+str(self.get_ora())+" Descriere: "+str(self.get_descriere())

    def __iter__(self):
        self.iterPoz=0
        return self