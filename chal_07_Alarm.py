import time, sched
import simpleaudio as sa



def alarm(setTime, alarmSound, message):
    wave_audio = sa.WaveObject.from_wave_file(alarmSound)
    play_obj = wave_audio.play()

    alarmTime = time.time() + float(setTime)
    print("The alarm will ring in ", alarmTime, " seconds")

    while time.time() != alarmTime:
        print("sleeping")
    if time.time() >= alarmTime:
        for play_obj in range(5):
            wave_audio.play()
            print(play_obj)
    
    print(message)


