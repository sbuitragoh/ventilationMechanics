from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread

def get_values():
    global levels
    while True:
        with open('test.txt', 'r') as df:
            lines = df.readlines()
            for line in lines:
                line = float(line[:-1])
                if len(levels) >= 120:
                    levels = []
                levels.append(line)


class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1,0,0,1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.5)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/1.5) for i,j in enumerate(levels)]

class RealTimeGraph(App):
    def build(self):
        return Builder.load_file('Sample.kv')

if __name__ == "__main__":
    levels = []
    get_level_thread = Thread(target=get_values)
    get_level_thread .daemon = True
    get_level_thread.start()
    RealTimeGraph().run()