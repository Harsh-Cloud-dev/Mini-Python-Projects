from manim import *

class Twelve(Scene):
    def construct(self):
        circle = Circle(radius=2, fill_color=RED, fill_opacity=1.0)
        circle_text = Text("Circle").to_edge(DOWN)

        square = Square(side_length=2)
        square_text = Text("Square").to_edge(DOWN)

        triangle = Polygon(
            [-2, -2, 0],
            [ 2, -2, 0],
            [ 0,  2, 0],
            color=BLUE
        )
        triangle_text = Text("Triangle").to_edge(DOWN)

        # Show circle first
        self.play(Create(circle), Write(circle_text))
        self.wait(1)

        # Transform to square
        self.play(Transform(circle, square), Transform(circle_text, square_text))
        self.wait(1)

        # Transform to triangle
        self.play(Transform(circle, triangle), Transform(circle_text, triangle_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(circle, circle_text))