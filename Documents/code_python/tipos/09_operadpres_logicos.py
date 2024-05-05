#and, orn , not
gas= False
encendido = True
edad = 19 

if gas and encendido:
    print("Todo esta bien") # anbos tienes quer ser verdaderos and

if gas or encendido:
    print("Todo esta bien") #uno de los dos tiene que ser verdadero or

if not gas and (encendido or edad > 18):
    print("puedes avanzar") #not es lo contrario de lo que esta en la variable

