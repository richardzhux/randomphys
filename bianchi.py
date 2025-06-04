# Visualization of Bianchi's black hole thermodynamics in a 3Blue1Brown style
# using the manim library.  Each scene is a simplified representation of the
# derivation presented in Bianchi's paper on quantum geometry and black hole
# entropy.

from manim import *

class RindlerGeometryScene(Scene):
    """Illustrate the near horizon region as a Rindler wedge."""
    def construct(self):
        # Draw a schematic Schwarzschild horizon
        horizon = Circle(radius=2, color=BLUE)
        self.play(Create(horizon))
        self.wait(0.5)

        # Zoom into a patch and morph into a flat wedge
        patch = Square(side_length=0.5, color=YELLOW).move_to(horizon.get_right())
        self.play(Create(patch))
        self.play(patch.animate.scale(4).move_to(ORIGIN))
        wedge = VGroup(
            Line(LEFT * 4, ORIGIN, color=WHITE),
            Line(DOWN * 3, ORIGIN, color=WHITE)
        )
        self.play(ReplacementTransform(patch, wedge))
        self.wait(0.5)

        # Display the metric
        metric = MathTex(r"ds^2 = -(\kappa \ell)^2 dt^2 + d\ell^2 + r_S^2 d\Omega^2")
        metric.to_edge(UP)
        self.play(Write(metric))
        self.wait(1)

class LocalObserverScene(Scene):
    """Show an accelerated observer experiencing Unruh radiation."""
    def construct(self):
        observer = Dot(ORIGIN, color=RED)
        arrow = Arrow(ORIGIN, UP * 2, color=RED)
        self.play(Create(observer), GrowArrow(arrow))
        self.wait(0.5)

        accel_label = MathTex(r"a = 1/\ell")
        accel_label.next_to(arrow, RIGHT)
        self.play(Write(accel_label))
        self.wait(0.5)

        temp = MathTex(r"T = \frac{\hbar a}{2\pi}")
        temp.to_edge(UP)
        self.play(Write(temp))
        self.wait(1)

class FacetSpinScene(Scene):
    """Depict facets of the horizon labelled by spins."""
    def construct(self):
        # Create a grid of facets
        facets = VGroup()
        labels = VGroup()
        for i in range(3):
            for j in range(3):
                sq = Square(side_length=1, color=BLUE).shift(RIGHT * i + UP * j)
                facets.add(sq)
                lbl = MathTex(r"j_{%d%d}=1" % (i, j)).scale(0.5)
                lbl.move_to(sq.get_center())
                labels.add(lbl)
        facets.center()
        labels.center()
        self.play(Create(facets), Write(labels))
        self.wait(0.5)

        energy = MathTex(r"E_f = \hbar\, \gamma\, j_f\, a").to_edge(UP)
        self.play(Write(energy))
        self.wait(1)

class DetectorInteractionScene(Scene):
    """Couple a two level system to one facet and show transition rates."""
    def construct(self):
        facet = Square(side_length=1, color=BLUE)
        atom = Dot(RIGHT * 2, color=YELLOW)
        arrow = Arrow(atom.get_left(), facet.get_right(), buff=0.1)
        self.play(Create(facet), Create(atom), GrowArrow(arrow))
        self.wait(0.5)

        rate = MathTex(r"\frac{\Gamma_+}{\Gamma_-} = e^{-2\pi\Delta\epsilon/(\hbar a)}")
        rate.to_edge(UP)
        self.play(Write(rate))
        self.wait(1)

class EntropyScene(Scene):
    """Show how absorbed energy changes the entropy of a facet."""
    def construct(self):
        area_change = MathTex(r"\delta S = \frac{\delta E}{T} = 2\pi\gamma j_f")
        self.play(Write(area_change))
        self.wait(1)

        sum_entropy = MathTex(r"S = \sum_f \delta S_f = \frac{A}{4G\hbar}")
        sum_entropy.next_to(area_change, DOWN)
        self.play(Write(sum_entropy))
        self.wait(1)

class PartitionFunctionScene(Scene):
    """Display the partition function and its thermodynamic consequences."""
    def construct(self):
        Z = MathTex(
            r"Z(\beta) = \exp\left[ -\frac{1}{8\pi G\hbar} \sum_f A_f (\beta a - 2\pi) \right]"
        )
        self.play(Write(Z))
        self.wait(0.5)

        arrows = VGroup(
            Arrow(Z.get_bottom(), DOWN * 2 + LEFT * 2, buff=0.1),
            Arrow(Z.get_bottom(), DOWN * 2 + RIGHT * 2, buff=0.1)
        )
        labels = VGroup(
            MathTex(r"E = -\partial_\beta \ln Z"),
            MathTex(r"S = (1-\beta\partial_\beta) \ln Z")
        )
        labels.arrange(RIGHT, buff=1).next_to(arrows, DOWN)
        self.play(Create(arrows), Write(labels))
        self.wait(1)

# Scenes can be rendered individually with, for example:
# manim -pql bianchi.py RindlerGeometryScene
