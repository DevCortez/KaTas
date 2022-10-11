# HH-1 19.46 made by Bar0ti https://youtu.be/2H8HWIzYJxQ
# Maybe improvable
# The second bullet that hits HH is way sooner than the 1st one
# maybe there is that 1 frame early window at which you can hit HH earlier as well on the 1st hit

from katas import Controller, Scripter
script = Scripter()

#Bunker 2-3 script
script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.left, duration=70)
script.Button(Controller.up, duration=11)
script.Wait(82)
script.MoveLeftStick(180)
script.Button(Controller.X, duration=0)
script.Wait(6)
script.Button(Controller.right, duration=180)
script.Wait(80)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(2)
script.Button(Controller.up, duration=27)
script.Wait(160)
script.MoveLeftStick(190)
script.Button(Controller.B, duration=0)
script.Wait(5)
script.MoveLeftStick(300)
script.Button(Controller.X, duration=0)
script.Wait(2)
script.Button(Controller.down, duration=62)
script.Wait(25)
script.MoveLeftStick(260)
script.Button(Controller.X, duration=0)

script.save()
#41
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
