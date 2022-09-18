%% Laboratorio 2: Intro a ROS.   

% Conexión con nodo maestro
rosinit;
%% Creación publicador y mensaje
[velPub,velMsg] = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); 
% Mensaje: Con las teclas 'w' y 's' avanza y retrocede respectivamente y 
%con las teclas 'a' y 'd' gira en sentido horario o antihorario 
%respectivamente.
count=0;
while count < 4 
    [lin,Ang]=tecla; 
    velMsg.Linear.X = lin;
    velMsg.Linear.Y = 0;
    velMsg.Linear.Z = 0;
    velMsg.Angular.X = 0;
    velMsg.Angular.Y = 0;
    velMsg.Angular.Z = Ang;
    % Envio del mensaje
    send(velPub,velMsg); 
    pause(1)
    count=count+1;
end

%% Suscripción al Topico Pose
% El topico pose contiene la posicion 'X,Y'; la orientación 'tetha' y la
% velocidad lineal y angular de la tortuga
posSub = rossubscriber('/turtle1/pose','turtlesim/Pose');
pause(1)
posMsg=receive(posSub); %suscriptor a la espera de que se transmita un mensaje del topico
disp(posMsg)

%%  Envio de nueva pose
%Para actualizar la pose turtle1 cuenta con el servicio 'teleport_absolute'
%para conectar con el servicio matlab cuenta con la funcion 'rossvcclient' 
[nposCl,nposMsg] = rossvcclient('/turtle1/teleport_absolute');
%Modificamos los datos del mensaje con la nueva pose 
nposMsg.X = 1;
nposMsg.Y=1;
nposMsg.Theta=pi/4;
%Enviamos la nueva posición como un servicio de respuesta usando la
%función de matlab 'call' 
nposResp = call(nposCl,nposMsg);
%Verificamos la nueva posición
posMsg=receive(posSub); 
disp(posMsg)

%% Finalizar Nodo
rosshutdown;
