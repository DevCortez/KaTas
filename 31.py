# Prison-1 made by Bar0ti https://youtu.be/ZWigbCOMRqs
# Maybe improvable
# Play around with roll lengths and stuff

from katas import Controller, Scripter
script = Scripter()



#Club-7 script
script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0.8)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(0.453)
script.Button(Controller.X, duration=0)
script.Wait(4)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(9)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(5)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.B, duration=0)
script.Wait(1)
script.Button(Controller.right, duration=2)
script.Button(Controller.A, duration=0)
script.Button(Controller.left_thumb, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=16)
script.Button(Controller.left, duration=20)
script.Wait(23)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(4)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.MoveLeftStick(179.453)
script.Button(Controller.X, duration=0)
script.Wait(7)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(179.2)
script.Button(Controller.X, duration=0)
script.Wait(11)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(9)
script.MoveLeftStick(176)
script.Button(Controller.X, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(8)
script.MoveLeftStick(179.54)
script.Button(Controller.X, duration=0)
script.Wait(4)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(11)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.left, duration=7)
script.Button(Controller.A, duration=0)
script.Button(Controller.left_thumb, duration=0)
script.Wait(3)
script.Button(Controller.down, duration=2)
script.Wait(1)
script.Roll()
script.Wait(10)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(5)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()


script.Wait(472)
script.Button(Controller.X, duration=0)

#Prison-1 script
script.Wait(1)
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
