from manim import *
class MyTest(Scene):
    def construct(self):
        text = Text("Area of a Circle",font_size=36).to_edge(UP)
        circle = Circle(color=BLUE,fill_opacity = 0.6)
        formula = MathTex(r"A = \pi r^2").shift(DOWN*2)
        self.play(Write(text))
        self.wait(1)
        self.play(Create(circle))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(text,circle,formula))