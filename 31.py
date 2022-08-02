# Prison-1 4.77 + 7.23 made by Bar0ti https://youtu.be/J9nW0Vw8j2s
# Find a new rolling method to be faster :)
# the timing method is bit inaccurate, it's probably off by a few frames

from katas import Controller, Scripter
script = Scripter()


script.Button(Controller.left_shoulder, 0)
script.Wait(2)
script.Button(Controller.down, duration=1)
script.Wait(1)
script.Roll()
script.Wait(10)
for k in range(7):
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
    script.Wait(8)
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.save()

#slow-mo
#script.Button(Controller.left_thumb, duration=0)

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
#script.Button(Controller.down, duration=1)
#script.Wait(3)
#script.Button(Controller.down, duration=1)
#script.Wait(1)
#script.Roll()


