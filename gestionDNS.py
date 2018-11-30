import os

# Si el script recibe -a, se añadirá el nombre que recibe
# Si el script recibe -b, se borrará el nombre que recibe 

# Aquí irá la ruta a nuestro fichero
path = 'prueba'

# Abrimos el fichero con el modo a+ para que no nos borre todo el contenido que teníamos previamente
f = open(path, 'a+')

# Comprobamos los argumentos que le estamos pasando al programa
if sys.argv[1] == '-a':
    # Si los argumentos son -a y -dir, creamos un registro de tipo A
    if sys.argv[2] == '-dir':
        f.writelines(['\n{}\t\tA\t\t{}'.format(sys.argv[3], sys.argv[4])])
    # Si los argumentos son -a y -alias, creamos un registro de tipo CNAME    
    elif sys.argv[2] == '-alias':
        f.writelines(['\n{}\t\tCNAME\t\t{}'.format(sys.argv[3], sys.argv[4])])
