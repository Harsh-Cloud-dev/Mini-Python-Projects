from manim import *
class Eleven(Scene):
    def construct(self):
        title = Text("The Unit Circle").to_edge(UP)
        circle = Circle(radius=2,fill_color = BLUE,fill_opacity = 0.5)
        dot = Dot()
        text = Text("r = 1").shift(RIGHT*3)
        self.play(Create(circle))
        self.wait(1)
        self.play(FadeIn(title,dot,text))
        self.wait(2)