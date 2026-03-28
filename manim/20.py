from manim import *
class Twenty(Scene):
    def construct(self):
        tri = Polygon(
            [1,0,0],
            [-1,0,0],
            [1,2,0],
            color=  BLUE,
            fill_opacity = 0.6
        )
        formula = MathTex(r"a^2 + b^2 = c^2").next_to(tri,DOWN)
        a = Text("a").move_to([-1.3,0,0])
        b = Text("b").move_to([1.3,0,0])
        c = Text("c").move_to([1,2.3,0])
        diagram = VGroup(tri,a,b,c,formula)
        title = Text("Pythagoras Theorem",font_size=50).shift(RIGHT*4.5)
        self.play(Create(tri))
        self.wait(1)
        self.play(Create(a),Create(b),Create(c))
        self.wait(1)
        self.play(Create(formula))
        self.wait(1)
        self.play(diagram.animate.scale(0.6).shift(LEFT*6).set_color(RED))
        self.wait(1)
        self.play(Create(title))
        self.wait(2)
        self.play(FadeOut(diagram,title))
        self.wait(1)