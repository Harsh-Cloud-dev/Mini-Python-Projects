from manim import *
class Eighteen(Scene):
    def construct(self):
        triangle = Triangle()
        tri = Polygon(
            [1,0,0],
            [-1,0,0],
            [0,2,0],
            color=BLUE,
            fill_opacity = 0.5
        )
        self.play(Create(triangle))
        self.wait(1)
        self.play(Transform(triangle,tri))
        self.wait(1)
        text = Text("Triangle transformed to self.Tri",font_size=14)
        text.next_to(tri,DOWN)
        self.play(Create(text))
        self.wait(2)
        triangle.set_fill(color=BLUE, opacity=0.5)
        self.play(FadeOut(triangle,tri,text))
        self.wait(1)