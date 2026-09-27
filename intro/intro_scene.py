"""15-second animated intro for the 'Learning with Meta AI' YouTube series.

Style: clean explainer intro, dark navy background, subtle glowing network,
two-tone title, dim subtitle. No LaTeX anywhere — Text only.

Render: manim -qh intro_scene.py IntroScene   (1080p, 1920x1080)
"""
from manim import *
import random
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = "#0A0E1A"

NAVY = "#0A0E1A"
ACCENT = "#5AA9FF"
DIM = "#8A93A8"
FONT = "DejaVu Sans"


class IntroScene(Scene):
    def construct(self):
        random.seed(42)
        np.random.seed(42)

        # ---------- Network backdrop: glowing dots + self-drawing edges ----------
        n = 26
        pts = [
            np.array(
                [random.uniform(-7.0, 7.0), random.uniform(-3.9, 3.9), 0.0]
            )
            for _ in range(n)
        ]
        dots = VGroup()
        for p in pts:
            halo = Dot(p, radius=0.17, color=ACCENT, fill_opacity=0.16)
            core = Dot(p, radius=0.065, color=ACCENT, fill_opacity=0.9)
            dots.add(VGroup(halo, core))

        edges = VGroup()
        for i in range(n):
            for j in range(i + 1, n):
                if np.linalg.norm(pts[i] - pts[j]) < 2.7:
                    edges.add(
                        Line(
                            pts[i],
                            pts[j],
                            stroke_width=1.6,
                            color=ACCENT,
                            stroke_opacity=0.22,
                        )
                    )
        network = VGroup(edges, dots)

        # ---------- Title / subtitle ----------
        t1 = Text("Learning with ", font=FONT, font_size=88, color=WHITE, weight=BOLD)
        t2 = Text("Meta AI", font=FONT, font_size=88, color=ACCENT, weight=BOLD)
        title = VGroup(t1, t2).arrange(RIGHT, buff=0.22)
        if title.width > 11.5:
            title.scale(11.5 / title.width)
        title.move_to(UP * 0.35)

        subtitle = Text(
            "Real builds. Real agent. No hype.",
            font=FONT,
            font_size=42,
            color=DIM,
        )
        subtitle.next_to(title, DOWN, buff=0.55)

        # ---------- Timeline (~15 s total) ----------
        # 0.0 - 1.5 s : dots fade in
        self.play(FadeIn(dots, lag_ratio=0.06), run_time=1.5)
        # 1.5 - 3.5 s : edges draw themselves
        self.play(
            LaggedStart(*[Create(e) for e in edges], lag_ratio=0.05),
            run_time=2.0,
        )
        # 3.5 - 4.0 s : gentle settle drift
        self.play(network.animate.shift(UP * 0.12), run_time=0.5, rate_func=smooth)
        # 4.0 - 6.5 s : title writes on
        self.play(Write(title), run_time=2.5)
        # 6.5 - 8.0 s : hold
        self.wait(1.5)
        # 8.0 - 9.5 s : subtitle fades in
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.5)
        # 9.5 - 13.5 s : hold with slow ambient drift of the network
        self.play(network.animate.shift(DOWN * 0.14), run_time=4.0, rate_func=linear)
        # 13.5 - 15.0 s : fade everything out
        self.play(
            FadeOut(VGroup(network, title, subtitle)), run_time=1.5
        )
