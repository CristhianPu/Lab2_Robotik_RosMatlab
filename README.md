
# Laboratorio 2: Introducción a ROSY
## A. Comandos de Linux
Revisando el libro de Mark G. Sobell, "A Practical Guide to Linux Commands,Editors and Shell Programming" resaltan los siguientes comandos:
* `comando --help` Obtener ayuda acerca de un comando.
* `ls` Ver el contenido de la ruta actual o la que se especifique. "ls Downloads" 
* `cp` Copiar un archivo.
* `echo` mostrar texto
* `bzip2`,`bunzip2` Comprimir y Descomprimir archivos.
* `mkdir` Crear un directorio.
* `cd` Moverse entre directorios. "cd Downloads" "cd ..".
* `su/sudo` Priviligios de administrador.

Existen muchos otros comandos de consola, pero estos son comandos para empezar a familiarizarse con el entorno de linux.

## B. Conexion ROS y Matlab

Creado el nodo con los comandos `roscore` y `rosrun turtlesim turlesim_node` cada uno en una terminal, luego abrir y correr el archivo `Lab2.m`.
En este codigo primero se realiza la conexión a matlab con el comando `rosinit`; luego, para hacer mover la torutuga se usa el topico `cmd_vel` y se usa el comando de matlab `rospublisher` para crear el publicador y el mensaje del topico. Este mensaje se puede modificar para actualizar la velocidad lineal y angular en cada eje X, Y, Z, segun se requiera y se envia con el comando `send`. Para este caso se ajusto el movimiento a las teclas como se muestra en el siguiente punto del taller.

Para conocer la posición de la tortuga se tiene el topico `pose`, pero este solo permite conocer la posición y orientación de la torutuga, es decir suscribirse usando el comando de matlab 'rossubscriber', para modificar la posición se tiene el servicio 'teleport_absolute', pero como se trata de un servicio, para acceder es necesario crear un cliente usando el comando de matlab `rossvcclient` y enviar un mensaje con la posición actualizada con el comando 'call'. 

##C. Implementación en Python

Para la segunda parte del laboratorio se requiere escribir un código en Python que permita operar una tortuga del paquete turtlesim con el teclado,
cumpliendo las siguientes especificaciones:

* Se debe mover hacia adelante y hacia atrás con las teclas W y S
* Debe girar en sentido horario y antihorario con las teclas D y A.
* Debe retornar a su posición y orientación centrales con la tecla R
* Debe dar un giro de 180° con la tecla ESPACIO

### Reconocer entradas del teclado 

Se inicia instalando el paquete **pynput.keyboard** el cual contiene clases para controlar y monitorear el teclado. **pynput** es la biblioteca de Python que se puede usar para capturar entradas de teclado. Para realizar la instalación de esta libreria se ejecuta el siguiente comando desde la terminal:
```console
pip install pynput 
```
Es probable que no se encuentre la orden «pip», pero se puede instalar ejecutando el comando:
```console
sudo apt install python3-pip
```
 ### Ejecución del código
 Se requiere abrir tres terminales y ejecutar los siguientes comandos:
 #### Primer terminal
 Es el nodo maestro, el cual lanza los nodos requeridos para el funcionamiento de ROS 
 ```console
roscore
```
  #### Segundo terminal
 Lanza el nodo de la tortuga, contenido en el paquete de turtlesim, este paquete viene instalado por defecto con los demás paquetes de ROS 
 ```console
rosrun turtlesim turtlesim_node
```
#### Tercer terminal 
 Por ultimo se ejecuta el programa de Python llamado myTeleopKey.py, **es necesario que la terminal se abra dentro de la carpeta que contiene el archivo**, esto se puede hacer especificando la ruta de la carpeta o abriendo la carpeta y eligiendo la opción de "Abrir en una terminal" que aparece al dar click derecho al interior de la carpeta

 ```console
python myTeleopKey.py
```
Se debe abrir una terminal
### Explicación del código 
