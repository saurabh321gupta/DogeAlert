import time

from pushbullet import Pushbullet

while(True):
    Pushbullet("o.IH0xSegxyprlnyGm3Qdnx9ZvlKrcnL6c").push_note('Hi,', 'this is an alert!')
    time.sleep(10)