#imports:
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu

hub = PrimeHub() #cria conexão com o hub

motor_esq = Motor(Port.E, Direction.CLOCKWISE) #sentido horário
motor_dir = Motor(Port.D, Direction.COUNTERCLOCKWISE) #sentido anti-horário
garra_esq = Motor(Port.A, Direction.CLOCKWISE)
garra_dir = Motor(Port.B, Direction.CLOCKWISE)

#variaveis de componentes:
gb = DriveBase(left_motor = motor_esq, right_motor = motor_dir, wheel_diameter = 62.4, axle_track = 146.2)

gb.use_gyro(True) # uso do giroscópio

#configurações de velocidade:
gb.settings(straight_speed = 200, straight_acceleration = 150, turn_rate = 100, turn_acceleration = 200)

# configurações de PID
gb.heading_pid.gains( kp = 380, ki = 6,  kd =42)
gb.distance_pid.gains(kp = 900, ki = 40, kd =35)

hub.display.text("CAL")
wait(2000)

async def calibracao ():
 hub.imu.reset_heading(0)
 motor_esq.reset_angle(0)
 motor_dir.reset_angle(0)
 garra_esq.reset_angle(0)
 garra_dir.reset_angle(0)

calibracao ()
wait (10)

selected = hub_menu("1", "2", "3", "4", "5", "6", "7") # TODAS AS SAÍDAS

if selected == "1":
    import saida1
    saida1.executar(gb, garra_esq, garra_dir, hub)

elif selected == "2":
    import saida2
    saida2.executar(gb, garra_esq, garra_dir, hub)

elif selected == "3":
    import saida3
    saida3.executar(gb, garra_esq, garra_dir, hub)

elif selected == "4":
    import saida4
    saida4.executar(gb, garra_esq, garra_dir, hub)

elif selected == "5":
    import saida5
    saida5.executar(gb, garra_esq, garra_dir, hub)

elif selected == "6":
    import saida6
    saida6.executar(gb, garra_esq, garra_dir, hub)

elif selected == "7":
    import saida7
    saida7.executar(gb, garca_esq, garra_dir, hub)
