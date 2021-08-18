import math

class Controller:
    dpad_up = 1
    dpad_down = 2
    dpad_left = 4
    dpad_right = 8
    start = 0x10
    back = 0x20
    left_thumb = 0x40
    right_thumb = 0x80
    left_shoulder = 0x100
    right_shoulder = 0x200
    A = 0x1000
    B = 0x2000
    X = 0x4000
    Y = 0x8000



class Scripter:
    action_list = []
    current_time = 0

    def Wait(self, duration):
        self.current_time+=duration

    def AddRawAction(self, time, duration=1, buttons=0, lt=0, rt=0, lx=0, ly=0, rx=0, ry=0):
        self.action_list.append(f'{time},{duration},{buttons},{lt},{rt},{lx},{ly},{rx},{ry}')

    def Button(self, buttons, frame=None, duration=1):
        if frame is None:
             frame = self.current_time

        self.AddRawAction(frame, duration, buttons)
    
    def MoveLeftStick(self, deg, frame=None, duration=1):
         x_pos = math.cos(math.radians(deg))*32767
         y_pos = math.sin(math.radians(deg))*32767
         
         if frame is None:
             frame = self.current_time

         self.AddRawAction(frame, duration, lx=x_pos, ly=y_pos)

    def MoveRightStick(self, deg, frame=None, duration=1):
         x_pos = math.cos(math.radians(deg))*32767
         y_pos = math.sin(math.radians(deg))*32767
         
         if frame is None:
             frame = self.current_time

         self.AddRawAction(frame, duration, rx=x_pos, ry=y_pos)

    def Roll(self, duration=1):
        self.AddRawAction(self.current_time, duration, rt=0xFF)

    def CrouchRoll(self):        
        self.Button(Controller.dpad_down, duration=1)
        self.Roll()

    def PerfectRollWait(self, amount=1):
        for a in range(amount):
            self.CrouchRoll()
            self.Wait(22)

    def WaitLevel(self):
        self.Wait(90)

    def save(self, file='C:/Applications/St/steamapps/common/Katana ZERO/tas.kzt'):
        fw = open(file, 'w')

        for st in self.action_list:
            fw.write(st+'\n')

        fw.close()

    
potato = Scripter()
potato.Button(Controller.left_shoulder, duration=0)
potato.Wait(2)
potato.Button(Controller.A, duration=11)
potato.Button(Controller.dpad_right, duration=11)
potato.Wait(12)
potato.Button(Controller.X, duration=0)
potato.Wait(16)
potato.Button(Controller.dpad_down, duration=44)
potato.Roll()
potato.Wait(22)
potato.Roll()
potato.Wait(8)
potato.MoveLeftStick(10)
potato.Button(Controller.X, duration=0)
potato.Button(Controller.dpad_right, duration=12)
potato.Wait(11)
potato.Button(Controller.X, duration=0)
potato.Button(Controller.dpad_down, duration=12)
potato.Wait(23)
potato.MoveLeftStick(115)
potato.Button(Controller.X, duration=0)
potato.Button(Controller.dpad_left, duration=15)
potato.Wait(6)
potato.Button(Controller.dpad_down, duration=9)
potato.Wait(8)
potato.MoveLeftStick(200)
potato.Button(Controller.X, duration=0)
potato.Wait(5)
potato.Button(Controller.dpad_left, duration=8)
potato.Button(Controller.dpad_down, duration=25)
potato.Wait(8)
potato.Button(Controller.dpad_right, duration=16)
potato.Wait(20)
potato.MoveLeftStick(10)
potato.Button(Controller.X, duration=0)
potato.Wait(6)
potato.Button(Controller.dpad_left, duration=16)
potato.Button(Controller.dpad_down, duration=30)
potato.Wait(8)
potato.MoveLeftStick(180)
potato.Button(Controller.B, duration=0)
potato.Wait(24)
potato.MoveLeftStick(290)
potato.Button(Controller.X, duration=0)
potato.Wait(2)
potato.Button(Controller.dpad_right, duration=20)
potato.Button(Controller.dpad_down, duration=20)
potato.Wait(22)
potato.MoveLeftStick(30)
potato.Button(Controller.X, duration=0)
potato.Wait(3)
potato.Button(Controller.dpad_left, duration=30)
potato.Button(Controller.dpad_down, duration=30)
potato.Wait(28)
#I didn't bother checking out at which exactly frame to slash, too much work :pensive:
potato.MoveLeftStick(160)
potato.Button(Controller.X, duration=0)
potato.Wait(4)
potato.Button(Controller.dpad_right, duration=30)
potato.Button(Controller.dpad_down, duration=30)
potato.Wait(7)
potato.MoveLeftStick(330)
potato.Button(Controller.X, duration=0)
potato.Wait(11)
potato.MoveLeftStick(330)
potato.Button(Controller.X, duration=0)
potato.Wait(13)
potato.Button(Controller.B, duration=0)
potato.Wait(2)
potato.MoveLeftStick(250)
potato.Button(Controller.X, duration=0)
potato.Wait(5)
potato.Button(Controller.B, duration=0)
potato.Button(Controller.dpad_left, duration=13)
potato.Button(Controller.dpad_down, duration=13)
potato.Wait(20)
potato.Button(Controller.A, duration=1)
potato.Wait(1)
potato.Button(Controller.dpad_down, duration=10)
potato.Wait(8)
#I am sure that this following section can be done faster
potato.MoveLeftStick(0)
potato.Button(Controller.X, duration=0)
potato.Button(Controller.dpad_right, duration=100)
potato.Wait(8)
potato.Button(Controller.dpad_down, duration=28)
potato.Wait(28)
potato.MoveLeftStick(0)
potato.Button(Controller.X, duration=0)
potato.Wait(4)
potato.Button(Controller.dpad_down, duration=36)
potato.Wait(36)
potato.MoveLeftStick(0)
potato.Button(Controller.X, duration=0)
potato.Wait(11)
potato.PerfectRollWait(3)
potato.save()

