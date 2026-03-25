from manim import *
class fiveteen(Scene):
    def construct(self):
        line = Line()
        arrow = Arrow()
        line.shift(UP*3)
        self.play(Create(line))
        self.play(Create(arrow))
        self.play(FadeOut(line,arrow))