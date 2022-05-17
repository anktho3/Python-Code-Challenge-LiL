import time
from random import randint

def waiting_game():
    selectedTime = randint(2, 5)
    print("Your target time is " + str(selectedTime) + " seconds.")
    input("---Press Enter to Begin---")
    timeStarted = time.time_ns()
    input(f"\n...Press Enter again after {selectedTime} seconds...")
    timeEnded = time.time_ns()

    timeWaited = (timeEnded - timeStarted) / 1000000000

    if timeWaited < selectedTime:
        print(f"Elapsed time: {timeWaited:.3f} seconds")
        print(f"{selectedTime - timeWaited:.3f} too fast")
    elif timeWaited > selectedTime:
        print(f"Elapsed time: {timeWaited:.3f} seconds")
        print(f"{timeWaited - selectedTime:.3f} too slow")
    elif timeWaited == selectedTime:
        print(f"Elapsed time: {timeWaited:.3f} seconds")
        print("Exact!")

waiting_game()

