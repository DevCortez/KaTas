import math

# F for frames T for time
MODE = 'F'

class Controller:
    up = 1
    down = 2
    left = 4
    right = 8
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
        if MODE == 'F':
            self.action_list.append(f'{time},{duration},{buttons},{lt},{rt},{lx},{ly},{rx},{ry}')
        else:
            self.action_list.append(f'{time * (1/60)},{duration * (1/60)},{buttons},{lt},{rt},{lx},{ly},{rx},{ry}')

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
        self.Button(Controller.down, duration=1)
        self.Roll()

    def PerfectRollWait(self, amount=1):
        for a in range(amount):
            self.CrouchRoll()
            self.Wait(22)

    def WaitLevel(self):
        self.Wait(90)

    def save(self, file=R'.\..\tas.kzt'):
        fw = open(file, 'w')

        for st in self.action_list:
            fw.write(st+'\n')

        fw.close()