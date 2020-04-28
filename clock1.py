import time
from turtle import *
setup()
a1 = Turtle()


the_seconds_hand = 57
the_minute_hand = 58
the_hour_hand = 9

while True: #otherwise (1==1)
    a1.clear()
    a1.write(str(the_hour_hand).zfill(2)  + ":" + str(the_minute_hand).zfill(2) + ":" + str(the_seconds_hand).zfill(2),font = ("arial",90,"normal"))
    the_seconds_hand = the_seconds_hand + 1
    time.sleep(1)
    if the_seconds_hand == 60:
        the_seconds_hand = 0
        the_minute_hand = the_minute_hand + 1
    if the_minute_hand == 60:
        the_minute_hand = 0
        the_hour_hand = the_hour_hand + 1


