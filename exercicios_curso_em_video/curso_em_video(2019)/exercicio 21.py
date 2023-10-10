""" faça um programa que abra e reproduza o audio de um
arquivo mp3"""
#1° modo  (erro)
#import pygame
#pygame.init()
#pygame.mixer.music.load('cheiademania.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()
#2° modo
import playsound
playsound.playsound('cheiademania.mp3')
