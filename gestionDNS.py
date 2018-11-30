import sys

# Abrimos el fichero de configuración y guardamos el contenido
with open('conf.csv', 'r') as c:
   cfg = c.readlines().pop(1).strip('\n').split(',')

# Aquí irá la ruta a nuestro fichero
path = 'prueba'

f = open(path, 'r')

lineas = f.readlines()
f.close()

# Abrimos el fichero con el modo a para que no nos borre todo el contenido que teníamos previamente
f = open(path, 'a')

# Comprobamos los argumentos que le estamos pasando al programa
if sys.argv[1] == '-a':
    # Si los argumentos son -a y -dir, creamos un registro de tipo A
    if sys.argv[2] == '-dir':
        f.writelines(['\n{}.{}\t\tA\t\t{}'.format(sys.argv[3], cfg[0] , sys.argv[4])])
        
    # Si los argumentos son -a y -alias, creamos un registro de tipo CNAME    
    elif sys.argv[2] == '-alias':
        f.writelines(['\n{}.{}\t\tCNAME\t\t{}'.format(sys.argv[3], cfg[0], sys.argv[4])])

    f.close()

elif sys.argv[1] == '-b':
    # Si el argumento es -b, borramos el registro con el nombre que le hayamos pasado
    with open(path, 'w') as fich:
        for linea in lineas:
            if sys.argv[2] not in linea:
                fich.writelines(linea)


