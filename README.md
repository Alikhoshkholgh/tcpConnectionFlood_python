# tcpConnectionFlood_python
this is multi-thread program and what this does is creating a tcp-connection on a each thread and on a specified time interval send a simple packet to avoid the server to drop the connection

To run this script you should have both AttackModules.py and driver.py in the same directory and then,
run the following:(python version : 3.x)
  python ./driver.py
  
  
Important:
  + in driver.py code you see some important variables which i describe them:
      + target: target IP address
      + port: target port number
      + thread_count: number of connections you want to make 
      + timeInterval: specify that in which time interval each theard in the program should send packets to avoid server to drop the session
      
