# Bunker 2-1 23.37s made by snek pliskin (https://youtu.be/ue-e1zafpEo) and 23.42s made by Bar0ti (https://youtu.be/G08T01H6kCc)

# change the value of STRAT to use other variations of this room
# STRAT = 1 - 23.37s - cannot be improved without substantial changes to the strat(snek pliskin)
# STRAT = 2 - 23.37s - very likely to be improved upon, you need to tinker with the scanner skip, try different starting positions of the roll or
                   # - perhaps different spots at which the head lands etc. (Bar0ti)

STRAT = 1
from katas import Controller, Scripter
script = Scripter()

script.Button(Controller.left_shoulder, 0)
script.Wait(2)

if STRAT == 1:
    #crouch roll to ajust position
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
   
    #goto left
    script.MoveLeftStick(180)
    script.PerfectRollWait(4)

    #destroy turrets
    script.Wait(35)
    script.Button(Controller.A, duration = 10)
    script.Wait(29)
    script.MoveLeftStick(91)
    script.Button(Controller.X, duration = 0)

    #jump off wall
    script.Button(Controller.left, duration = 20)
    script.Wait(40)
    script.Button(Controller.A, duration = 100)

    #slash
    script.Wait(29)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration = 0)

    #go back to the left
    script.Button(Controller.left, duration = 70)
    script.Wait(50)

    #onto wall
    script.Wait(67)
    script.Button(Controller.A, duration = 10)
    script.Button(Controller.left, duration = 20)

    #off wall
    script.Wait(50)
    script.Button(Controller.A, duration = 100)
    script.Wait(10)
    script.MoveLeftStick(135)
    script.Button(Controller.X, duration = 0)

    #fastfall
    script.Button(Controller.right, duration = 30)
    script.Wait(8)
    script.Button(Controller.down, duration = 0)
    script.Wait(20)

    #roll-throw-roll
    script.Roll()
    script.Wait(19)
    script.MoveLeftStick(180)
    script.Button(Controller.B, duration = 0)
    script.Wait(4)
    script.MoveLeftStick(0)
    script.Roll()

    #wait for slowmo & decapitate
    script.Wait(327)
    script.MoveLeftStick(260)
    script.Button(Controller.X, duration = 0)
    script.Button(Controller.left, duration = 21)

    #get head & exit
    script.Wait(92)
    script.Button(Controller.Y, duration = 0)
    script.Button(Controller.B, duration = 0)
    script.Wait(30)
    script.Button(Controller.A, duration = 0)

    script.save()

if STRAT == 2:
    script.Button(Controller.down, duration=1)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(14)
    script.MoveLeftStick(0)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.left, duration=1)
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(180)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(180)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.down, duration=9)
    script.Wait(1)
    script.Roll()
    script.Wait(10)
    script.MoveLeftStick(180)
    script.Button(Controller.X, duration=0)
    script.Wait(11)
    script.Button(Controller.down, duration=9)
    script.Wait(30)
    script.Button(Controller.left, duration=12)
    script.Button(Controller.A, duration=12)
    script.Wait(53)
    script.Button(Controller.left, duration=12)
    script.MoveLeftStick(200)
    script.Button(Controller.X, duration=0)
    script.Wait(20)
    script.Button(Controller.A, duration=4)
    script.Wait(34)
    script.MoveLeftStick(50)
    script.Button(Controller.X, duration=0)
    script.Wait(18)
    script.MoveLeftStick(60)
    script.Button(Controller.X, duration=0)
    script.Wait(10)
    script.Button(Controller.left, duration=12)
    script.Button(Controller.down, duration=12)
    script.Wait(18)
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
    script.Wait(10)
    script.MoveLeftStick(170)
    script.Button(Controller.X, duration=0)
    script.Wait(78)
    script.Button(Controller.left, duration=24)
    script.Button(Controller.A, duration=12)
    script.Wait(28)
    script.Button(Controller.A, duration=4)
    script.Wait(10)
    script.MoveLeftStick(120)
    script.Button(Controller.X, duration=0)
    script.Wait(8)
    script.Button(Controller.right, duration=12)
    script.Button(Controller.down, duration=12)
    script.Wait(16)
    script.Button(Controller.down, duration=1)
    script.Wait(1)
    script.Roll()
    script.Wait(20)
    script.Wait(1)
    script.MoveLeftStick(180)
    script.Button(Controller.B, duration=0)
    script.Wait(1)
    script.Button(Controller.right, duration=1)
    script.Wait(1)
    script.Roll()
    script.Wait(330)
    script.MoveLeftStick(260)
    script.Button(Controller.X, duration=0)
    script.Wait(4)
    script.Button(Controller.left, duration=55)
    script.Wait(66)
    script.Button(Controller.right, duration=1)
    script.Wait(1)
    script.Roll()
    script.Wait(9)
    script.Button(Controller.Y, duration=0)
    script.Wait(31)
    script.Button(Controller.A, duration=0)
    script.Wait(22)
    script.Button(Controller.A, duration=0)
    script.save()










