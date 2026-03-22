from manim import *

class TextDemo(Scene):
    def construct(self):
        title = Text("Pythagoras Theorem")
        formula = MathTex(r"a^2 + b^2 = c^2")

        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, formula))  # title morphs into formula
        self.wait(2)
        self.play(FadeOut(title))