# HH1 14.73s made by snek pliskin (https://youtu.be/sxuICNiLgWg)


from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(2)

#crouch roll
script.Button(Controller.down, duration = 0)
script.Wait(1)
script.Roll()
script.Wait(3)

#two crunchy slashes to HH
for i in range(2):
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration=0)
    script.Wait(11)

#go to right
script.Wait(23)
script.Button(Controller.right, duration = 50)

#slash right gunner
script.Wait(78)
script.MoveLeftStick(269)
script.Button(Controller.X, duration = 0)
script.Wait(2)
script.Button(Controller.down, duration = 0)

#roll through bullet 1
script.Wait(75)
script.Roll()
script.Wait(1)
script.Button(Controller.A, duration = 0)
script.Wait(5)
script.Button(Controller.down, duration = 0)

#roll throught bullet 2
script.Wait(2)
script.Button(Controller.left, duration = 12)
script.Wait(12)
script.Roll()
script.Wait(1)
script.Button(Controller.A, duration = 0)
script.Wait(5)
script.Button(Controller.down, duration = 0)

#deflect bullet 3 to kill left riot sheild
script.Wait(10)
script.Button(Controller.X, duration = 0)

#slash right riot shield
script.Button(Controller.left, duration = 9)
script.Wait(10)
script.Button(Controller.X, duration = 0)

#deflect bullet 4 to kill left gunner
script.Wait(9)
script.MoveLeftStick(0)
script.Roll()
script.Wait(24)
script.MoveLeftStick(180)
script.Button(Controller.X, duration = 0)

#deflect bullet 5 to hit HH
script.Button(Controller.left, duration = 87)
script.Wait(1)
script.Roll()
script.Wait(7)
script.Button(Controller.X, duration = 0)

#slash left ricky
script.Wait(138)
script.Button(Controller.X, duration = 0)

#get to right
script.Wait(8)
script.MoveLeftStick(0)
for i in range(2):
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration=0)
    script.Wait(11)

#move to center
script.Button(Controller.left, duration = 8)


#slash right gunner
script.Wait(64)
script.MoveLeftStick(0)
script.Button(Controller.X, duration = 0)
script.Button(Controller.right, duration = 12)

#crouch slash left gunner
script.Wait(12)
script.MoveLeftStick(180)
script.Button(Controller.down, duration=9)
script.Wait(1)
script.Roll()
script.Wait(10)
script.Button(Controller.X, duration=0)
script.Wait(11)

#line up with center
script.MoveLeftStick(0)
script.Roll()
script.Wait(9)
script.Button(Controller.A, duration = 0)
script.Wait(5)
script.Button(Controller.down, duration = 0)

#wait till HH is locked in and crunch slash to her
script.Wait(25)

script.Button(Controller.X, duration=0)
script.Wait(11)

script.Button(Controller.down, duration=9)
script.Wait(1)
script.Roll()
script.Wait(11) #<-- imperfect
script.MoveLeftStick(0)
script.Button(Controller.X, duration=0)
script.Wait(11)

#get to left
script.MoveLeftStick(180)
for i in range(4):
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(180)
    script.Button(Controller.X, duration=0)
    script.Wait(11)

script.Button(Controller.right, duration = 0)

script.Wait(43)
script.MoveLeftStick(180)
script.Roll()

script.Wait(24)
script.Button(Controller.A, duration = 0)
script.Wait(5)
script.Button(Controller.down, duration = 0)

script.save()















