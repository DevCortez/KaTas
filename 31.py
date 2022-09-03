# Prison-1 made by Bar0ti https://youtu.be/ZWigbCOMRqs
# Maybe improvable
# Play around with roll lengths and stuff

from katas import Controller, Scripter
script = Scripter()


script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
for k in range (7):
    script.MoveLeftStick(0.6)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.down, duration=1)
    script.Wait(1)
    script.Roll()
    script.Wait(8)
    script.Button(Controller.left_thumb, duration=0)
    script.Wait(3)
    script.Button(Controller.down, duration=0)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.save()

#c-slash timings
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(10)
#script.MoveLeftStick(0)
#script.Button(Controller.X, duration=0)
#script.Wait(11)

#scuffed slow-mo c-slashing timings
#script.MoveLeftStick(0.6)
#script.Button(Controller.X, duration=0)
#script.Wait(11)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(8)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(3)
#script.Button(Controller.down, duration=0)
#script.Wait(1)
#script.Roll()
#script.Wait(10)

#slow-mo roll cancel timings
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(11)
#script.Button(Controller.right, duration=6)
#script.Button(Controller.A, duration=0)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(2)
#script.Button(Controller.down, duration=0)
#script.Wait(2)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()

#Roll cancel on stairs
#script.Button(Controller.right, duration=7)
#script.Button(Controller.A, duration=0)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(3)
#script.Button(Controller.down, duration=2)
#script.Wait(1)
#script.Roll()

#Early wall slide exit into a c-roll
#script.Button(Controller.left, duration=6)
#script.Wait(6)
#script.Button(Controller.right, duration=6)
#script.Button(Controller.down, duration=0)
#script.Wait(2)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
