from manim import *

class VGroupDemo(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        label = Text("Circle").next_to(circle, DOWN)

        group = VGroup(circle, label)

        self.play(Create(circle), Write(label))
        self.wait(0.5)
        self.play(group.animate.shift(LEFT * 2))   # both move together
        self.play(group.animate.scale(0.5))         # both shrink together
        self.wait(1)
        self.play(FadeOut(group))