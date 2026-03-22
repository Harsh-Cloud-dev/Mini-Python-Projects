from manim import *

class TwoShapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle,square))
        self.wait(1)
        FadeIn(square)
