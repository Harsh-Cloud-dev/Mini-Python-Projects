from manim import *

class ArrowDemo(Scene):
    def construct(self):
        arrow = Arrow(start=ORIGIN, end=UR * 2, color=YELLOW)
        self.play(Create(arrow))
        self.wait(1)