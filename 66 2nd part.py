# Kissyface 2nd part 21.27 made by Bar0ti https://youtu.be/8TH6mnpemdE
# Guaranteed to be improvable
# At the very end it should be possible to slash out of the room
# Check other approaches to slashing kissyface

from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(6)
script.MoveLeftStick(240)
script.Button(Controller.X, duration=0)
script.Wait(10)
script.MoveLeftStick(240)
script.Button(Controller.X, duration=140)
script.Wait(157)
script.Button(Controller.left, duration=30)
script.Wait(27)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(271)
script.Button(Controller.X, duration=0)
script.Wait(18)
script.MoveLeftStick(271)
script.Button(Controller.X, duration=180)
script.Wait(179)
script.Button(Controller.right, duration=30)
script.Wait(27)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(20)
script.MoveLeftStick(269)
script.Button(Controller.X, duration=0)
script.Wait(18)
script.MoveLeftStick(269)
script.Button(Controller.X, duration=220)
script.Wait(231)
script.Button(Controller.left, duration=30)
script.Wait(27)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(271)
script.Button(Controller.X, duration=0)
script.Wait(18)
script.MoveLeftStick(271)
script.Button(Controller.X, duration=300)
script.Wait(349)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=1)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=1)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=1)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(2)
script.Button(Controller.A, duration=1)
script.Wait(2)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=1)

script.save()
