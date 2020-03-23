#! python3
# countdown.py: a simple countdown script

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft -1

# at the end of the countdown, play sound file

subprocess.Popen(['start', 'alarm.wav'], shell=True)
