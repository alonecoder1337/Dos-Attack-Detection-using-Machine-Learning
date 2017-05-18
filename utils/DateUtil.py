from datetime import datetime
import time


def get_microseconds(date_inst):

    datetime_obj = datetime.strptime(date_inst,'%d-%b-%Y %H:%M:%S')
    return time.mktime(datetime_obj.timetuple())



if __name__=="__main__":
    print get_microseconds('16/Apr/2017 15:48:35.730')
    print get_microseconds('16/Apr/2017 15:49:35.730')