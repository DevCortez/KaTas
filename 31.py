# Prison 1 - 12.17

from katas import Scripter, Controller

script = Scripter()
script.Button(Controller.A)
script.Wait(60*7) # This is innacurate, should be counted in actual frames instead
script.Button(Controller.down, duration=10)
script.Wait(3)
script.Button(Controller.X)
script.AddRawAction(437, 3, rt=0xFF) # the waits should align to this
script.Wait(1)

for _ in range(13):
    script.Wait(10)
    script.Button(Controller.X)
    script.Wait(11)
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()

script.save()