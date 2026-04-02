from manim import *

class Twentyfive(Scene):
    def construct(self):
        circle_shape = Circle(radius=1, color=BLUE, fill_opacity=0.5).move_to([-3.5, 2, 0])
        circle_info = Text("Circle", font_size=48).next_to(circle_shape, DOWN)

        tri_shape = Polygon(
            [-2.5, 0, 0],
            [-1.5, 0, 0],
            [-2, 2, 0],
            color=BLUE,
            fill_opacity=0.5
        )
        tri_info = Text("Triangle", color=BLUE).next_to(tri_shape, DOWN)

        square_shape = Polygon(
            [-1.5, 0, 0],
            [-1.5, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
            color=BLUE,
            fill_opacity=0.5
        )
        square_info = Text("Square", color=BLUE).next_to(square_shape, DOWN)

        self.play(Create(circle_shape), Write(circle_info))
        self.wait(1)

        self.play(Create(tri_shape), Write(tri_info))
        self.wait(1)

        self.play(Create(square_shape), Write(square_info))
        self.wait(2)