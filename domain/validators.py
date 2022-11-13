from exceptions.validation_exceptions import ValidationExceptions


class EventValidator:
    def validare(self,event):
        errors=[]
        day,mounth,year=[data.strip() for data in event.get_data().split('.')]
        if int(day)>31 or int(day)<0 or int(mounth)>12:
            errors.append("Data nu este buna")

        hour,minute=[data.strip() for data in event.get_ora().split(':')]
        if int(hour)>24 or int(minute)>60:
            errors.append("Ora nu este buna")

        if len(errors)>0:
            error_string = '\n'.join(errors)
            raise ValidationExceptions(error_string)