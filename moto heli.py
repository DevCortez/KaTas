# Club-5 10.79 made by Bar0ti https://youtu.be/Eiera5ikpLc
# Guaranteed to be improved
# Find a way to execute laser skip :)

from katas import Controller, Scripter
script = Scripter()

A = 1

script.Button(Controller.left_shoulder, 0)


if A == 1:
    script.Wait(315)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration=0)
    script.Wait(1)
    script.Button(Controller.left, duration=60)
    script.Button(Controller.down, duration=10)
    script.Wait(57)
    script.MoveLeftStick(15)
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
