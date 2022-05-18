from ast import arg
import time, sched
import wave
import simpleaudio as sa
from simpleaudio import PlayObject



def alarm(setTime, alarmSound, message):
    wave_obj = sa.WaveObject.from_wave_file(alarmSound)
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(setTime, 1, print, argument=(message,))
    s.enterabs(setTime, 1, PlayObject(), argument=(wave_obj))
    print('Alarm set for', time.asctime(time.localtime(setTime)))
    s.run()
