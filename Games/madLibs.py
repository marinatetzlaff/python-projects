#madLibs
#El lector pregunta por turnos a cada escritor una palabra.
#A continuación el lector utiliza dichas palabras para rellenar los huecos y completar así la historia.

gerundio = input('Por favor, elija un verbo gerundio. ')
lugar = input('Por favor, elija un sustantivo que es un lugar. ')
cancion = input('Por favor, elija una canción navideña. ')
adjetivo = input('Por favor, elija un adjetivo ')
tu_amigo = input('Por favor, elija el nombre de un amigo. ')
gerundio2 = input('Por favor, elija otro gerundio. ')
tiempo = input('Por favor, elija una cantidad de tiempo. ')

madLib =  '''

Estaba %s en el %s el otro día cuando escuché %s en la radio. 
Me sentía realmente %s y estoy bastante seguro de que me veía súper %s porque %s (tu amigo) entró y casi
 %s. ¡En serio, él estuvo %s por cerca de %s!

''' % (gerundio, lugar, cancion, adjetivo, adjetivo, tu_amigo, gerundio2, gerundio2, tiempo)

print(madLib)