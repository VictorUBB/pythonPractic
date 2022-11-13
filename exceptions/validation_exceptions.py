class EventsExceptions(Exception):
    pass

class ValidationExceptions(EventsExceptions):
    def __init__(self,msg):
        self.__msg=msg

    def getMsg(self):
        return self.__msg

    def __str__(self):
        return "Validation Exception: "+str(self.getMsg())

class RepoExceptions(EventsExceptions):
    def __init__(self, msg):
        self.__msg = msg

    def getMsg(self):
        return self.__msg

    def __str__(self):
        return "Validation Exception: " + str(self.getMsg())

class CorruptedFileExcception(RepoExceptions):
    def __init__(self):
        RepoExceptions.__init__("Corrupted File")

