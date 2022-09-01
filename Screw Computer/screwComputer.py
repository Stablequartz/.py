# Two Keyboard Shortcuts Bindings You Will Need To Set For This Python File To Run
# TO OPEN KEYBOARD SHORTCUTS : Ctrl K + Ctrl S

# Search For
# 1. Run Python File
# 2. Kill the Active Terminal Instance

import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for i in range(100000): # Number Of Rotation 
    time.sleep(1)
    screen.rotate_to(i*90 % 360)