'''
import tello
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('Drone app')
log.info('Starting')


def fly_shape(sides):
    for s in range(sides):
        t.move_forward(20)
        t.rotate_cw(round(360 / sides))


t = tello.Tello('192.168.10.1', 8889)
try:
    t.get_battery()
    t.takeoff()
    fly_shape(3)
except Exception as e:
    log.error(e)
t.land()
t.get_battery()
'''
import telloWrap
import time
# TODO: initiate d object with LOCAL IP and port, **NOT** Tello!!
chris = telloWrap.Tello("192.168.10.2", 8889, timeout=1)

chris.takeoff()
time.sleep(5)
chris.rotate_cw(90)
time.sleep(1)
chris.land()