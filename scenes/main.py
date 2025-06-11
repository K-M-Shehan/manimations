from manim import *

class firstScene(Scene):
    def construct(self):
        text = Text("Yeah boi")
        self.play(Write(text))
        self.wait(2)
    
class demo(Scene):
   def construct(self):
        t = Text("Supremestrawhat")
        self.play(Write(t))
        self.wait(3)

class Test(Scene):
    def construct(self):
        circ = Circle(radius = 2.4, color = RED)
        self.play(Write(circ))
        self.wait(2)
