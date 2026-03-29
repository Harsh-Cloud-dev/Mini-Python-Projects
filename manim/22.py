from manim import *
class TwentyTwo(Scene):
    def construct(self):
        #circle
        circle_data = Circle(radius=1,color=BLUE,fill_opacity=0.5).shift(DOWN-1)
        circle_text = MathTex(r"\pi r^2").next_to(circle_data,DOWN)

        #Right angle triangle
        tri_info = Polygon(
            [-3,2.5,0],
            [0,3.5,0],
            [0,2.5,0],
            color=BLUE,
            fill_opacity = 0.5
        )
        tri_text = MathTex(r"a^2 + b^2 = c^2").next_to(tri_info,DOWN)
        
        #Title
        text = Text("Thanks by \nHarsh",font_size=50)

        #VGroup
        tri = VGroup(tri_info,tri_text)
        circle = VGroup(circle_data,circle_text)
        
        #Animation
        self.wait(1)
        self.play(Create(circle),Create(tri))
        self.wait(1)
        self.play(circle.animate.shift(LEFT*6).scale(0.3), tri.animate.shift(LEFT*6).scale(0.3))
        self.play(Create(text))
        self.wait(2)