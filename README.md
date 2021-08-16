# KaTas Scripts Community Repository

This repository is made for storing community's KaTas scripts

# Installation

Download one of KaTas releases from [this post in kc0rtez's Patreon](https://www.patreon.com/posts/54701987).
Extract the archive and put dinput8.dll and KaTas.dll in Katana ZERO game folder. 

To disable KaTas remove or rename dinput8.dll.

# Using KaTas
## .kzt file format

To simulate the inputs KaTas first reads an .kzt input file.
Currently KaTas can only read tas.kzt file inside game's folder.

.kzt file consists of instruction, each with 9 values separated by commas.
```
Example of .kzt file contents

0,1,4096,0,0,0,0,0,0
420,10,2,0,0,0,0,0,0
423,1,16384,0,0,0,0,0,0
437,3,0,0,255,0,0,0,0
```
The values represent: Time when instruction runs, duration of the instruction, button inputs bit mask, left trigger analog value, right trigger analog value, left stick X position, left stick Y postion, right stick X position and right stick Y position.

You can write .kzt input files manually but this approach is slow and inconvenient, because of this, python scripter was made.

## KaTas python script writing

For writing Python KaTas scripts you need:

* Python [(Python download page)](https://www.python.org/downloads/)
* KaTas python script (it's included in KaTas release archive, you can also download it from this repository)



```python
''' Example of python script 
    More can be found in katas.py
'''

# Importing Scripter and Controller classes from KaTas script
from katas import Scripter, Controller

# Scripter object translates commands to .kzt format
script = Scripter()

# Button(buttons, frame=None, duration=1) creates as instruction
# to press `buttons` for `duration` frames starting from frame `frame`
script.Button(Controller.A, duration=10)  # Press A for 10 frames

# Wait(duration) waits for `duration` frames
script.Wait(20)

# MoveLeftStick(deg, frame=None, duration=1) sets left stick's
# degree to `deg` for `duration` frames starting from frame `frame`
script.MoveLeftStick(45, duration=7)

script.Button(Controller.X + Controller.up, duration=12)  # You can press more than 1 button at once!
script.Wait(30)

script.Roll()  # Perform a roll

script.save()  # Save the instructions to tas.kzt file
```

This script will create this .kzt file
```
0,10,4096,0,0,0,0,0,0   Press X for 10 frames starting from frame 0
20,7,0,0,0,23169.767899139606,23169.767899139606,0,0  Set left stick's degree to 45 for 7 frames starting from frame 20
20,12,16385,0,0,0,0,0,0  Press X and DPad Up for 12 frames starting from frame 20
50,1,0,0,255,0,0,0,0  Do a roll on frame 50
```

## Launching the script

KaTas' hotkeys:

* HOME - launches the script "tas.kzt" located within the game's folder.

* END - Toggle infinite execution loop. (tas.kzt script launches again after being completed)