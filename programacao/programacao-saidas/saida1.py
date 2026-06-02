from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from movimentos import gyroMove

DISTANCIA_AVANCO = 300

DISTANCIA_RECUO = -300

ANGULO_GARRA_ABERTA = 60
ANGULO_GARRA_FECHADA = 0

VELOCIDADE_GARRA = 400

KP = 120
KI = 10
KD = 5

def executar(gb, garra_esq, garra_dir, hub):
    
    hub.display.number(1) #mostra no hub o número da saída

    #reseta os valores:
    garra_esq.reset_angle(0)
    garra_dir.reset_angle(0)

    # variaveis do PID:
    garra_esq.control.pid(kp = KP, ki = KI, kd = KD)
    garra_dir.control.pid(kp = KP, ki = KI, kd = KD)

    # limites da garra esquerda 
    garra_esq.control.limits  (speed=VELOCIDADE_GARRA, acceleration = 300)

    # limites da garra direita 
    garra_dir.control.limits( speed = VELOCIDADE_GARRA,acceleration = 300)

    gyroMove(gb, hub, DISTANCIA_AVANCO, velocidade = 300)

    garra_esq.run_target(VELOCIDADE_GARRA, ANGULO_GARRA_ABERTA, then=Stop.HOLD, wait=True)
    
    wait(100)
    # volta para o ponto original:
    gyroMove (gb, hub, DISTANCIA_RECUO, velocidade = 300)
    
    # FECHA GARRA
    garra_esq.run_target(VELOCIDADE_GARRA, ANGULO_GARRA_FECHADA, then=Stop.HOLD, wait=True)

    wait (100)
