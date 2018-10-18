import pygame,sys
from pygame.locals import *
import random

pygame.init()
pygame.display.set_caption("Retrocar game.v.1.0")
pantalla = pygame.display.set_mode((400, 700))
color_fondo = pygame.Color(250,250,250)
color2 = pygame.Color(200,200,70)
velocidad = 6
reloj = pygame.time.Clock()

class Pista():
	def __init__(self):
		self.x=0
		self.x2=350
		self.y=1
		self.y2=0
		self.y3=0
		self.speed = 0.1
	def dibujar(self,lado,time):
		pygame.draw.rect(pantalla,(color2),(lado,self.y-200,50,100))#colores,coord,dimensiones
		self.y += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y,50,100))
		self.y += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y+200,50,100))
		self.y += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y+400,50,140))
		self.y += self.speed * time

	def dibujar2(self,lado,time):
		pygame.draw.rect(pantalla,(color2),(lado,self.y2-800,50,100))
		self.y2 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y2-600,50,100))
		self.y2 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y2-400,50,100))
		self.y2 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y2-200,50,100))
		self.y2 += self.speed * time

	def dibujar3(self,lado,time):
		pygame.draw.rect(pantalla,(color2),(lado,self.y3-800,50,100))
		self.y3 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y3-600,50,100))
		self.y3 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y3-400,50,100))
		self.y3 += self.speed * time
		pygame.draw.rect(pantalla,(color2),(lado,self.y3-200,50,60))
		self.y3 += self.speed * time

class Carrito():
	def __init__(self):
		self.imagen = pygame.image.load("img/car2.png")
		self.rect = self.imagen.get_rect()
		self.rect.x=150
		self.rect.y= 540
	def actualizar(self,time):
		if self.rect.right >= 370:
			self.rect.centerx -= 25
		if self.rect.left <= 30:
			self.rect.centerx += 25

class Competidor():
	def __init__(self,numero):
		self.imagen = pygame.image.load("img/car.png")
		self.rect = self.imagen.get_rect()
		self.rect.x =numero
		self.rect.y = -200
		self.speed = -0.1
	def dibujar(self,time):
		pantalla.blit(self.imagen,self.rect)
		competidor.actualizar(time)
	def actualizar(self,time):
		self.rect.y -= self.speed * time
	def colision(self, objetivo):
		if self.rect.colliderect(objetivo.rect):
			pygame.time.wait(200)
			frente.reiniciar=True

class Frente():
	def __init__(self):
		self.fuente = pygame.font.Font(None, 30)
		self.puntos =0
		self.x=250
		self.y=0
		self.iniciar=False
		self.reiniciar=False
	def puntaje(self):
		pygame.draw.rect(pantalla,(0,0,0),(self.x,self.y,150,60))
		puntos = self.fuente.render(" "+str(self.puntos), 3, (255, 255, 255))
		pantalla.blit(puntos, (320,20))
	def iniciar_game(self):
		mensaje2=self.fuente.render("Click para empezar", 1, (5,25,255))
		pantalla.blit(mensaje2, (100,400))

pista=Pista()
frente=Frente()
carrito=Carrito()
competidor=Competidor(150)
pygame.key.set_repeat(1, 25)  # Activa repeticion de teclas
#pygame.mouse.set_visible(True) #Visibilidad del puntero mouse

while True:
	pantalla.fill(color_fondo)
	frente.iniciar_game()
	pantalla.blit(carrito.imagen,carrito.rect)
	carrito.actualizar(50)
	competidor.colision(carrito)
	frente.puntaje()
	if frente.iniciar==True:
		frente.puntos=frente.puntos+1
		pantalla.fill(color_fondo)
		pantalla.blit(carrito.imagen,carrito.rect)
		carrito.actualizar(50)
		if pista.y>0:	
			pista.dibujar(pista.x,velocidad)
			pista.dibujar(pista.x2,velocidad)
			ubicacion_random=random.uniform(40,280)
			if pista.y>200:
				pista.dibujar2(pista.x,velocidad)
				pista.dibujar2(pista.x2,velocidad)
				competidor.dibujar(50)
				if pista.y>400:
					pista.dibujar3(pista.x,velocidad)
					pista.dibujar3(pista.x2,velocidad)
					if pista.y>1004:
						pista.y=1
						pista.y2=0
						pista.y3=0
						competidor=Competidor(ubicacion_random)

		frente.puntaje()

	if frente.reiniciar==True:
		pista=Pista()
		frente=Frente()
		carrito=Carrito()
		competidor=Competidor(150)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			frente.iniciar=True
		elif event.type == pygame.KEYDOWN:
			if event.key == K_RIGHT:
				carrito.rect. centerx += 25
			elif event.key == K_LEFT:
				carrito.rect.centerx -= 25
			elif event.key == K_UP:
				frente.reiniciar=True
			elif event.key == K_ESCAPE:
				sys.exit(0)

	pygame.display.flip()
