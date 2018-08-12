###################################################
# CLI Kajataca para Gestionar Actividades en PC   #
###################################################
import sys 
from clases.Menu import *

menu = Menu()


if( len(sys.argv) < 2 ):

	opcion = ''

	while opcion != 'exit' and  opcion != 'salir' :
		opcion = menu.principal()

	
else:
	menu.add_argumentos( sys.argv ) 
	menu.lanzar_evento()

