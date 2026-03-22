from manim import *

class TwoShapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(circle))
        self.wait(0.5)
        self.play(Create(square))
        self.wait(1)