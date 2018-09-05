from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout

class Sample(BoxLayout):
    pass

class SampleApp(App):
    def build(self):
        return Sample()

if __name__ == '__main__':
    SampleApp().run()