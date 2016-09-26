#!/usr/sbin/env python
################################################################################
# watch_random - execute a program repeatedly with random intervals.
# Syntax: ./watch_random.py <command> <min_interval> <max_interval>
# Input Arguments:
# command - The command to be executed. If the command contains its own 
#           arguments, put everything in quotation marks.
# min_interval - Minimum interval between subsequent runs.
# max_interval - Maximum interval between subsequent runs.
# Xiaoke Yang <das.xiaoke@gmail.com> Mon 26 Sep 17:16:58 CST 2016
################################################################################
import sys                          # handling command line arguments
from os import system               # call external commands
from random import randrange        # generate random integers
from time import sleep              # delay function
import time
from datetime import date

if (len(sys.argv)!=4):              # only accept 3 arguments
    print ('Syntax: ' + str(sys.argv[0]) + ' command min_interval max_interval. The intervals are in seconds. Put the command within quotation marks if it has its own arguments.')
else:
    min_int = int(sys.argv[2])
    max_int = int(sys.argv[3])
    cmd = sys.argv[1]               # external command
    print(cmd)
    if max_int < min_int:
        print("ERROR: min_interval should be less than or equal to max_interval.")
    else:
        while True:
            system(cmd)             # execute command
            if max_int == min_int:
                delay_int = max_int
            else:
                delay_int = randrange(min_int, max_int+1)
                d = date.today()    # date and time
                d = d.strftime("%d-%m-%Y")
                t = time.strftime("%H:%M:%S")
                print (d + ', ' + t + '. ' + "Delaying ", str(delay_int), " seconds...")
            sleep(delay_int)        # delay
