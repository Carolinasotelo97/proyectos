import pygame
import sys

pygame.init() #inicializo pygame
pantalla_x = 800
pantalla_y = 600
size = (pantalla_x, pantalla_y)
screen = pygame.display.set_mode(size) #creo la ventana del juego de 800px x 600px
punto_X_circulo = 250
punto_y_circulo = 80
punto_X_cuadrado= pantalla_x//2
punto_y_cuadrado = 400
clock = pygame.time.Clock() #se encarga de contar los fps del juego
direccion = 1 #si es 1 mueve hacia la derecha, si es 2 se mueve a la izquierda
direccion_c = 1
'''
Guia de colores:
color_rojo = (255,0,0)
color_verde= (0,255,0)
color_azul =(0,0,255)
color_blanco = (255,255,255)
color_negro = (0,0,0)'''

while True:
    for event in pygame.event.get(): #le digo que todos los eventos de pygame se guarden en event
        #print(event) #para saber que evento se esta ejecutando
        if event.type == pygame.QUIT: #si hago click en cerrar
            sys.exit() #sali

    screen.fill((210, 180, 222)) #los colores son rgb
    pygame.draw.line(screen,(255,0,0),[0,0],(size), 5)
    #pygame.draw.line(screen,(255,0,0),[size[0], 0],[0,size[1]], 10)
    pygame.draw.rect(screen,(0,255,0),(punto_X_cuadrado,punto_y_cuadrado,100,100)) #rect(pantalla_x, pantalla_y, ancho, alto) el doble pipe el resultado me da int


    pygame.draw.circle(screen, (0,0,255),(punto_X_circulo, punto_y_circulo),50)

    if direccion == 1:
         punto_X_circulo +=5
    else:
        punto_X_circulo -= 5

    if punto_X_circulo + 50 >= pantalla_x: #50 es por el radio del circulo
        direccion = 2
    if punto_X_circulo - 50 <= 0:
        direccion = 1

    if direccion_c == 1:
        punto_y_cuadrado -=5 #como esta en el cuadrante 4, si quiero que vaya para arriba, le tengo que sacar valores a y
    else:
        punto_y_cuadrado += 5
    
    if punto_y_cuadrado + 100 >= pantalla_y: #el punto del cuadraro + 100 da el total del cuadrado
        direccion_c = 1
    if punto_y_cuadrado <= 0:
        direccion_c =2
    pygame.display.flip() 
    clock.tick(35) #cantidad de fps