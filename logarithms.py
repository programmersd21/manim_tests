from manim import *

config.background_color = "#0b1020"
config.frame_rate = 60

BASE = YELLOW
EXPONENT = BLUE_C
RESULT = GREEN_C
LOGCOLOR = PURPLE_C
ACCENT = TEAL_C
TEXT = GREY_A
MUTED = GREY_B
DANGER = RED_C


class LogarithmsMasterclass(MovingCameraScene):
    def construct(self):
        self.setup_theme()

        self.hook_section()
        self.transition_section("Exponents Refresher", "Exponent = repeated multiplication")
        self.exponents_section()
        self.transition_section("The Missing Question", "What exponent gives the result?")
        self.problem_section()
        self.transition_section("Birth of Logarithms", "A logarithm asks for the exponent")
        self.birth_of_logs_section()
        self.transition_section("Build Intuition", "Many bases. Same idea.")
        self.intuition_section()
        self.transition_section("The Machine View", "Exponentiation forward. Logarithms backward.")
        self.machine_section()
        self.transition_section("Number Line Meaning", "Logs compress huge growth")
        self.number_line_section()
        self.transition_section("Real-World Applications", "Anywhere scale changes fast")
        self.applications_section()
        self.transition_section("Logarithm Laws", "The rules come from exponent rules")
        self.log_laws_section()
        self.transition_section("Common Mistakes", "Notation matters")
        self.common_mistakes_section()
        self.transition_section("Worked Problems", "Solve by turning logs into exponents")
        self.worked_examples_section()
        self.transition_section("Final Summary", "One sentence to remember")
        self.final_summary_section()

    def setup_theme(self):
        self.camera.background_color = "#0b1020"

    def clear_stage(self, run_time=0.75):
        mobs = self.mobjects.copy()
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)
        self.clear()

    def transition_section(self, title, subtitle):
        self.clear_stage(run_time=0.55)
        t = Text(title, font_size=42, weight=BOLD, color=WHITE)
        s = Text(subtitle, font_size=24, color=TEXT)
        g = VGroup(t, s).arrange(DOWN, buff=0.18)
        g.move_to(ORIGIN)
        bar = Line(LEFT * 4.5, RIGHT * 4.5, color=MUTED, stroke_width=2).next_to(g, DOWN, buff=0.35)
        self.play(Write(t), FadeIn(s, shift=UP * 0.15), Create(bar), run_time=1.0)
        self.wait(0.35)
        self.play(FadeOut(g), FadeOut(bar), run_time=0.55)

    def title_block(self, title, subtitle=None):
        t = Text(title, font_size=38, weight=BOLD, color=WHITE).to_edge(UP, buff=0.35)
        if subtitle:
            s = Text(subtitle, font_size=22, color=TEXT)
            s.next_to(t, DOWN, buff=0.12)
            return VGroup(t, s)
        return VGroup(t)

    def pill(self, text, color=WHITE, fill_opacity=0.14, stroke_color=None, width=2.3, height=0.68):
        stroke_color = stroke_color or color
        box = RoundedRectangle(corner_radius=0.22, width=width, height=height)
        box.set_fill(color, opacity=fill_opacity)
        box.set_stroke(stroke_color, width=2)
        label = Text(text, font_size=22, weight=BOLD, color=color)
        label.move_to(box)
        return VGroup(box, label)

    def math_card(self, tex, width=3.0, height=1.18, fill="#13233d", stroke="#2c4266", font_size=38):
        box = RoundedRectangle(corner_radius=0.22, width=width, height=height)
        box.set_fill(fill, opacity=0.95)
        box.set_stroke(stroke, width=2)
        expr = MathTex(tex, font_size=font_size)
        expr.move_to(box)
        return VGroup(box, expr)

    def eq_pair(self, left_tex, right_tex, left_color=None, right_color=None, font_size=48):
        left = MathTex(left_tex, font_size=font_size)
        right = MathTex(right_tex, font_size=font_size)
        if left_color is not None:
            left.set_color(left_color)
        if right_color is not None:
            right.set_color(right_color)
        arrow = MathTex(r"\Longleftrightarrow", font_size=font_size + 10, color=MUTED)
        return VGroup(left, arrow, right).arrange(RIGHT, buff=0.45)

    def hook_section(self):
        title = self.title_block("2 → 4 → 8 → 16 → 32 ...", "What operation is really happening here?")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        nums = [2, 4, 8, 16, 32]
        nodes = VGroup()
        for n in nums:
            c = Circle(radius=0.52)
            c.set_fill("#13233d", opacity=0.95)
            c.set_stroke("#38557f", width=2)
            t = MathTex(str(n), font_size=42, color=WHITE)
            nodes.add(VGroup(c, t))
        nodes.arrange(RIGHT, buff=0.92)
        nodes.move_to(ORIGIN).shift(UP * 0.2)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            arrows.add(Arrow(nodes[i].get_right(), nodes[i + 1].get_left(), buff=0.12, stroke_width=5, max_tip_length_to_length_ratio=0.12, color=MUTED))

        label = self.pill("× 2", color=BASE, fill_opacity=0.18, stroke_color=BASE, width=1.8)
        label.next_to(nodes, UP, buff=0.45)

        self.play(LaggedStart(*[FadeIn(m, scale=0.65) for m in nodes], lag_ratio=0.12), run_time=1.2)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.13), run_time=1.0)
        self.play(FadeIn(label, shift=DOWN * 0.12), run_time=0.45)

        repeated = MathTex(r"2\times 2\times 2\times 2\times 2 = 32", font_size=40)
        repeated.set_color_by_tex("2", BASE)
        repeated.set_color_by_tex("32", RESULT)
        repeated.next_to(nodes, DOWN, buff=0.55)

        power = MathTex(r"2^5 = 32", font_size=50)
        power[0].set_color(BASE)
        power[2].set_color(RESULT)
        power.move_to(repeated)

        self.play(Write(repeated))
        self.wait(0.4)
        self.play(TransformMatchingTex(repeated, power))
        self.wait(0.9)

        caption = Text("The hidden operation is repeated multiplication.", font_size=26, color=TEXT)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption, shift=UP * 0.12))
        self.wait(1.0)

    def exponents_section(self):
        title = self.title_block("Exponents Refresher", "The exponent tells you how many times the base is used.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        ladder = VGroup()
        items = [(1, 2), (2, 4), (3, 8), (4, 16), (5, 32)]
        for e, r in items:
            card = self.math_card(rf"2^{{{e}}} = {r}", width=2.35, height=1.1, font_size=34)
            card[1].set_color_by_tex("2", BASE)
            card[1].set_color_by_tex(str(r), RESULT)
            ladder.add(card)
        ladder.arrange(DOWN, buff=0.18)
        ladder.scale(0.92).shift(LEFT * 2.95 + UP * 0.2)

        note = VGroup(
            self.pill("Base", color=BASE, fill_opacity=0.16, stroke_color=BASE, width=1.4),
            self.pill("Exponent", color=EXPONENT, fill_opacity=0.16, stroke_color=EXPONENT, width=1.8),
            self.pill("Result", color=RESULT, fill_opacity=0.16, stroke_color=RESULT, width=1.5),
        ).arrange(RIGHT, buff=0.3).to_edge(RIGHT, buff=0.5).shift(UP * 0.2)

        expl = Text("2 × 2 × 2 × 2 × 2", font_size=40, color=WHITE)
        expl.next_to(note, DOWN, buff=0.45)
        expl.set_color_by_tex("2", BASE)

        self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.12) for c in ladder], lag_ratio=0.1), run_time=1.3)
        self.play(FadeIn(note, shift=UP * 0.1))
        self.play(Write(expl))
        self.wait(1.0)

        active = SurroundingRectangle(ladder[-1], color=BASE, buff=0.12, corner_radius=0.12)
        self.play(Create(active), run_time=0.5)
        self.wait(0.7)

    def problem_section(self):
        title = self.title_block("The Missing Question", "We know the value. Now ask for the exponent itself.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        known = MathTex(r"2^5 = 32", font_size=62)
        known[0].set_color(BASE)
        known[2].set_color(RESULT)
        known.move_to(UP * 0.9)

        question = Text("If 2⁵ = 32, what exponent gives 32?", font_size=30, color=WHITE)
        question.next_to(known, DOWN, buff=0.48)

        blank = MathTex(r"2^x = 32", font_size=62)
        blank[0].set_color(BASE)
        blank[2].set_color(RESULT)
        blank.move_to(known)

        self.play(Write(known))
        self.play(FadeIn(question, shift=UP * 0.1))
        self.wait(0.5)

        xmark = MathTex("x", font_size=66, color=EXPONENT).move_to(known[0].get_center() + RIGHT * 0.18)
        self.play(FadeTransform(known.copy(), blank), FadeIn(xmark, scale=1.15))
        self.wait(0.4)

        logform = MathTex(r"\log_2(32) = 5", font_size=62)
        logform[0].set_color(LOGCOLOR)
        logform[2].set_color(EXPONENT)
        logform.move_to(blank)

        subtitle = Text("A logarithm asks for the exponent.", font_size=28, color=TEXT)
        subtitle.to_edge(DOWN, buff=0.55)

        self.play(TransformMatchingTex(blank, logform), FadeOut(xmark), FadeOut(question))
        self.play(FadeIn(subtitle, shift=UP * 0.1))
        self.wait(1.1)

    def birth_of_logs_section(self):
        title = self.title_block("Birth of Logarithms", "Same relationship. New question.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        left = MathTex(r"2^5 = 32", font_size=58)
        left[0].set_color(BASE)
        left[2].set_color(RESULT)

        right = MathTex(r"\log_2(32) = 5", font_size=58)
        right[0].set_color(LOGCOLOR)
        right[2].set_color(EXPONENT)

        left.to_edge(LEFT, buff=0.9).shift(UP * 0.35)
        right.to_edge(RIGHT, buff=0.9).shift(UP * 0.35)

        arrow = MathTex(r"\Longleftrightarrow", font_size=84, color=MUTED).move_to(ORIGIN)

        self.play(Write(left))
        self.play(Write(right))
        self.play(Write(arrow))
        self.wait(0.5)

        left_box = SurroundingRectangle(left, color=BASE, buff=0.18, corner_radius=0.12)
        right_box = SurroundingRectangle(right, color=LOGCOLOR, buff=0.18, corner_radius=0.12)
        self.play(Create(left_box), Create(right_box), run_time=0.6)

        explain = VGroup(
            Text("Exponentiation asks: What number do I get?", font_size=24, color=WHITE),
            Text("Logarithms ask: What exponent did I use?", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(explain[0], shift=UP * 0.1), FadeIn(explain[1], shift=UP * 0.1))
        self.wait(1.0)

        self.play(self.camera.frame.animate.scale(0.95), run_time=0.7)
        self.play(self.camera.frame.animate.scale(1 / 0.95), run_time=0.7)

    def intuition_section(self):
        title = self.title_block("Build Intuition", "Many bases. Same meaning: the log returns the exponent.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        examples = [
            (10, 3, 1000),
            (3, 3, 27),
            (5, 3, 125),
            (2, 6, 64),
        ]

        cards = VGroup()
        for b, e, r in examples:
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=1.4)
            box.set_fill("#13233d", opacity=0.95)
            box.set_stroke("#2c4266", width=2)

            exp = MathTex(rf"{b}^{{{e}}} = {r}", font_size=38)
            exp[0].set_color(BASE)
            exp[-1].set_color(RESULT)
            exp.move_to(box).shift(UP * 0.2)

            log = MathTex(rf"\log_{{{b}}}({r}) = {e}", font_size=38)
            log[0].set_color(LOGCOLOR)
            log[-1].set_color(EXPONENT)
            log.move_to(box).shift(DOWN * 0.26)

            cards.add(VGroup(box, exp, log))

        cards.arrange_in_grid(rows=2, cols=2, buff=0.45)
        cards.scale(0.88).shift(LEFT * 0.15 + DOWN * 0.15)

        self.play(LaggedStart(*[FadeIn(c[0], scale=0.92) for c in cards], lag_ratio=0.12), run_time=1.0)
        self.play(LaggedStart(*[Write(c[1]) for c in cards], lag_ratio=0.12), run_time=1.1)
        self.play(LaggedStart(*[TransformFromCopy(c[1], c[2]) for c in cards], lag_ratio=0.12), run_time=1.3)

        tower = VGroup(
            MathTex(r"5^1 = 5", font_size=34),
            MathTex(r"5^2 = 25", font_size=34),
            MathTex(r"5^3 = 125", font_size=34),
        ).arrange(DOWN, buff=0.18)
        for m in tower:
            m.set_color_by_tex("5", BASE)
        tower.to_edge(RIGHT, buff=0.35).shift(UP * 0.25)

        tower_label = Text("Growth tower", font_size=24, color=TEXT).next_to(tower, UP, buff=0.15)
        self.play(FadeIn(tower_label, shift=LEFT * 0.1))
        self.play(LaggedStart(*[FadeIn(m, shift=LEFT * 0.12) for m in tower], lag_ratio=0.15), run_time=1.0)
        self.wait(1.1)

    def machine_section(self):
        title = self.title_block("The Machine View", "Exponentiation goes forward. Logarithms run it backward.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        exp_machine = RoundedRectangle(corner_radius=0.25, width=4.85, height=2.05)
        exp_machine.set_fill("#13233d", opacity=0.96)
        exp_machine.set_stroke(BASE, width=2.5)
        exp_machine.shift(LEFT * 3.0 + UP * 0.15)

        log_machine = RoundedRectangle(corner_radius=0.25, width=4.85, height=2.05)
        log_machine.set_fill("#231338", opacity=0.96)
        log_machine.set_stroke(LOGCOLOR, width=2.5)
        log_machine.shift(RIGHT * 3.0 + UP * 0.15)

        exp_label = Text("Exponentiation", font_size=28, weight=BOLD, color=BASE).move_to(exp_machine.get_top() + DOWN * 0.4)
        log_label = Text("Logarithm", font_size=28, weight=BOLD, color=LOGCOLOR).move_to(log_machine.get_top() + DOWN * 0.4)

        exp_in_base = MathTex("2", font_size=46, color=BASE).move_to(exp_machine.get_left() + RIGHT * 1.05)
        exp_in_power = MathTex("5", font_size=46, color=EXPONENT).move_to(exp_machine.get_left() + RIGHT * 0.15)
        exp_out = MathTex("32", font_size=46, color=RESULT).move_to(exp_machine.get_right() + LEFT * 1.0)

        log_in = MathTex("32", font_size=46, color=RESULT).move_to(log_machine.get_left() + RIGHT * 1.0)
        log_out = MathTex("5", font_size=46, color=EXPONENT).move_to(log_machine.get_right() + LEFT * 1.0)

        exp_arrow = Arrow(exp_machine.get_left() + RIGHT * 1.45, exp_machine.get_right() + LEFT * 1.45, buff=0.12, stroke_width=5, max_tip_length_to_length_ratio=0.12, color=MUTED)
        log_arrow = Arrow(log_machine.get_right() + LEFT * 1.45, log_machine.get_left() + RIGHT * 1.45, buff=0.12, stroke_width=5, max_tip_length_to_length_ratio=0.12, color=MUTED)

        exp_desc = Text("base + exponent → result", font_size=22, color=TEXT)
        exp_desc.next_to(exp_machine, DOWN, buff=0.14)
        log_desc = Text("result → exponent", font_size=22, color=TEXT)
        log_desc.next_to(log_machine, DOWN, buff=0.14)

        self.play(FadeIn(exp_machine), FadeIn(log_machine))
        self.play(Write(exp_label), Write(log_label))
        self.play(GrowArrow(exp_arrow), GrowArrow(log_arrow))
        self.play(Write(exp_desc), Write(log_desc))
        self.play(FadeIn(exp_in_base, shift=UP * 0.08), FadeIn(exp_in_power, shift=UP * 0.08), FadeIn(exp_out, shift=UP * 0.08))
        self.play(FadeIn(log_in, shift=UP * 0.08), FadeIn(log_out, shift=UP * 0.08))

        token = Dot(color=WHITE).move_to(exp_in_base.get_center())
        self.add(token)

        p1 = VMobject()
        p1.set_points_smoothly([exp_in_base.get_center(), exp_in_power.get_center(), exp_out.get_center()])
        self.play(MoveAlongPath(token, p1), run_time=1.5)
        self.play(token.animate.move_to(log_in.get_center()), run_time=0.35)
        p2 = VMobject()
        p2.set_points_smoothly([log_in.get_center(), log_out.get_center()])
        self.play(MoveAlongPath(token, p2), run_time=1.1)
        self.wait(1.0)

    def number_line_section(self):
        title = self.title_block("Number Line Meaning", "Logs compress multiplicative growth into manageable steps.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        top = NumberLine(x_range=[0, 4, 1], length=11, include_numbers=False, color=TEXT)
        bottom = NumberLine(x_range=[0, 4, 1], length=11, include_numbers=False, color=TEXT)
        top.to_edge(UP, buff=1.45).shift(DOWN * 0.1)
        bottom.to_edge(DOWN, buff=1.15)

        top_label = Text("1 → 10 → 100 → 1000 → 10000", font_size=24, color=WHITE)
        top_label.next_to(top, UP, buff=0.18)
        bottom_label = Text("0 → 1 → 2 → 3 → 4", font_size=24, color=WHITE)
        bottom_label.next_to(bottom, UP, buff=0.18)

        self.play(Create(top), Create(bottom))
        self.play(FadeIn(top_label), FadeIn(bottom_label))

        xs = [0, 1, 2, 3, 4]
        vals = [1, 10, 100, 1000, 10000]

        for x, v in zip(xs, vals):
            d1 = Dot(top.n2p(x), radius=0.07, color=ACCENT)
            d2 = Dot(bottom.n2p(x), radius=0.07, color=LOGCOLOR)
            l1 = MathTex(str(v), font_size=26, color=WHITE)
            l1.next_to(d1, UP, buff=0.12)
            l2 = MathTex(str(x), font_size=26, color=WHITE)
            l2.next_to(d2, DOWN, buff=0.12)
            self.play(FadeIn(d1), FadeIn(d2), FadeIn(l1), FadeIn(l2), run_time=0.3)

        note = Text("The log scale turns huge jumps into equal steps.", font_size=26, color=TEXT)
        note.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(note, shift=UP * 0.1))
        self.wait(0.7)

        tracker = ValueTracker(0)
        moving = always_redraw(lambda: Dot(top.n2p(tracker.get_value()), radius=0.1, color=RESULT))
        moving_lbl = always_redraw(lambda: MathTex(rf"10^{{{int(tracker.get_value())}}}", font_size=30, color=RESULT).next_to(moving, UP, buff=0.12))
        self.add(moving, moving_lbl)
        self.play(tracker.animate.set_value(4), run_time=2.8, rate_func=linear)
        self.wait(0.8)

    def applications_section(self):
        title = self.title_block("Real-World Applications", "Logs appear whenever scales grow by orders of magnitude.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        items = [
            ("Earthquakes", "Magnitude scales"),
            ("Sound", "Decibels"),
            ("Population", "Exponential growth"),
            ("Computer science", "O(log n) algorithms"),
            ("Storage", "KB → MB → GB → TB"),
            ("Chemistry", "pH scale"),
        ]

        cards = VGroup()
        for a, b in items:
            box = RoundedRectangle(corner_radius=0.2, width=4.0, height=1.08)
            box.set_fill("#13233d", opacity=0.95)
            box.set_stroke("#2c4266", width=2)
            t1 = Text(a, font_size=25, weight=BOLD, color=WHITE)
            t2 = Text(b, font_size=21, color=TEXT)
            t1.move_to(box).shift(UP * 0.16)
            t2.move_to(box).shift(DOWN * 0.2)
            cards.add(VGroup(box, t1, t2))

        cards.arrange_in_grid(rows=3, cols=2, buff=0.38)
        cards.scale(0.84).shift(DOWN * 0.1)

        self.play(LaggedStart(*[FadeIn(c[0], scale=0.92) for c in cards], lag_ratio=0.12), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(c[1], shift=LEFT * 0.08) for c in cards], lag_ratio=0.08), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(c[2], shift=LEFT * 0.08) for c in cards], lag_ratio=0.08), run_time=0.8)

        takeaway = Text("A logarithm is useful when linear thinking is too small for the scale.", font_size=26, color=WHITE)
        takeaway.to_edge(DOWN, buff=0.4)
        self.play(Write(takeaway))
        self.wait(1.0)

    def log_laws_one(self):
        header = Text("Product Rule", font_size=28, weight=BOLD, color=WHITE)
        formula = MathTex(r"\log_b(MN)=\log_b(M)+\log_b(N)", font_size=42)
        formula.set_color(LOGCOLOR)
        formula.next_to(header, DOWN, buff=0.2)

        step1 = MathTex(r"M=b^x,\quad N=b^y", font_size=36)
        step2 = MathTex(r"MN=b^{x+y}", font_size=36)
        step3 = MathTex(r"\log_b(MN)=x+y", font_size=36)
        step4 = MathTex(r"x+y=\log_b(M)+\log_b(N)", font_size=36)

        for m in (step1, step2, step3):
            m.set_color_by_tex("b", BASE)
        step3.set_color(LOGCOLOR)
        step4.set_color(LOGCOLOR)

        group = VGroup(header, formula, step1, step2, step3, step4).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        group.to_edge(UP, buff=1.05).shift(LEFT * 0.35)

        self.play(Write(header), Write(formula))
        self.play(Write(step1))
        self.play(TransformMatchingTex(step1.copy(), step2))
        self.play(TransformMatchingTex(step2.copy(), step3))
        self.play(TransformMatchingTex(step3.copy(), step4))
        self.wait(0.5)
        return group

    def log_laws_two(self):
        header = Text("Quotient Rule", font_size=28, weight=BOLD, color=WHITE)
        formula = MathTex(r"\log_b(M/N)=\log_b(M)-\log_b(N)", font_size=42)
        formula.set_color(LOGCOLOR)
        formula.next_to(header, DOWN, buff=0.2)

        step1 = MathTex(r"M=b^x,\quad N=b^y", font_size=36)
        step2 = MathTex(r"M/N=b^{x-y}", font_size=36)
        step3 = MathTex(r"\log_b(M/N)=x-y", font_size=36)
        step4 = MathTex(r"x-y=\log_b(M)-\log_b(N)", font_size=36)

        for m in (step1, step2):
            m.set_color_by_tex("b", BASE)
        step3.set_color(LOGCOLOR)
        step4.set_color(LOGCOLOR)

        group = VGroup(header, formula, step1, step2, step3, step4).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        group.to_edge(UP, buff=1.05).shift(LEFT * 0.35)

        self.play(Write(header), Write(formula))
        self.play(Write(step1))
        self.play(TransformMatchingTex(step1.copy(), step2))
        self.play(TransformMatchingTex(step2.copy(), step3))
        self.play(TransformMatchingTex(step3.copy(), step4))
        self.wait(0.5)
        return group

    def log_laws_three(self):
        header = Text("Power Rule", font_size=28, weight=BOLD, color=WHITE)
        formula = MathTex(r"\log_b(M^n)=n\log_b(M)", font_size=42)
        formula.set_color(LOGCOLOR)
        formula.next_to(header, DOWN, buff=0.2)

        step1 = MathTex(r"M=b^x", font_size=36)
        step2 = MathTex(r"M^n=(b^x)^n=b^{xn}", font_size=36)
        step3 = MathTex(r"\log_b(M^n)=xn", font_size=36)
        step4 = MathTex(r"xn=n\log_b(M)", font_size=36)

        for m in (step1, step2):
            m.set_color_by_tex("b", BASE)
        step3.set_color(LOGCOLOR)
        step4.set_color(LOGCOLOR)

        group = VGroup(header, formula, step1, step2, step3, step4).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        group.to_edge(UP, buff=1.05).shift(LEFT * 0.35)

        self.play(Write(header), Write(formula))
        self.play(Write(step1))
        self.play(TransformMatchingTex(step1.copy(), step2))
        self.play(TransformMatchingTex(step2.copy(), step3))
        self.play(TransformMatchingTex(step3.copy(), step4))
        self.wait(0.5)
        return group

    def log_laws_section(self):
        block1 = self.log_laws_one()
        self.play(FadeOut(block1), run_time=0.5)

        block2 = self.log_laws_two()
        self.play(FadeOut(block2), run_time=0.5)

        block3 = self.log_laws_three()
        self.wait(1.0)
        self.play(FadeOut(block3), run_time=0.6)

    def common_mistakes_section(self):
        title = self.title_block("Common Mistakes", "Read the notation carefully.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        cards = []
        entries = [
            (r"\log(a+b)\neq\log(a)+\log(b)", DANGER, "No sum rule"),
            (r"\log_b(x)", LOGCOLOR, "Base stays outside"),
            (r"\log_b(b^x)=x", RESULT, "Undoing works"),
            (r"b^{\log_b(x)}=x", RESULT, "Only for x>0"),
        ]
        for tex, color, caption in entries:
            box = RoundedRectangle(corner_radius=0.2, width=5.35, height=1.16)
            box.set_fill("#13233d", opacity=0.95)
            box.set_stroke(color, width=2)
            expr = MathTex(tex, font_size=34)
            expr.set_color(color)
            cap = Text(caption, font_size=20, color=TEXT)
            expr.move_to(box).shift(UP * 0.12)
            cap.next_to(expr, DOWN, buff=0.08)
            cards.append(VGroup(box, expr, cap))

        cards = VGroup(*cards).arrange_in_grid(rows=2, cols=2, buff=0.42)
        cards.scale(0.88).shift(DOWN * 0.1)

        self.play(LaggedStart(*[FadeIn(c[0], scale=0.93) for c in cards], lag_ratio=0.12), run_time=1.0)
        self.play(LaggedStart(*[Write(c[1]) for c in cards], lag_ratio=0.1), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(c[2], shift=UP * 0.08) for c in cards], lag_ratio=0.08), run_time=0.8)

        xmark = Cross(cards[0][1], color=DANGER, stroke_width=8)
        self.play(Create(xmark), run_time=0.6)
        self.wait(1.0)

    def worked_example_block(self, qtex, stept1, stept2, answer, answer_color=EXPONENT):
        q = MathTex(qtex, font_size=54)
        q.set_color(LOGCOLOR)
        q.to_edge(UP, buff=1.3)

        s1 = MathTex(stept1, font_size=54)
        s1.set_color(BASE)
        s1.move_to(ORIGIN)

        s2 = MathTex(stept2, font_size=54)
        s2.set_color(BASE)
        s2.move_to(ORIGIN)

        ans = MathTex(answer, font_size=54, color=answer_color)
        ans.move_to(DOWN * 1.3)
        return q, s1, s2, ans

    def worked_examples_section(self):
        title = self.title_block("Worked Problems", "Turn the log into an exponent question, then solve.")
        self.play(Write(title[0]), FadeIn(title[1], shift=DOWN * 0.12))
        self.wait(0.2)

        examples = [
            (r"\log_2(64)=?", r"2^x=64", r"2^6=64", r"x=6"),
            (r"\log_3(1/27)=?", r"3^x=1/27", r"3^{-3}=1/27", r"x=-3"),
            (r"\log_5(125)=?", r"5^x=125", r"5^3=125", r"x=3"),
        ]

        for qtex, step1, step2, ans in examples:
            q, s1, s2, a = self.worked_example_block(qtex, step1, step2, ans)
            panel = RoundedRectangle(corner_radius=0.25, width=9.4, height=3.7)
            panel.set_fill("#101a2e", opacity=0.96)
            panel.set_stroke("#2c4266", width=2)
            panel.shift(DOWN * 0.15)

            self.play(FadeIn(panel))
            self.play(Write(q))
            self.play(TransformMatchingTex(q.copy(), s1))
            self.play(TransformMatchingTex(s1.copy(), s2))
            self.play(TransformMatchingTex(s2.copy(), a))
            self.wait(0.65)
            self.play(FadeOut(panel), FadeOut(q), FadeOut(s1), FadeOut(s2), FadeOut(a), run_time=0.5)

        self.wait(0.5)

    def final_summary_section(self):
        top = self.eq_pair(r"b^x=y", r"\log_b(y)=x", left_color=WHITE, right_color=WHITE, font_size=60)
        top[0].set_color_by_tex("b", BASE)
        top[0].set_color_by_tex("x", EXPONENT)
        top[0].set_color_by_tex("y", RESULT)
        top[2].set_color(LOGCOLOR)
        top[2].set_color_by_tex("x", EXPONENT)
        top[2].set_color_by_tex("y", RESULT)
        top.move_to(UP * 0.6)

        box1 = RoundedRectangle(corner_radius=0.24, width=5.0, height=1.15)
        box1.set_fill("#13233d", opacity=0.95)
        box1.set_stroke(BASE, width=2)
        box2 = RoundedRectangle(corner_radius=0.24, width=5.0, height=1.15)
        box2.set_fill("#231338", opacity=0.95)
        box2.set_stroke(LOGCOLOR, width=2)

        left = VGroup(Text("Exponentiation", font_size=28, weight=BOLD, color=BASE), Text("What number do I get?", font_size=26, color=WHITE))
        left.arrange(DOWN, buff=0.12).move_to(box1)
        right = VGroup(Text("Logarithms", font_size=28, weight=BOLD, color=LOGCOLOR), Text("What exponent did I use?", font_size=26, color=WHITE))
        right.arrange(DOWN, buff=0.12).move_to(box2)

        groups = VGroup(VGroup(box1, left), VGroup(box2, right)).arrange(RIGHT, buff=0.6).move_to(DOWN * 1.45)

        self.play(Write(top[0]), Write(top[1]), Write(top[2]))
        self.play(FadeIn(groups[0][0]), FadeIn(groups[1][0]))
        self.play(Write(left[0]), Write(left[1]), Write(right[0]), Write(right[1]))
        self.wait(0.7)

        final = Text(
            "Exponentiation asks: What number do I get?   •   Logs ask: What exponent did I use?",
            font_size=25,
            color=TEXT
        ).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(final, shift=UP * 0.1))
        self.wait(1.8)
