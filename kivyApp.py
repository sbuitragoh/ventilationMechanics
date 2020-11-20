from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.graph import MeshLinePlot, LinePlot
from kivy.clock import Clock
from threading import Thread

def get_values():
    global pressure, flow, volume
    while True:
        with open('test.txt', 'r') as df:
            lines = df.readlines()
            for line in lines:
                line = float(line[:-1])
                if len(pressure) >= 120:
                    pressure = []
                if len(flow) >= 120:
                    flow = []
                if len(volume) >= 120:
                    volume = []
                pressure.append(line)
                flow.append(line//2)
                volume.append(line-10)

class mainWindow(Screen):
    pass

class secondWindow(Screen):
    pass

class Logic(Screen):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = LinePlot(line_width=2, color=[1, 0, 0, 1])
        self.plot2 = LinePlot(line_width=2,color=[0, 1, 0, 1])
        self.plot3 = LinePlot(line_width=2,color=[0, 0, 1, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        self.ids.graph2.add_plot(self.plot2)
        self.ids.graph3.add_plot(self.plot3)
        Clock.schedule_interval(self.get_value, 0.5)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/1.5) for i,j in enumerate(pressure)]
        self.plot2.points = [(i, j / 1.5) for i, j in enumerate(flow)]
        self.plot3.points = [(i, j / 1.5) for i, j in enumerate(volume)]

class windowManager(ScreenManager):
    pass

kv = Builder.load_file('Sample.kv')

sm = ScreenManager()
sm.add_widget(mainWindow(name='main'))
sm.add_widget(secondWindow(name='second'))
sm.add_widget(Logic(name='logic'))

class RealTimeGraph(App):
    def build(self):
        return sm

if __name__ == "__main__":
    pressure = []
    flow = []
    volume = []
    get_level_thread = Thread(target=get_values)
    get_level_thread .daemon = True
    get_level_thread.start()
    RealTimeGraph().run()