from manim import *

class AnimateDemo(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)

        self.play(Create(circle))
        self.wait(0.5)
        self.play(circle.animate.shift(RIGHT * 2).set_color(RED))
        self.wait(0.5)
        self.play(circle.animate.scale(2))
        self.wait(1)
        self.play(FadeOut(circle))