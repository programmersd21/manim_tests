from manim import *
import os

config.background_color = "#08111f"
config.frame_width = 16
config.frame_height = 9

BG = "#08111f"
PANEL = "#0f1b2d"
PANEL_2 = "#13253c"
TEXT = "#f6fbff"
MUTED = "#a8bdd4"
ACCENT = "#63d3ff"
ACCENT_2 = "#8cffc1"
ACCENT_3 = "#ffd36b"
ACCENT_4 = "#ff7aa2"
GOOD = "#8cffc1"
WARN = "#ffd36b"
BAD = "#ff7a7a"

class NEP2020MasterScene(MovingCameraScene):
    def safe_add_sound(self, path, gain=0):
        if path and os.path.exists(path):
            self.add_sound(path, gain=gain)

    def card(self, width, height, fill=PANEL, stroke=WHITE, opacity=0.18, stroke_opacity=0.22, radius=0.22):
        return RoundedRectangle(width=width, height=height, corner_radius=radius, fill_color=fill, fill_opacity=opacity, stroke_color=stroke, stroke_opacity=stroke_opacity, stroke_width=1.2)

    def glow_card(self, width, height, fill=PANEL_2, opacity=0.28):
        base = self.card(width, height, fill=fill, opacity=opacity, stroke_opacity=0.18)
        glow = RoundedRectangle(width=width + 0.2, height=height + 0.2, corner_radius=0.25, fill_opacity=0, stroke_color=ACCENT, stroke_opacity=0.12, stroke_width=4)
        return VGroup(glow, base)

    def title_block(self, kicker, title, subtitle, width=14.0):
        kicker_m = Text(kicker, font_size=22, color=ACCENT_2, weight=BOLD)
        title_m = Text(title, font_size=44, color=TEXT, weight=BOLD)
        subtitle_m = Text(subtitle, font_size=24, color=MUTED)
        group = VGroup(kicker_m, title_m, subtitle_m).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        group.width = min(group.width, width)
        return group

    def tag(self, text, color=ACCENT, txt_color=BG):
        pill = RoundedRectangle(width=0.1, height=0.1, corner_radius=0.2, fill_color=color, fill_opacity=1, stroke_width=0)
        label = Text(text, font_size=20, color=txt_color, weight=BOLD)
        group = VGroup(pill, label).arrange(RIGHT, buff=0.18, center=False)
        pill.stretch_to_fit_width(label.width + 0.45)
        pill.stretch_to_fit_height(label.height + 0.22)
        return group

    def section_label(self, index, title):
        box = self.tag(f"{index:02d}", ACCENT_3)
        txt = Text(title, font_size=26, color=TEXT, weight=BOLD)
        return VGroup(box, txt).arrange(RIGHT, buff=0.28, aligned_edge=DOWN)

    def info_chip(self, text, color=ACCENT, width=None):
        chip = RoundedRectangle(width=0.1, height=0.1, corner_radius=0.18, fill_color=color, fill_opacity=0.18, stroke_color=color, stroke_opacity=0.7, stroke_width=1.2)
        label = Text(text, font_size=18, color=TEXT)
        if width is None:
            chip.stretch_to_fit_width(label.width + 0.45)
        else:
            chip.stretch_to_fit_width(width)
        chip.stretch_to_fit_height(label.height + 0.18)
        return VGroup(chip, label)

    def bullet_row(self, text, color=ACCENT_2):
        dot = Dot(radius=0.06, color=color)
        label = Text(text, font_size=20, color=TEXT)
        return VGroup(dot, label).arrange(RIGHT, buff=0.18, aligned_edge=UP)

    def timeline_block(self, title, age_text, color):
        rect = RoundedRectangle(width=3.0, height=1.4, corner_radius=0.18, fill_color=color, fill_opacity=0.22, stroke_color=color, stroke_opacity=0.8, stroke_width=2)
        t1 = Text(title, font_size=24, color=TEXT, weight=BOLD)
        t2 = Text(age_text, font_size=18, color=TEXT)
        return VGroup(rect, VGroup(t1, t2).arrange(DOWN, buff=0.08))

    def metric(self, value, label, color=ACCENT):
        num = Text(value, font_size=34, color=color, weight=BOLD)
        lab = Text(label, font_size=18, color=TEXT)
        return VGroup(num, lab).arrange(DOWN, buff=0.08)

    def divider(self, width=13.0, color=WHITE, opacity=0.12):
        return Line(LEFT * width / 2, RIGHT * width / 2, stroke_color=color, stroke_opacity=opacity, stroke_width=2)

    def floating_cards(self, labels, colors, scale=1.0):
        cards = VGroup()
        for i, (label, color) in enumerate(zip(labels, colors)):
            r = RoundedRectangle(width=2.2 * scale, height=0.9 * scale, corner_radius=0.18, fill_color=color, fill_opacity=0.16, stroke_color=color, stroke_opacity=0.8, stroke_width=1.6)
            txt = Text(label, font_size=int(18 * scale), color=TEXT, weight=BOLD)
            group = VGroup(r, txt)
            group.shift(RIGHT * i * 2.4 * scale)
            cards.add(group)
        return cards

    def construct(self):
        self.safe_add_sound("audio/bgm.mp3", gain=-10)
        self.scene_hook()
        self.scene_old_system()
        self.scene_structure()
        self.scene_foundational()
        self.scene_preparatory()
        self.scene_middle()
        self.scene_secondary()
        self.scene_assessment()
        self.scene_major_reforms()
        self.scene_before_after()
        self.scene_memory_palace()
        self.scene_finale()

    def scene_hook(self):
        self.camera.frame.save_state()
        bg = self.card(15.8, 8.6, fill="#0c1626", opacity=1, stroke_opacity=0)
        haze = Circle(radius=2.0, fill_color=ACCENT, fill_opacity=0.08, stroke_width=0).shift(LEFT * 4.3 + UP * 1.6)
        haze2 = Circle(radius=1.7, fill_color=ACCENT_2, fill_opacity=0.08, stroke_width=0).shift(RIGHT * 4.2 + DOWN * 1.2)
        title = self.title_block("NEP 2020", "India’s education system is changing forever.", "A cinematic guide to the National Education Policy 2020")
        title.move_to(UP * 2.2 + LEFT * 2.8)
        badge = self.tag("Premium Study Guide", ACCENT_3)
        badge.next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        skyline = VGroup()
        for x, h, c in [(-5.8, 2.0, PANEL_2), (-4.6, 3.0, PANEL), (-3.2, 2.4, PANEL_2), (-1.9, 3.4, PANEL), (-0.4, 2.2, PANEL_2)]:
            b = RoundedRectangle(width=0.9, height=h, corner_radius=0.08, fill_color=c, fill_opacity=0.8, stroke_width=0).shift(DOWN * 2.8 + RIGHT * x)
            skyline.add(b)
        school = RoundedRectangle(width=2.2, height=1.6, corner_radius=0.12, fill_color=PANEL_2, fill_opacity=0.92, stroke_color=ACCENT, stroke_opacity=0.3).shift(RIGHT * 4.6 + DOWN * 1.8)
        roof = Polygon(school.get_left() + UP * 0.8, school.get_top() + UP * 0.25, school.get_right() + UP * 0.8, color=ACCENT, fill_color=ACCENT, fill_opacity=0.2, stroke_opacity=0.4)
        students = VGroup(*[Circle(radius=0.17, fill_color=c, fill_opacity=1, stroke_width=0).shift(RIGHT * (4.0 + i * 0.45) + DOWN * 2.7) for i, c in enumerate([ACCENT, ACCENT_2, ACCENT_3, ACCENT_4])])
        book = RoundedRectangle(width=1.4, height=1.0, corner_radius=0.1, fill_color=ACCENT_3, fill_opacity=0.95, stroke_color=WHITE, stroke_opacity=0.2).shift(LEFT * 2.3 + DOWN * 1.0)
        digital = RoundedRectangle(width=1.4, height=1.0, corner_radius=0.1, fill_color=ACCENT, fill_opacity=0.92, stroke_color=WHITE, stroke_opacity=0.2).shift(LEFT * 0.2 + DOWN * 1.0)
        arrow = Arrow(book.get_right(), digital.get_left(), buff=0.12, stroke_width=5, color=ACCENT_2)
        book_txt = Text("Books", font_size=22, color=BG, weight=BOLD).move_to(book)
        digi_txt = Text("Digital", font_size=22, color=BG, weight=BOLD).move_to(digital)
        self.camera.frame.scale(0.94)
        self.play(FadeIn(bg), FadeIn(haze), FadeIn(haze2), run_time=0.7)
        self.play(LaggedStart(FadeIn(skyline, shift=DOWN * 0.3), FadeIn(school, shift=DOWN * 0.4), FadeIn(roof, shift=DOWN * 0.2), FadeIn(students, lag_ratio=0.12), lag_ratio=0.18), run_time=1.6)
        self.play(FadeIn(title, shift=DOWN * 0.3), FadeIn(badge, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(book, shift=LEFT * 0.2), FadeIn(digital, shift=RIGHT * 0.2), FadeIn(arrow), Write(book_txt), Write(digi_txt), run_time=1.4)
        self.play(Indicate(digital, scale_factor=1.03, color=ACCENT), run_time=0.8)
        self.play(self.camera.frame.animate.scale(1.08).move_to(LEFT * 0.2 + UP * 0.2), run_time=1.2)
        self.play(FadeOut(VGroup(bg, haze, haze2, skyline, school, roof, students, book, digital, arrow, book_txt, digi_txt, title, badge)), run_time=0.8)
        self.camera.frame.restore()

    def scene_old_system(self):
        self.safe_add_sound("audio/transition.mp3", gain=-8)
        header = self.section_label(2, "Why change was needed")
        header.to_edge(UP, buff=0.45)
        old_card = self.glow_card(6.4, 4.7, fill="#201323", opacity=0.28).shift(LEFT * 3.75 + DOWN * 0.1)
        old_title = Text("Old System", font_size=30, color=TEXT, weight=BOLD).move_to(old_card[1].get_top() + DOWN * 0.5)
        structure = Text("10 + 2", font_size=52, color=BAD, weight=BOLD).move_to(old_card[1].get_center() + UP * 0.6)
        problem_labels = ["Rote learning", "Exam pressure", "Rigid streams", "Low flexibility"]
        problem_rows = VGroup(*[self.bullet_row(p, BAD) for p in problem_labels]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        problem_rows.next_to(structure, DOWN, buff=0.35, aligned_edge=LEFT)
        for row in problem_rows:
            row.align_to(old_card[1].get_left(), LEFT)
        break_line = Line(old_card[1].get_left() + RIGHT * 0.65, old_card[1].get_right() + LEFT * 0.65, color=BAD, stroke_width=5).shift(UP * 0.2)
        crack = VMobject().set_points_as_corners([LEFT * 0.3 + DOWN * 0.2, LEFT * 0.1 + UP * 0.4, RIGHT * 0.1 + DOWN * 0.1, RIGHT * 0.3 + UP * 0.45])
        crack.set_stroke(BAD, width=4)
        solution = self.glow_card(6.2, 4.7, fill="#12293b", opacity=0.26).shift(RIGHT * 3.75 + DOWN * 0.1)
        solution_title = Text("The Solution", font_size=30, color=TEXT, weight=BOLD).move_to(solution[1].get_top() + DOWN * 0.5)
        solution_text = Text("A flexible, multidisciplinary, learner-centered structure.", font_size=24, color=TEXT, line_spacing=0.8, weight=BOLD)
        solution_text.set_width(5.0)
        solution_text.next_to(solution_title, DOWN, buff=0.55)
        cards = self.floating_cards(["Flexibility", "Skills", "Depth", "Choice"], [ACCENT, ACCENT_2, ACCENT_3, ACCENT_4], scale=0.85)
        cards.arrange(DOWN, buff=0.22).next_to(solution_text, DOWN, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(old_card, shift=LEFT * 0.2), FadeIn(solution, shift=RIGHT * 0.2), run_time=0.9)
        self.play(Write(old_title), Write(structure), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in problem_rows], lag_ratio=0.12), run_time=1.0)
        self.play(Create(break_line), Create(crack), run_time=0.8)
        self.play(FadeIn(solution_title, shift=DOWN * 0.15), FadeIn(solution_text, shift=DOWN * 0.15), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(card, shift=UP * 0.15) for card in cards], lag_ratio=0.14), run_time=1.0)
        self.play(Indicate(solution_text, color=ACCENT_2, scale_factor=1.02), run_time=0.7)
        self.play(FadeOut(VGroup(header, old_card, old_title, structure, problem_rows, break_line, crack, solution, solution_title, solution_text, cards)), run_time=0.8)

    def scene_structure(self):
        self.safe_add_sound("audio/whoosh.mp3", gain=-7)
        header = self.section_label(3, "The 5+3+3+4 structure")
        header.to_edge(UP, buff=0.45)
        subtitle = Text("A complete redesign of the school journey", font_size=24, color=MUTED)
        subtitle.next_to(header, DOWN, buff=0.18, aligned_edge=LEFT)
        path = Line(LEFT * 6.0, RIGHT * 6.0, color=WHITE, stroke_opacity=0.18, stroke_width=6).shift(DOWN * 0.5)
        blocks = VGroup(
            self.timeline_block("Foundational", "3–8 years", ACCENT_3),
            self.timeline_block("Preparatory", "8–11 years", ACCENT),
            self.timeline_block("Middle", "11–14 years", ACCENT_2),
            self.timeline_block("Secondary", "14–18 years", ACCENT_4),
        ).arrange(RIGHT, buff=0.42)
        blocks.shift(DOWN * 0.15)
        n1 = Circle(radius=0.14, fill_color=ACCENT_3, fill_opacity=1, stroke_width=0).move_to(blocks[0].get_left() + DOWN * 0.55)
        n2 = Circle(radius=0.14, fill_color=ACCENT, fill_opacity=1, stroke_width=0).move_to(blocks[1].get_left() + DOWN * 0.55)
        n3 = Circle(radius=0.14, fill_color=ACCENT_2, fill_opacity=1, stroke_width=0).move_to(blocks[2].get_left() + DOWN * 0.55)
        n4 = Circle(radius=0.14, fill_color=ACCENT_4, fill_opacity=1, stroke_width=0).move_to(blocks[3].get_left() + DOWN * 0.55)
        age_labels = VGroup(*[Text(a, font_size=18, color=TEXT, weight=BOLD).next_to(b[0], DOWN, buff=0.15) for a, b in zip(["3–8", "8–11", "11–14", "14–18"], blocks)])
        giant = Text("5 + 3 + 3 + 4", font_size=58, color=TEXT, weight=BOLD).to_edge(DOWN, buff=0.7)
        expl = Text("One continuous pathway, not isolated fragments.", font_size=24, color=MUTED)
        expl.next_to(giant, UP, buff=0.18)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(subtitle, shift=DOWN * 0.15), run_time=0.7)
        self.play(Create(path), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.18) for b in blocks], lag_ratio=0.12), run_time=1.4)
        self.play(FadeIn(VGroup(n1, n2, n3, n4)), FadeIn(age_labels, shift=UP * 0.12), run_time=0.8)
        self.play(Write(expl), Write(giant), run_time=1.0)
        for b in blocks:
            self.play(Indicate(b, scale_factor=1.03, color=b[0].get_fill_color()), run_time=0.55)
        self.play(FadeOut(VGroup(header, subtitle, path, blocks, n1, n2, n3, n4, age_labels, giant, expl)), run_time=0.8)

    def scene_foundational(self):
        header = self.section_label(4, "Foundational stage")
        header.to_edge(UP, buff=0.45)
        frame = self.card(15.2, 7.2, fill="#102033", opacity=0.92, stroke_opacity=0.08)
        frame.shift(DOWN * 0.35)
        sun = Circle(radius=0.55, fill_color=ACCENT_3, fill_opacity=0.35, stroke_width=0).shift(LEFT * 5.0 + UP * 2.0)
        clouds = VGroup(*[Circle(radius=r, fill_color=WHITE, fill_opacity=0.08, stroke_width=0).shift(pos) for r, pos in [(0.45, LEFT * 3.0 + UP * 2.2), (0.35, LEFT * 2.4 + UP * 2.1), (0.32, LEFT * 2.0 + UP * 2.3)]])
        ground = RoundedRectangle(width=14.0, height=2.0, corner_radius=0.15, fill_color="#17301f", fill_opacity=0.95, stroke_width=0).shift(DOWN * 2.1)
        mat = RoundedRectangle(width=3.3, height=1.7, corner_radius=0.18, fill_color="#204d36", fill_opacity=0.9, stroke_color=ACCENT_2, stroke_opacity=0.2).shift(LEFT * 3.9 + DOWN * 0.95)
        story = RoundedRectangle(width=3.1, height=1.55, corner_radius=0.18, fill_color="#2d274f", fill_opacity=0.88, stroke_color=ACCENT, stroke_opacity=0.2).shift(LEFT * 0.7 + DOWN * 0.92)
        toy = RoundedRectangle(width=3.0, height=1.45, corner_radius=0.18, fill_color="#4c2f33", fill_opacity=0.88, stroke_color=ACCENT_4, stroke_opacity=0.2).shift(RIGHT * 2.5 + DOWN * 0.92)
        labels = [
            (mat, "Play-based learning", ACCENT_2),
            (story, "Stories & language", ACCENT),
            (toy, "Toys & numeracy", ACCENT_3),
        ]
        parts = VGroup()
        for rect, txt, col in labels:
            icon = Circle(radius=0.16, fill_color=col, fill_opacity=1, stroke_width=0).move_to(rect.get_top() + DOWN * 0.35 + LEFT * 0.95)
            tx = Text(txt, font_size=22, color=TEXT, weight=BOLD).move_to(rect)
            parts.add(VGroup(rect, icon, tx))
        note = Text("Warm, joyful, language-rich foundations", font_size=26, color=TEXT, weight=BOLD).next_to(frame, UP, buff=0.2).shift(DOWN * 0.3)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(frame), FadeIn(sun), FadeIn(clouds), FadeIn(ground), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in parts], lag_ratio=0.15), run_time=1.3)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
        for rect, txt, col in labels:
            self.play(rect.animate.scale(1.03), Indicate(txt, color=col, scale_factor=1.02), run_time=0.55)
        self.play(FadeOut(VGroup(header, frame, sun, clouds, ground, parts, note)), run_time=0.8)

    def scene_preparatory(self):
        header = self.section_label(5, "Preparatory stage")
        header.to_edge(UP, buff=0.45)
        center = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=0.18, stroke_color=ACCENT, stroke_opacity=0.5).shift(LEFT * 4.4 + UP * 0.4)
        center_txt = Text("Discovery", font_size=24, color=TEXT, weight=BOLD).move_to(center)
        cards = VGroup()
        data = [("Art", ACCENT_4), ("Maths", ACCENT_3), ("Language", ACCENT), ("Physical activity", ACCENT_2)]
        for i, (label, col) in enumerate(data):
            rect = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.16, fill_color=col, fill_opacity=0.18, stroke_color=col, stroke_opacity=0.8, stroke_width=1.8)
            txt = Text(label, font_size=20, color=TEXT, weight=BOLD).move_to(rect)
            group = VGroup(rect, txt)
            group.shift(RIGHT * (i * 2.8 - 1.3) + UP * (0.9 if i % 2 == 0 else -0.1))
            cards.add(group)
        arrows = VGroup(*[Arrow(center.get_right(), c[0].get_left(), buff=0.12, stroke_width=4, color=c[0].get_stroke_color()) for c in cards])
        ribbon = Text("Broad exposure before specialization", font_size=26, color=MUTED).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(center, scale=0.8), Write(center_txt), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.18) for c in cards], lag_ratio=0.12), run_time=1.3)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.08), run_time=0.9)
        self.play(Write(ribbon), run_time=0.7)
        self.play(Indicate(cards[0], color=ACCENT_4), Indicate(cards[1], color=ACCENT_3), run_time=0.8)
        self.play(FadeOut(VGroup(header, center, center_txt, cards, arrows, ribbon)), run_time=0.8)

    def scene_middle(self):
        header = self.section_label(6, "Middle stage")
        header.to_edge(UP, buff=0.45)
        panel = self.card(15.0, 7.3, fill="#102033", opacity=0.96, stroke_opacity=0.08).shift(DOWN * 0.3)
        left = VGroup()
        for i, txt in enumerate(["Science", "Maths", "Social Science", "Humanities"]):
            rect = RoundedRectangle(width=2.8, height=1.0, corner_radius=0.15, fill_color=[ACCENT, ACCENT_2, ACCENT_3, ACCENT_4][i], fill_opacity=0.2, stroke_color=[ACCENT, ACCENT_2, ACCENT_3, ACCENT_4][i], stroke_opacity=0.8, stroke_width=1.6)
            label = Text(txt, font_size=20, color=TEXT, weight=BOLD).move_to(rect)
            left.add(VGroup(rect, label))
        left.arrange(DOWN, buff=0.22).move_to(LEFT * 4.2 + UP * 0.5)
        vocational = RoundedRectangle(width=5.3, height=3.1, corner_radius=0.2, fill_color="#173146", fill_opacity=0.92, stroke_color=ACCENT_2, stroke_opacity=0.7, stroke_width=2).shift(RIGHT * 3.4 + UP * 0.2)
        voc_title = Text("Vocational education begins", font_size=26, color=TEXT, weight=BOLD).move_to(vocational.get_top() + DOWN * 0.45)
        grade = Text("Grade 6 → Skills → Real-world exposure", font_size=24, color=ACCENT_2, weight=BOLD).move_to(vocational.get_center() + UP * 0.1)
        toolbox = VGroup(
            RoundedRectangle(width=1.0, height=1.0, corner_radius=0.12, fill_color=ACCENT_3, fill_opacity=0.18, stroke_color=ACCENT_3, stroke_opacity=0.8),
            RoundedRectangle(width=1.0, height=1.0, corner_radius=0.12, fill_color=ACCENT, fill_opacity=0.18, stroke_color=ACCENT, stroke_opacity=0.8),
            RoundedRectangle(width=1.0, height=1.0, corner_radius=0.12, fill_color=ACCENT_4, fill_opacity=0.18, stroke_color=ACCENT_4, stroke_opacity=0.8)
        ).arrange(RIGHT, buff=0.25).move_to(vocational.get_center() + DOWN * 0.95)
        link = Arrow(left[-1].get_right(), vocational.get_left(), buff=0.12, stroke_width=5, color=ACCENT_2)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(panel), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(item, shift=LEFT * 0.15) for item in left], lag_ratio=0.12), run_time=1.0)
        self.play(FadeIn(vocational, shift=RIGHT * 0.2), FadeIn(voc_title), FadeIn(grade), FadeIn(toolbox), Create(link), run_time=1.2)
        self.play(Indicate(grade, color=ACCENT_2, scale_factor=1.02), run_time=0.6)
        self.play(FadeOut(VGroup(header, panel, left, vocational, voc_title, grade, toolbox, link)), run_time=0.8)

    def scene_secondary(self):
        header = self.section_label(7, "Secondary stage")
        header.to_edge(UP, buff=0.45)
        wall = RoundedRectangle(width=15.0, height=6.2, corner_radius=0.18, fill_color="#132037", fill_opacity=0.96, stroke_width=0).shift(DOWN * 0.2)
        split = Line(ORIGIN + UP * 2.7, ORIGIN + DOWN * 2.7, stroke_color=BAD, stroke_width=8).shift(LEFT * 0.1)
        left_side = Text("Arts", font_size=38, color=BAD, weight=BOLD).shift(LEFT * 4.0 + UP * 1.4)
        right_side = Text("Science", font_size=38, color=ACCENT, weight=BOLD).shift(RIGHT * 4.0 + UP * 1.4)
        wall_text = Text("Rigid choice wall", font_size=24, color=MUTED).next_to(split, UP, buff=0.25)
        crack_paths = VGroup(
            Line(LEFT * 0.05 + UP * 2.0, LEFT * 0.25 + UP * 0.9, color=WHITE, stroke_width=4),
            Line(LEFT * 0.25 + UP * 0.9, RIGHT * 0.02 + DOWN * 0.3, color=WHITE, stroke_width=4),
            Line(RIGHT * 0.02 + DOWN * 0.3, RIGHT * 0.3 + DOWN * 1.5, color=WHITE, stroke_width=4),
        )
        mix_title = Text("Flexible multidisciplinary choices", font_size=30, color=TEXT, weight=BOLD).to_edge(DOWN, buff=0.6)
        subjects = VGroup(*[
            self.info_chip("Physics", ACCENT),
            self.info_chip("Music", ACCENT_4),
            self.info_chip("Coding", ACCENT_2),
            self.info_chip("Economics", ACCENT_3),
            self.info_chip("Design", GOOD),
        ]).arrange(RIGHT, buff=0.24).shift(DOWN * 1.2)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(wall), run_time=0.7)
        self.play(Write(left_side), Write(right_side), FadeIn(split), FadeIn(wall_text), run_time=0.8)
        self.play(Create(crack_paths), run_time=0.8)
        self.play(FadeOut(VGroup(split, wall_text)), FadeIn(mix_title, shift=UP * 0.12), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in subjects], lag_ratio=0.1), run_time=1.1)
        self.play(Indicate(subjects[2], color=ACCENT_2), Indicate(subjects[0], color=ACCENT), run_time=0.8)
        self.play(FadeOut(VGroup(header, wall, left_side, right_side, crack_paths, mix_title, subjects)), run_time=0.8)

    def scene_assessment(self):
        header = self.section_label(8, "360 degree assessment")
        header.to_edge(UP, buff=0.45)
        wheel_center = Circle(radius=0.82, fill_color=ACCENT, fill_opacity=0.16, stroke_color=ACCENT, stroke_opacity=0.7, stroke_width=2).shift(LEFT * 4.0 + UP * 0.2)
        wheel = Circle(radius=2.15, stroke_color=WHITE, stroke_opacity=0.18, stroke_width=4).shift(LEFT * 4.0 + UP * 0.2)
        spokes = VGroup(*[Line(wheel_center.get_center(), wheel.point_at_angle(a), color=[ACCENT, ACCENT_2, ACCENT_3, ACCENT_4][i], stroke_width=5) for i, (a, c) in enumerate(zip([PI/6, PI/2, 5*PI/6, 7*PI/6], [ACCENT, ACCENT_2, ACCENT_3, ACCENT_4]))])
        center_point = wheel_center.get_center()
        labels = VGroup(
            Text("Self", font_size=20, color=TEXT, weight=BOLD).move_to(center_point + (wheel.point_at_angle(PI/6) - center_point) * 0.86),
            Text("Peer", font_size=20, color=TEXT, weight=BOLD).move_to(center_point + (wheel.point_at_angle(PI/2) - center_point) * 0.86),
            Text("Teacher", font_size=20, color=TEXT, weight=BOLD).move_to(center_point + (wheel.point_at_angle(5*PI/6) - center_point) * 0.86),
            Text("Portfolio", font_size=20, color=TEXT, weight=BOLD).move_to(center_point + (wheel.point_at_angle(7*PI/6) - center_point) * 0.86)
        )
        right_card = self.card(7.1, 5.4, fill="#13253c", opacity=0.95, stroke_opacity=0.1).shift(RIGHT * 3.7 + UP * 0.1)
        rtitle = Text("Holistic Progress Card", font_size=28, color=TEXT, weight=BOLD).move_to(right_card.get_top() + DOWN * 0.55)
        radial = VGroup(
            self.metric("Cognitive", "Thinking, understanding", ACCENT),
            self.metric("Affective", "Attitude, values", ACCENT_3),
            self.metric("Psychomotor", "Skills, action", ACCENT_2),
        ).arrange(DOWN, buff=0.42).move_to(right_card.get_center() + DOWN * 0.15)
        card_glow = VGroup(*[Circle(radius=0.52 + i * 0.16, stroke_color=[ACCENT, ACCENT_2, ACCENT_3][i], stroke_width=5, stroke_opacity=0.22, fill_opacity=0).move_to(right_card.get_center() + DOWN * 1.05) for i in range(3)])
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(wheel), FadeIn(wheel_center), FadeIn(right_card), run_time=0.8)
        self.play(Create(spokes), FadeIn(labels), run_time=1.0)
        self.play(Rotate(wheel, angle=TAU/6), Rotate(spokes, angle=TAU/6), run_time=1.1)
        self.play(TransformFromCopy(labels[0], labels[1]), TransformFromCopy(labels[1], labels[2]), run_time=0.7)
        self.play(FadeIn(rtitle, shift=UP * 0.15), FadeIn(radial, shift=UP * 0.12), FadeIn(card_glow), run_time=0.9)
        self.play(LaggedStart(*[Indicate(m, color=[ACCENT, ACCENT_3, ACCENT_2][i], scale_factor=1.03) for i, m in enumerate(radial)], lag_ratio=0.18), run_time=1.2)
        self.play(FadeOut(VGroup(header, wheel, wheel_center, spokes, labels, right_card, rtitle, radial, card_glow)), run_time=0.8)

    def scene_major_reforms(self):
        header = self.section_label(9, "Major reforms")
        header.to_edge(UP, buff=0.45)
        dashboard = self.card(15.2, 7.2, fill="#0f1f33", opacity=0.96, stroke_opacity=0.08).shift(DOWN * 0.3)
        items = [
            ("ECCE", "Early childhood care and education", ACCENT_3),
            ("PARAKH", "Assessment reform body", ACCENT),
            ("NETF", "Technology-enabled learning", ACCENT_2),
            ("6% GDP", "Investment in education", ACCENT_4),
            ("Mother tongue", "Instruction in early years", GOOD),
            ("Integrated B.Ed.", "Stronger teacher preparation", WARN),
            ("GER 100%", "By 2030", ACCENT),
        ]
        cards = VGroup()
        for i, (k, d, c) in enumerate(items):
            rect = RoundedRectangle(width=4.0, height=1.25, corner_radius=0.18, fill_color=c, fill_opacity=0.16, stroke_color=c, stroke_opacity=0.8, stroke_width=1.6)
            key = Text(k, font_size=24, color=TEXT, weight=BOLD)
            desc = Text(d, font_size=16, color=MUTED)
            textg = VGroup(key, desc).arrange(DOWN, buff=0.04, aligned_edge=LEFT)
            textg.move_to(rect)
            group = VGroup(rect, textg)
            cards.add(group)
        cards.arrange_in_grid(rows=3, cols=3, buff=(0.35, 0.28)).move_to(DOWN * 0.2)
        counter = Text("2020 → 2030", font_size=34, color=TEXT, weight=BOLD).to_edge(RIGHT, buff=0.7).shift(UP * 2.5)
        arc = Arc(radius=1.0, angle=TAU * 0.85, color=ACCENT, stroke_width=8).move_to(counter)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(dashboard), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.12) for c in cards], lag_ratio=0.09), run_time=1.4)
        self.play(Write(counter), Create(arc), run_time=1.0)
        for card in cards[:4]:
            self.play(Indicate(card, scale_factor=1.02, color=card[0].get_stroke_color()), run_time=0.45)
        self.play(FadeOut(VGroup(header, dashboard, cards, counter, arc)), run_time=0.8)

    def scene_before_after(self):
        header = self.section_label(10, "Before vs after")
        header.to_edge(UP, buff=0.45)
        left_panel = self.card(7.2, 5.8, fill="#241623", opacity=0.26, stroke_opacity=0.15).shift(LEFT * 3.95 + DOWN * 0.1)
        right_panel = self.card(7.2, 5.8, fill="#13263a", opacity=0.26, stroke_opacity=0.15).shift(RIGHT * 3.95 + DOWN * 0.1)
        left_title = Text("Old system", font_size=30, color=BAD, weight=BOLD).move_to(left_panel.get_top() + DOWN * 0.55)
        right_title = Text("NEP 2020", font_size=30, color=ACCENT_2, weight=BOLD).move_to(right_panel.get_top() + DOWN * 0.55)
        old_points = VGroup(*[self.bullet_row(t, BAD) for t in ["Rigid streams", "Exams first", "Limited choice", "Low flexibility"]]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        new_points = VGroup(*[self.bullet_row(t, ACCENT_2) for t in ["Flexible pathways", "Critical thinking", "Multiple options", "Skill integration"]]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        old_points.next_to(left_title, DOWN, buff=0.45, aligned_edge=LEFT).shift(RIGHT * 0.25)
        new_points.next_to(right_title, DOWN, buff=0.45, aligned_edge=LEFT).shift(RIGHT * 0.25)
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.9, buff=0.1, stroke_width=6, color=ACCENT_3).shift(DOWN * 2.3)
        label = Text("Transformation", font_size=22, color=ACCENT_3, weight=BOLD).next_to(arrow, DOWN, buff=0.15)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(left_panel), FadeIn(right_panel), run_time=0.8)
        self.play(Write(left_title), Write(right_title), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.12) for p in old_points], lag_ratio=0.1), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.12) for p in new_points], lag_ratio=0.1), run_time=1.0)
        self.play(Create(arrow), Write(label), run_time=0.8)
        self.play(TransformFromCopy(old_points[0], new_points[0]), run_time=0.5)
        self.play(Indicate(new_points[1], color=ACCENT_2), run_time=0.5)
        self.play(FadeOut(VGroup(header, left_panel, right_panel, left_title, right_title, old_points, new_points, arrow, label)), run_time=0.8)

    def scene_memory_palace(self):
        header = self.section_label(11, "Memory palace")
        header.to_edge(UP, buff=0.45)
        palace = RoundedRectangle(width=15.0, height=6.9, corner_radius=0.2, fill_color="#102033", fill_opacity=0.95, stroke_opacity=0.08).shift(DOWN * 0.25)
        tower = Text("5 + 3 + 3 + 4", font_size=66, color=TEXT, weight=BOLD).to_edge(LEFT, buff=0.9).shift(UP * 1.15)
        tower_glow = Circle(radius=1.5, fill_color=ACCENT, fill_opacity=0.08, stroke_width=0).move_to(tower)
        anchors = VGroup(
            self.tag("Grade 5 → Mother tongue", GOOD),
            self.tag("Grade 6 → Vocational", ACCENT_2),
            self.tag("PARAKH", ACCENT),
            self.tag("NETF", ACCENT_3),
            self.tag("2030 → GER + B.Ed.", ACCENT_4),
        )
        anchors.arrange(DOWN, buff=0.28, aligned_edge=LEFT).to_edge(RIGHT, buff=0.9).shift(DOWN * 0.05)
        trails = VGroup(*[DashedLine(tower.get_right() + DOWN * 0.2, a[0].get_left(), dash_length=0.12, color=[GOOD, ACCENT_2, ACCENT, ACCENT_3, ACCENT_4][i], stroke_width=3) for i, a in enumerate(anchors)])
        lens = Text("Make the policy sticky.", font_size=26, color=MUTED).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(header, shift=DOWN * 0.2), FadeIn(palace), FadeIn(tower_glow), run_time=0.7)
        self.play(Write(tower), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(a, shift=LEFT * 0.12) for a in anchors], lag_ratio=0.1), run_time=1.0)
        self.play(LaggedStart(*[Create(t) for t in trails], lag_ratio=0.08), run_time=1.0)
        self.play(Write(lens), run_time=0.6)
        self.play(Indicate(anchors[1], color=ACCENT_2), Indicate(anchors[4], color=ACCENT_4), run_time=0.9)
        self.play(FadeOut(VGroup(header, palace, tower_glow, tower, anchors, trails, lens)), run_time=0.8)

    def scene_finale(self):
        self.safe_add_sound("audio/finale.mp3", gain=-8)
        bg = self.card(15.8, 8.8, fill="#07131f", opacity=1, stroke_opacity=0)
        halo = Circle(radius=2.4, fill_color=ACCENT, fill_opacity=0.08, stroke_width=0).shift(LEFT * 3.5 + UP * 1.1)
        halo2 = Circle(radius=1.9, fill_color=ACCENT_2, fill_opacity=0.08, stroke_width=0).shift(RIGHT * 3.4 + DOWN * 0.7)
        india = VMobject()
        india.set_points_smoothly([
            LEFT * 1.0 + DOWN * 0.9,
            LEFT * 0.7 + UP * 0.8,
            LEFT * 0.2 + UP * 1.2,
            RIGHT * 0.4 + UP * 0.7,
            RIGHT * 0.8 + DOWN * 0.1,
            RIGHT * 0.4 + DOWN * 1.0,
            LEFT * 0.3 + DOWN * 1.3,
        ])
        india.set_stroke(ACCENT_3, width=6, opacity=0.9)
        india.set_fill(ACCENT_3, opacity=0.12)
        india.scale(1.7).shift(RIGHT * 2.9 + DOWN * 0.2)
        lines = VGroup(*[Text(t, font_size=28, color=TEXT, weight=BOLD) for t in ["Flexible Learning", "Strong Foundations", "Skill-Oriented Education", "Future Ready India"]]).arrange(DOWN, buff=0.22).shift(LEFT * 3.0)
        finale = Text("NEP 2020", font_size=58, color=ACCENT_2, weight=BOLD).to_edge(DOWN, buff=0.55)
        sub = Text("A policy built for depth, choice, and capability.", font_size=24, color=MUTED).next_to(finale, UP, buff=0.18)
        spark = VGroup(*[Star(outer_radius=0.12 + 0.03 * i, color=[ACCENT, ACCENT_2, ACCENT_3][i % 3]).shift(LEFT * 4.6 + UP * (1.7 - i * 0.5)) for i in range(6)])
        self.play(FadeIn(bg), FadeIn(halo), FadeIn(halo2), run_time=0.8)
        self.play(FadeIn(india), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.12) for t in lines], lag_ratio=0.14), run_time=1.1)
        self.play(FadeIn(sub, shift=UP * 0.1), FadeIn(finale, shift=UP * 0.1), run_time=0.9)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in spark], lag_ratio=0.1), run_time=0.8)
        self.play(Indicate(finale, color=ACCENT_2, scale_factor=1.03), run_time=0.8)
        self.play(FadeOut(VGroup(bg, halo, halo2, india, lines, sub, finale, spark)), run_time=0.8)
