# Laboratorio 2: Introducción a ROS
## A. Comandos de Linux
Revisando el libro de Mark G. Sobell, "A Practical Guide to Linux Commands,Editors and Shell Programming" se tiene que los comandos mas usado son:
* `cd` Moverse entre directorios. "cd Downloads" "cd ..".
* ls Ver el contenido de la ruta actual o la que se especifique. "ls Downloads" 
* comando --help Obtener ayuda acerca de un comando.

## B. Conexion ROS y Matlab


## C. Implementación en Python
Para la segunda parte del laboratorio se requiere escribir un código en Python que permita operar una tortuga del paquete turtlesim con el teclado,
cumpliendo las siguientes especificaciones:
* Se debe mover hacia adelante y hacia atrás con las teclas W y S
* Debe girar en sentido horario y antihorario con las teclas D y A.
* Debe retornar a su posición y orientación centrales con la tecla R
* Debe dar un giro de 180° con la tecla ESPACIO
* Adicionalmente: Limpia la trayectoria con la letra C

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
 https://github.com/CristhianPu/Lab2_Robotik_RosMatlab/issues/2#issue-1377172208
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
Una vez ejecutado este ultimo comando debe desplegarse el siguiente menu:
### Explicación del código 
