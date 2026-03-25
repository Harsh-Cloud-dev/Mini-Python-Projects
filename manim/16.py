from manim import *
class Sixteen(Scene):
    def construct(self):
        circle = Circle(radius=2,color=BLUE,fill_opacity = 0.5)
        square = Square(side_length=2,fill_opacity = 0.4,color=RED)
        self.play(Create(circle))
        square.shift(UP*2 + RIGHT*4)
        self.play(Transform(circle,square))
        square.to_edge(DOWN)
        self.play(Transform(circle,square))
        self.play(FadeOut(circle,square))