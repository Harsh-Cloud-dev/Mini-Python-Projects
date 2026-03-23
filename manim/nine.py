from manim import *

class PythagorasScene(Scene):
    def construct(self):
        # Title
        title = Text("The Pythagorean Theorem").to_edge(UP)

        # Triangle
        triangle = Polygon(
            [-2, -1, 0],
            [ 2, -1, 0],
            [ 2,  2, 0],
            color=WHITE
        )

        # Labels
        label_a = Text("a").next_to(triangle, DOWN)
        label_b = Text("b").next_to(triangle, RIGHT)
        label_c = Text("c").move_to([-0.3, 0.6, 0])

        # Formula
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=48).to_edge(DOWN)

        # Group triangle + labels together
        tri_group = VGroup(triangle, label_a, label_b, label_c)

        # --- Animation sequence ---
        self.play(Write(title))
        self.wait(0.5)

        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Highlight the triangle in blue
        self.play(tri_group.animate.set_color(BLUE))
        self.wait(0.5)

        # Formula appears
        self.play(Write(formula))
        self.wait(2)

        # Fade everything out together
        self.play(FadeOut(title, tri_group, formula))