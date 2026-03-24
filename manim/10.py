from manim import *
class Ten(Scene):
    def construct(self):
        text = Text("Area of a Triangle").to_edge(UP)
        triangle = Polygon(
            [-2,-2,0],
            [2,-2,0],
            [0,2,0],
            color=BLUE
        )
        formula = MathTex(r"A = \frac{1}{2} b h").to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)
        self.play(Create(triangle))
        self.wait(1)
        self.play(Write(formula))
        self.play(FadeOut(formula,text,triangle))