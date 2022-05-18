import time
import simpleaudio as sa



def alarm(setTime, alarmSound, message):
    wave_audio = sa.WaveObject.from_wave_file(alarmSound)
    print("The time is: ", time.time())
    alarmTime = time.time() + float(setTime)
    print("The time is: ", time.time())
    print("The alarm will ring in ", (alarmTime - time.time()), " seconds")
    print("The time is: ", time.time())

    while True:
        if time.time() >= alarmTime:
            for play_obj in range(5):
                wave_audio.play()
                print(message)
                time.sleep(2)
                play_obj
            break
        else:
            print("The time is: ", time.time())
            time.sleep(1)

