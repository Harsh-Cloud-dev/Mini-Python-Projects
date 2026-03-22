from manim import *

class ColorDemo(Scene):
    def construct(self):
        title = Text("Shapes & Colors").to_edge(UP)

        circle = Circle(color=RED, fill_opacity=0.5)
        circle.shift(LEFT * 2)

        square = Square(color=BLUE, fill_opacity=0.5)
        square.shift(RIGHT * 2)

        self.play(Write(title))
        self.play(Create(circle), Create(square))  # both at the same time!
        self.wait(2)