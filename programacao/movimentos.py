    """
    Move o robô em linha reta utilizando o giroscópio para corrigir desvios.

    Parâmetros:
        gb         -> objeto DriveBase.
        hub        -> PrimeHub utilizado para acessar o giroscópio.
        distancia  -> distância desejada em milímetros.
        velocidade -> velocidade de deslocamento (mm/s).

    Funcionamento:
        - Zera o odômetro do robô. odômetro = encoder
        - Define a direção (frente ou ré).
        - Mantém o robô alinhado usando correção proporcional
          baseada no erro do giroscópio.
        - Ao final, reduz gradualmente a velocidade para evitar
          ultrapassar a distância desejada (permite que vá mais rápido e dê mais velocidade ao robô).
    """
from pybricks.tools import wait

# Ganhos proporcionais utilizados para correção de trajetória
# e para giros utilizando o sensor giroscópico.
KP_STRAIGHT = 2.2
KP_TURN     = 3.2

#gb = Drive Base (motor_dir, motor_esq...)
def gyroMove(gb, hub, distancia, velocidade = 300):

    gb.reset() #reseta o DriveBase todo (sensor e motores)

    direcao = 1 if distancia > 0 else -1 #se a direção for menor que 1 então é para trás, do contrário vai para frente

    while abs(gb.distance()) < abs(distancia):

        # Diferença entre o ângulo desejado e o atual = erro
        erro = alvo - hub.imu.heading() # exemplo: ângulo desejado = 0, erro -3, (0 - 3 = -3), corrije com o motor +3 para dar 0

        # Correção proporcional para manter o robô reto.
        correcao = erro * KP_STRAIGHT

        gb.drive(velocidade * direcao, correcao)

        wait(10) #delay

    # Desaceleração gradual para aumentar a precisão da parada.
    for v in range(int(velocidade * direcao), 0,
                   -int(velocidade * direcao / 5)):

        erro = alvo - hub.imu.heading()
        correcao = erro * KP_STRAIGHT

        gb.drive(v, correcao)

        wait(10)

    gb.stop()


def gyroTurn(gb, hub, angulo):
    """
    Realiza um giro utilizando o giroscópio.

    Parâmetros:
        gb     -> objeto DriveBase.
        hub    -> PrimeHub utilizado para acessar o IMU.
        angulo -> ângulo desejado em graus.
                  Positivo = direita
                  Negativo = esquerda

    Funcionamento:
        - Calcula o ângulo alvo.
        - Mede continuamente o erro angular.
        - Aplica uma velocidade de giro proporcional ao erro.
        - Encerra quando o erro for menor que 1 grau.
    """

    alvo = hub.imu.heading() + angulo

    while True:

        # Diferença entre o alvo e a orientação atual.
        erro = alvo - hub.imu.heading()

        # Faixa de tolerância para encerrar o giro.
        if abs(erro) < 1: # se o erro for menor que 1 o while para, porque é um erro pequeno demais.
            break

        # Controle proporcional do giro.
        velocidade_giro = erro * KP_TURN

        gb.drive(0, velocidade_giro)

        wait(10)

    gb.stop()
