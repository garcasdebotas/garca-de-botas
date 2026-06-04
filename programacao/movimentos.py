from pybricks.tools import wait

KP_STRAIGHT = 1.8  #correção de ângulos para frente
KP_TURN     = 3.2  # correção de ângulos para curvas

def gyroMove(gb, hub, distancia, velocidade = 300): # velocidade 300 como padrão, parâmetros do robô:
    """
    gb = DriveBase: motores e sensores
    hub = giroscópio
    distância = variavel do .strenght (distância = em milímetros)
    velocidade = tempo que algo leva para ir de um ponto A até B
    """
    gb.reset() # reset nos sensores e nos motores.
    
    alvo = hub.imu.heading() # grava o heading no momento do reset
    
    direcao = 1 if distancia > 0 else -1 # +1 = frente, -1 = ré


    # correção contante com o while:
    while abs(gb.distance()) < abs(distancia):
        erro = alvo - hub.imu.heading() # desvio em graus

        correcao = erro * KP_STRAIGHT

        gb.drive(velocidade * direcao, correcao)

        wait(10)

    passo = max(1, int(velocidade / 5))

    for desaceleracao_gradual in range(int(velocidade), 0, -passo):
        erro = alvo - hub.imu.heading()
        
        correcao = erro * KP_STRAIGHT
        
        gb.drive(desaceleracao_gradual, * direcao, correcao)
        
        wait(10)

    gb.stop()

def gyroTurn(gb, hub, angulo, velocidade_giro = 100, tolerancia = 1):

    alvo = hub.imu.heading() + angulo

    while True:
        erro = alvo - hub.imu.heading()

        if abs(erro) < tolerancia:         
            break

        # Velocidade proporcional ao erro: freia suavemente ao se aproximar
        velocidade_atual = erro * KP_TURN

        gb.drive(0, velocidade_atual)
        
        wait(10)

    gb.stop()
