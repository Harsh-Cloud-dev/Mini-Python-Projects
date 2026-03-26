from manim import *
class Seventeen(Scene):
    def construct(self):
        circle = Circle(radius=4,color=LIGHT_PINK,fill_opacity=0.7)
        square = Square(side_length=4,color=LIGHT_PINK,fill_opacity=0.7)
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle,square))
        self.wait(1)
        self.play(Transform(circle,Triangle()))
        self.wait(3)