import os


class Logs:

    def __init__(self):
        self.log_filename = "/var/log/apache2/custom.log"

    def read(self):
        '''
            Custom Log Format:
                Time
                Client_IP
                Request Method
                Request Status
                Request Size
                Time Taken to Server Request
                User Agent
                Request Header
        '''

        file_data = open(self.log_filename,"r").readlines()
        ds = []
        for line in file_data:
            newline = line.strip().split("::::")
            newline[0] =  " ".join(newline[0].split()[:2])
            ds.append(newline)
        return ds

if __name__=='__main__':
    something = Logs()
    objs = something.read()
