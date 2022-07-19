# Kissyface first part 3.97 + several frames made by Bar0ti https://youtu.be/PK-w4UD29so
# Maybe it's possible to be improved
# Try some other stuff with the rolls through kissyface

from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(1)
script.Button(Controller.right, duration=1)
script.Wait(38)
script.Button(Controller.right, duration=1)
script.Wait(115)
script.Button(Controller.right, duration=50)
script.Wait(27)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(22)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(22)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(3)
script.Button(Controller.B, duration=1)
script.Wait(12)

script.save()

