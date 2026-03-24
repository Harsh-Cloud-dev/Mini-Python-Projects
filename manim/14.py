from manim import *

class ArrowDemo(Scene):
    def construct(self):
        # A label with an arrow pointing to a circle
        circle = Circle(color=BLUE, fill_opacity=0.5)
        label = Text("This is a circle", font_size=30).shift(RIGHT * 3 + UP * 2)
        arrow = Arrow(start=label.get_left(), end=circle.get_top(), color=YELLOW)

        self.play(Create(circle))
        self.play(Write(label), Create(arrow))
        self.wait(2)