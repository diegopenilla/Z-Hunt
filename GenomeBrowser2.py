#!/usr/bin/python
import re
from mechanize import Browser
from lxml import etree
#creamos el objeto principal
br = Browser()
# Para no parecer que somos un robot
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]

#abrimos el link , la idea seria pasarle las variables que el usuario entre eso esta guardado en esta parte del url &c=chr1&l=11187960&r=11192780 , pero no es 1 a 1
#entonces tenes que pillar como le pasas las variables para que te tire el url que es.
br.open( "http://genome-euro.ucsc.edu/cgi-bin/hgc?hgsid=228679405_YauqVRbs3se7WXKkRUqmza9WHl5D&o=11187959&g=getDna&i=mixed&c=chr1&l=11187960&r=11192780&db=hg38&hgsid=228679405_YauqVRbs3se7WXKkRUqmza9WHl5D&submit=get+DNA" )
	
#seleccionamos la form , como solo hay una cogemos la primera
br.form = list(br.forms())[0]
#El usuario mete el input
secuencia = raw_input('Mete la secuencia : ')
#seleccionamos el area de texto, esto es equivalente a escribir en Position
br.form[ 'getDnaPos' ] = secuencia  #'chr1:11,187,960-11,192,780'
#le damos enter , esto es equivalente a darle click al getDna
response = br.submit()
#cogemos el contenido
content = response.get_data()

#lo pasamos a un objeto HTML pa poderle aplicar XPath
tree = etree.HTML(content)
r = tree.xpath("//pre/text()")[0]
#Cuando lo cogemos el coge las new line como \n , entonces las borramos
r.replace("\n", "")

#primera opcion pa quitar la primera linea
f2 = open("input_pal_programa.txt", "w+")
genom = r.strip().splitlines(True)
f2.writelines(genom[1:])
f2.close()

#si no te gusta la opcion de arriba aca te dejo otra
f = open("input_pal_programa2.txt", "w+")
reversed_string = r.strip()[::-1]
inverted_genom = ""
for i in reversed_string:
	if(i == "A" or i == "C" or i == "G" or i == "T"):
		inverted_genom+= i
#hay que invertir el genom otra vez
genom = inverted_genom[::-1]
f.write(genom)
f.close()
