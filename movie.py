  ## PROGRAMA DE PELICULAS DE MARVEL COMICS

import random


class Movies(object): # Se crea la clase movie con atributos de rank y title
    def __init__(self, title):
        self.title = title.lower()
        self.rank = random.randint(0,10) 
        
    def like(self):
        self.rank += 1 #Se incrementa a 1 el rank de movies
        
    def dislike(self):
        self.rank -= 1 #Se disminuye a 1 el rank de movies
    
    def display(self): #Muestra el titulo de la pelicula con la primera letra Mayuscula
      print("Titulo: %-20s Rango: %d" % (self.title.title(),self.rank)) 

pel1 = Movies("Iron Man")
pel2 = Movies("Thor")
pel3 = Movies("The Avengers")
pel4 = Movies("Thor El Mundo Oscuro")
pel5 = Movies("Guardianes de la Galaxia V1")
pel6 = Movies("Vengadores La Era de Ultron")
pel7 = Movies("Capitan America Civil War")
pel8 = Movies("Black Panther")
pel9 = Movies("Avengers Infinity War")
pel10 = Movies("Avengers End Game")

movies= [pel1, pel2, pel3, pel4, pel5, pel6, pel7, pel8, pel9, pel10]

pel8.display()
pel8.like()
pel8.like()
pel8.like()
pel8.display()
pel8.dislike()
pel8.dislike()
pel8.dislike()
pel10.display()
pel10.like()
pel10.like()
pel10.like()
pel10.like()
pel4.display()
pel4.dislike()
pel4.dislike()
pel4.dislike()
pel4.dislike()



