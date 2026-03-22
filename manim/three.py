from manim import *

class PositionDemo(Scene):
    def construct(self):
        title = Text("Pythagoras Theorem").to_edge(UP)
        formula = MathTex(r"a^2 + b^2 = c^2")  # center by default
        note = Text("where c is the hypotenuse", font_size=50).to_edge(DOWN)

        self.play(Write(title))
        self.play(Write(formula))
        self.play(FadeIn(note))
        self.wait(2)