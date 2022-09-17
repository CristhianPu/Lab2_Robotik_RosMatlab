import rospy  # ROS libraries
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportRelative, TeleportAbsolute
from std_srvs.srv import Empty
from pynput.keyboard import Key, Listener, KeyCode  # keyboard input
import numpy as np


class myTeleopkey():

    def __init__(self):

         # Print de comandos
        welcome = """\n Presiona las teclas para desplazar la tortuga

            * Space: Giro 180°
            * W: Mover adelante
            * S: Mover atrás
            * A: Giro horario
            * D: Giro antihorario        
            * C: Limpia la trayectoria
            * R: Vuelve a posición inicial
                  """
        rospy.loginfo(welcome)

        # Se detecta y almacena como una variable la tecla presionada
        self.keysPressed = set()
        listener = Listener(on_press=self.onPress, on_release=self.onRelease)
        listener.start()

        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            linear = 0
            angular = 0

            # Las teclas W S A D aumentan o decrecen la velocidad lineal y angular
            if KeyCode.from_char('w') in self.keysPressed:
                linear += 1

            if KeyCode.from_char('s') in self.keysPressed:
                linear -= 1

            if KeyCode.from_char('a') in self.keysPressed:
                angular += np.pi/2

            if KeyCode.from_char('d') in self.keysPressed:
                angular -= np.pi/2

            # Se publica la velocidad
            self.pubVel(linear, angular)
            rate.sleep()

            # La tecla espacio realiza una rotación relativa
            if Key.space in self.keysPressed:
                rospy.wait_for_service('/turtle1/teleport_relative')
                try:
                    rotateTurtle = rospy.ServiceProxy(
                        '/turtle1/teleport_relative', TeleportRelative)
                    moveRsp = rotateTurtle(0, np.pi)                    
                except rospy.ServiceException as e:
                     print(str(e))

           # La tecla r realiza un movimiento absoluto
            if KeyCode.from_char('r') in self.keysPressed:
                rospy.wait_for_service('/turtle1/teleport_absolute')
                try:
                    teleportA = rospy.ServiceProxy(
                        '/turtle1/teleport_absolute', TeleportAbsolute)
                    resp1 = teleportA(5.5, 5.5, 0)
                    print('Teleported to home')
                except rospy.ServiceException as e:
                    print(str(e))

              # La tecla C limpia la trayectoria realizada
            if KeyCode.from_char('c') in self.keysPressed:
                try:
                     rospy.wait_for_service('clear')
                     clear_bg = rospy.ServiceProxy('/clear', Empty)
                     clear_bg()
                     print('Limpiar trayectoria')
                except rospy.ServiceException as e:  
                     print(str(e))
                                  
      # Funciones para detectar tecla precionada   
    def onPress(self, key):
        print("\033[A")  # Borra en la tecla impresa en la terminal 
        self.keysPressed.add(key) 
    def onRelease(self, key):
        self.keysPressed.remove(key)

     # Funcion para publicar velocidad   
    def pubVel(self, linear, angular): 
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        pub.publish(msg)
    
if __name__ == "__main__":
    # Inicializa el nodo y ejecuta  myTeleopkey()
    rospy.init_node('TeleopKey', anonymous=False)
    myTeleopkey()
