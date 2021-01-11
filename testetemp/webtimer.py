from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty,StringProperty
from kivy.clock import Clock
import time
import datetime as dt
from datetime import datetime
import pyautogui

inicio = datetime.now()
current = None
elapsed = time.strftime('%I'+':'+'%M'+':'+'%S'+' %p')
pausa = 0
class relogioApp(App):
    displayText = ObjectProperty()
    def build(self):
        global event
        b=Base()
        c=b.ids.displayText
        event  = Clock.schedule_interval(c.update, 1)
        #Display.text= "w"
        event.cancel()
        return b


class Base(BoxLayout):
    def start(self):
        global inicio
        inicio = datetime.now()
        print('daf')

    def stop(self):
        global inicio
        # time.sleep(5)
        # #pyautogui.click('/Users/tetsuo/dev/camera.png')
        # print(pyautogui.locateOnScreen('/Users/tetsuo/dev/camera.png', confidence=.9))
        # cam=pyautogui.locateOnScreen('/Users/tetsuo/dev/camera.png', confidence=.9)
        # x1= cam.left+25
        # y1= cam.top+25
        # #pyautogui.click('/Users/tetsuo/dev/camera.png', confidence=.5)
        # pyautogui.click(x=x1,y=y1)
        print('acabou')
        event()


    def reset(self):
        global inicio
        inicio = datetime.now()
        print('daf')

class Display(Label):
    global pausa
    def update(self, *args):
        segundos = int((datetime.now()-inicio).total_seconds())
        minutos = segundos // 60
        horas = minutos // 60
        print(minutos)
        print(self.diferenca(0,15,0,horas,minutos,segundos))
        self.text= str(self.diferenca(0,15,0,horas,minutos,segundos))[2:]
        # if self.diferenca(0, 0, 20,horas,minutos,segundos)[2:] < 0:
        if int(self.diferenca(0, 0, 10,horas,minutos,segundos).days)<0:
            pausa = 1
            # Base.stop(self)
            #relogioApp.build(self).event.cancel()
        print(
        int(self.diferenca(0, 0, 20,horas,minutos,segundos).days)<0
        )

        return

    def diferenca(self, h1, m1, s1, h2, m2, s2):

        start_time = dt.time(h1, m1, s1)
        stop_time = dt.time(h2, m2, s2)

        date = dt.date(1, 1, 1)
        datetime1 = dt.datetime.combine(date, start_time)
        datetime2 = dt.datetime.combine(date, stop_time)
        time_elapsed = datetime1 - datetime2
        restante = str(int(time_elapsed.total_seconds()//60)) + ":" + str(int(time_elapsed.total_seconds()%60))
        return time_elapsed

    def encerrar(self):
        print("fim")

relogioApp().run()
