# Bunker 1-8 8.75 made by Bar0ti https://youtu.be/g3p8f3xxDL4
# Unlikely to be improved
# Play around with the end or maybe SCSCSC timings


from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
for k in range (6):
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
script.Wait(4)
script.Button(Controller.Y, duration=0)
script.Wait(7)
script.Button(Controller.right, duration=8)
script.Wait(4)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
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
#script.MoveLeftStick(0.8)
#script.Button(Controller.X, duration=0)
#script.Wait(11)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()
#script.Wait(10)
#script.Button(Controller.left_thumb, duration=0)
#script.Wait(3)
#script.Button(Controller.down, duration=1)
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
