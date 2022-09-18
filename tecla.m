function [lin,Ang] = tecla
    promp="Ingrese movimiento: ";
    tecla = input(promp, "s");
    switch tecla
        case "w"
            lin = 1;Ang=0;
        case "s"
            lin =-1;Ang=0;
        case "a"
            lin = 0;Ang=pi/2;        
        case "d" 
            lin = 0;Ang=-pi/2;
%         case 'r'
%             funcion1;
%         case 'tabulador'
%             funcion2; 
         otherwise
            lin=0;Ang=0;
    end
end



