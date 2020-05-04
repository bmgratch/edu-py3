#! python3
# stopwatch.py - A simple stopwatch program

import time, pyperclip

# display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.  Press Ctrl-C to quit.')
input()
print('Started!')
startTime = time.time()     # get the first lap's start time.
lastTime = startTime
lapNum = 1
lapFull = ''

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lapText = ('Lap #%s:' % lapNum).ljust(8)+ str(totalTime).rjust(6) + ' (' + str(lapTime).rjust(6)+ ')'
        print (lapText, end='')
#        print(('Lap #%s:' % lapNum).ljust(8), str(totalTime).rjust(5) + ' (', str(lapTime).rjust(4)+ ')', end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time.
        lapFull+= lapText + '\n'
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    pyperclip.copy(lapFull)
    print('Full records transfered to your clipboard!')
