from manim import *

class PythagorasScene(Scene):
    def construct(self):
        title = Text("The Pythagorean Theorem").to_edge(UP)

        triangle = Polygon(
            [-2, -1, 0],
            [ 2, -1, 0],
            [ 2,  2, 0],
            color=WHITE
        )

        label_a = Text("a").next_to(triangle, DOWN)
        label_b = Text("b").next_to(triangle, RIGHT)
        label_c = Text("c").move_to([-0.3, 0.6, 0])

        formula = MathTex(r"a^2 + b^2 = c^2", font_size=48).to_edge(DOWN)

        tri_group = VGroup(triangle, label_a, label_b, label_c)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)
        self.play(tri_group.animate.set_color(BLUE))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(title, tri_group, formula))