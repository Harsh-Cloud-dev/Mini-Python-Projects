from manim import *
class Twentythree(Scene):
    def construct(self):
        square_info = Polygon(
            [-1,1,0],
            [1,1,0],
            [1,-1,0],
            [-1,-1,0],
            color=BLUE,
        )
        square_text = Text("This is a square").next_to(square_info,RIGHT)
        squareA = Text("A",font_size=24).move_to([-1.4,1,0])
        squareB = Text("B",font_size=24).move_to([1.4,1,0])
        squareC = Text("C",font_size=24).move_to([1.4,-1,0])
        squareD = Text("D",font_size=24).move_to([-1.4,-1,0])
        square = VGroup(square_info,square_text)
        square_not = VGroup(squareA,squareB,squareC,squareD)
        self.play(Create(square_info))
        self.wait(1)
        self.play(FadeIn(square_not))
        self.wait(1)
        self.play(Create(square_text))
        everything = VGroup(square_not,square)
        self.play(everything.animate.scale(0.0).to_edge(LEFT))
        self.wait(1)
        self.play(FadeOut(square,square_not))