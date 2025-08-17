import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import random
import requests
from io import BytesIO
import math
import itertools

# Updated character data with blood type and height
CHARACTER_DATA = [
    {"name": "Honoka Kosaka", "year": 2, "group": "μ's", "blood_type": "O", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/e/e9/Main_Page_Honoka.png/"},
    {"name": "Kotori Minami", "year": 2, "group": "μ's", "blood_type": "O", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/0/02/Main_Page_Kotori.png/"},
    {"name": "Umi Sonoda", "year": 2, "group": "μ's", "blood_type": "A", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/5d/Main_Page_Umi.png/"},
    {"name": "Hanayo Koizumi", "year": 1, "group": "μ's", "blood_type": "A", "height": 156, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/27/Main_Page_Hanayo.png/"},
    {"name": "Rin Hoshizora", "year": 1, "group": "μ's", "blood_type": "AB", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/6/69/Main_Page_Rin.png/"},
    {"name": "Maki Nishikino", "year": 1, "group": "μ's", "blood_type": "A", "height": 161, "image_url": "https://static.wikia.nocookie.net/love-live/images/3/3e/Main_Page_Maki.png/"},
    {"name": "Nico Yazawa", "year": 3, "group": "μ's", "blood_type": "A", "height": 154, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/5f/Main_Page_Nico.png/"},
    {"name": "Eli Ayase", "year": 3, "group": "μ's", "blood_type": "B", "height": 162, "image_url": "https://static.wikia.nocookie.net/love-live/images/1/1b/Main_Page_Eli.png/"},
    {"name": "Nozomi Tojo", "year": 3, "group": "μ's", "blood_type": "O", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/a/ab/Main_Page_Nozomi.png/"},
    {"name": "Chika Takami", "year": 2, "group": "Aqours", "blood_type": "B", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/bc/Main_Page_Chika.png/"},
    {"name": "Riko Sakurauchi", "year": 2, "group": "Aqours", "blood_type": "A", "height": 160, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/c4/Main_Page_Riko.png/"},
    {"name": "Kanan Matsuura", "year": 3, "group": "Aqours", "blood_type": "O", "height": 162, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/8a/Main_Page_Kanan.png/"},
    {"name": "Dia Kurosawa", "year": 3, "group": "Aqours", "blood_type": "A", "height": 162, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/cb/Main_Page_Dia.png/"},
    {"name": "You Watanabe", "year": 2, "group": "Aqours", "blood_type": "AB", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/84/Main_Page_You.png/"},
    {"name": "Yoshiko Tsushima", "year": 1, "group": "Aqours", "blood_type": "O", "height": 156, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/c7/Main_Page_Yoshiko.png/"},
    {"name": "Hanamaru Kunikida", "year": 1, "group": "Aqours", "blood_type": "O", "height": 152, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/85/Main_Page_Hanamaru.png/"},
    {"name": "Mari Ohara", "year": 3, "group": "Aqours", "blood_type": "AB", "height": 163, "image_url": "https://static.wikia.nocookie.net/love-live/images/a/a0/Main_Page_Mari.png/"},
    {"name": "Ruby Kurosawa", "year": 1, "group": "Aqours", "blood_type": "A", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/4/46/Main_Page_Ruby.png/"},
    {"name": "Yu Takasaki", "year": 2, "group": "Nijigaku", "blood_type": "-", "height": 156, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/5a/Main_Page_Yu.png/"},
    {"name": "Ayumu Uehara", "year": 2, "group": "Nijigaku", "blood_type": "A", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/8a/Main_Page_Ayumu.png/"},
    {"name": "Kasumi Nakasu", "year": 1, "group": "Nijigaku", "blood_type": "B", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/ba/Main_Page_Kasumi.png/"},
    {"name": "Shizuku Osaka", "year": 1, "group": "Nijigaku", "blood_type": "A", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/b8/Main_Page_Shizuku.png/"},
    {"name": "Karin Asaka", "year": 3, "group": "Nijigaku", "blood_type": "AB", "height": 167, "image_url": "https://static.wikia.nocookie.net/love-live/images/7/71/Main_Page_Karin.png/"},
    {"name": "Ai Miyashita", "year": 2, "group": "Nijigaku", "blood_type": "A", "height": 163, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/b4/Main_Page_Ai.png/"},
    {"name": "Kanata Konoe", "year": 3, "group": "Nijigaku", "blood_type": "O", "height": 158, "image_url": "https://static.wikia.nocookie.net/love-live/images/9/99/Main_Page_Kanata.png/"},
    {"name": "Setsuna Yuki", "year": 2, "group": "Nijigaku", "blood_type": "O", "height": 154, "image_url": "https://static.wikia.nocookie.net/love-live/images/7/76/Main_Page_Setsuna.png/"},
    {"name": "Emma Verde", "year": 3, "group": "Nijigaku", "blood_type": "O", "height": 166, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/82/Main_Page_Emma.png/"},
    {"name": "Rina Tennoji", "year": 1, "group": "Nijigaku", "blood_type": "B", "height": 149, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/cf/Main_Page_Rina.png/"},
    {"name": "Shioriko Mifune", "year": 1, "group": "Nijigaku", "blood_type": "AB", "height": 160, "image_url": "https://static.wikia.nocookie.net/love-live/images/0/07/Main_Page_Shioriko.png/"},
    {"name": "Mia Taylor", "year": 3, "group": "Nijigaku", "blood_type": "AB", "height": 156, "image_url": "https://static.wikia.nocookie.net/love-live/images/1/13/Main_Page_Mia.png/"},
    {"name": "Lanzhu Zhong", "year": 2, "group": "Nijigaku", "blood_type": "B", "height": 165, "image_url": "https://static.wikia.nocookie.net/love-live/images/d/d3/Main_Page_Lanzhu.png/"},
    {"name": "Kanon Shibuya", "year": 3, "group": "Liella!", "blood_type": "A", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/d/d2/Main_Page_Kanon.png/"},
    {"name": "Keke Tang", "year": 3, "group": "Liella!", "blood_type": "O", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/50/Main_Page_Keke.png/"},
    {"name": "Chisato Arashi", "year": 3, "group": "Liella!", "blood_type": "B", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/f/f5/Main_Page_Chisato.png/"},
    {"name": "Sumire Heanna", "year": 3, "group": "Liella!", "blood_type": "AB", "height": 161, "image_url": "https://static.wikia.nocookie.net/love-live/images/6/65/Main_Page_Sumire.png/"},
    {"name": "Ren Hazuki", "year": 3, "group": "Liella!", "blood_type": "A", "height": 163, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/b3/Main_Page_Ren.png/"},
    {"name": "Kinako Sakurakoji", "year": 2, "group": "Liella!", "blood_type": "O", "height": 159, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/28/Main_Page_Kinako.png/"},
    {"name": "Mei Yoneme", "year": 2, "group": "Liella!", "blood_type": "A", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/6/6c/Main_Page_Mei.png/"},
    {"name": "Shiki Wakana", "year": 2, "group": "Liella!", "blood_type": "B", "height": 161, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/2f/Main_Page_Shiki.png/"},
    {"name": "Natsumi Onitsuka", "year": 2, "group": "Liella!", "blood_type": "AB", "height": 152, "image_url": "https://static.wikia.nocookie.net/love-live/images/9/9a/Main_Page_Natsumi.png/"},
    {"name": "Wien Margarete", "year": 1, "group": "Liella!", "blood_type": "A", "height": 161, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/81/Main_Page_Wien.png/"},
    {"name": "Tomari Onitsuka", "year": 1, "group": "Liella!", "blood_type": "B", "height": 163, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/c0/Main_Page_Tomari.png/"},
    {"name": "Kaho Hinoshita", "year": 3, "group": "Hasunosora", "blood_type": "-", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/23/Main_Page_Kaho.png/"},
    {"name": "Sayaka Murano", "year": 3, "group": "Hasunosora", "blood_type": "-", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/6/69/Main_Page_Sayaka.png/"},
    {"name": "Kozue Otomune", "year": 4, "group": "Hasunosora", "blood_type": "-", "height": 167, "image_url": "https://static.wikia.nocookie.net/love-live/images/4/44/Main_Page_Kozue.png/"},
    {"name": "Tsuzuri Yugiri", "year": 4, "group": "Hasunosora", "blood_type": "-", "height": 171, "image_url": "https://static.wikia.nocookie.net/love-live/images/6/63/Main_Page_Tsuzuri.png/"},
    {"name": "Rurino Osawa", "year": 3, "group": "Hasunosora", "blood_type": "-", "height": 151, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/22/Main_Page_Rurino.png/"},
    {"name": "Megumi Fujishima", "year": 4, "group": "Hasunosora", "blood_type": "-", "height": 160, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/54/Main_Page_Megumi.png/"},
    {"name": "Ginko Momose", "year": 2, "group": "Hasunosora", "blood_type": "-", "height": 162, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/80/Main_Page_Ginko.png/"},
    {"name": "Kosuzu Kachimachi", "year": 2, "group": "Hasunosora", "blood_type": "-", "height": 152, "image_url": "https://static.wikia.nocookie.net/love-live/images/8/8e/Main_Page_Kosuzu.png/"},
    {"name": "Hime Anyoji", "year": 2, "group": "Hasunosora", "blood_type": "-", "height": 160, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/c6/Main_Page_Hime.png/"},
    {"name": "Ceras Yanagida Lilienfeld", "year": 1, "group": "Hasunosora", "blood_type": "-", "height": 153, "image_url": "https://static.wikia.nocookie.net/love-live/images/5/5a/Main_Page_Ceras.png/"},
    {"name": "Izumi Katsuragi", "year": 2, "group": "Hasunosora", "blood_type": "-", "height": 170, "image_url": "https://static.wikia.nocookie.net/love-live/images/0/07/Main_Page_Izumi.png/"},
    {"name": "Polka Takahashi", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "-", "height": 157, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/2e/Main_Page_Polka.png/"},
    {"name": "Mai Azabu", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "B", "height": 154, "image_url": "https://static.wikia.nocookie.net/love-live/images/c/cf/Main_Page_Mai.png/"},
    {"name": "Akira Goto", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "O", "height": 164, "image_url": "https://static.wikia.nocookie.net/love-live/images/1/19/Main_Page_Akira.png/"},
    {"name": "Hanabi Komagata", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "A", "height": 160, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/ba/Main_Page_Hanabi.png/"},
    {"name": "Miracle Kanazawa", "year": 2, "group": "Ikizurai-Bu!", "blood_type": "AB", "height": 152, "image_url": "https://static.wikia.nocookie.net/love-live/images/b/bf/Main_Page_Miracle.png/"},
    {"name": "Noriko Chofu", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "B", "height": 153, "image_url": "https://static.wikia.nocookie.net/love-live/images/0/0a/Main_Page_Noriko.png/"},
    {"name": "Yukuri Harumiya", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "B", "height": 165, "image_url": "https://static.wikia.nocookie.net/love-live/images/e/ef/Main_Page_Yukuri.png/"},
    {"name": "Aurora Konohana", "year": 2, "group": "Ikizurai-Bu!", "blood_type": "O", "height": 162, "image_url": "https://static.wikia.nocookie.net/love-live/images/2/29/Main_Page_Aurora.png/"},
    {"name": "Midori Yamada", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "A", "height": 155, "image_url": "https://static.wikia.nocookie.net/love-live/images/d/d7/Main_Page_Midori.png/"},
    {"name": "Shion Sasaki", "year": 1, "group": "Ikizurai-Bu!", "blood_type": "-", "height": 158, "image_url": "https://static.wikia.nocookie.net/love-live/images/e/e0/Main_Page_Shion.png/"},
]

class LoveLiveTournament:
    def update_group_scrollregion(self, event=None):
            """Update scrollregion when group frame size changes"""
            self.group_canvas.config(scrollregion=self.group_canvas.bbox("all"))
    def __init__(self, root):
        self.root = root
        self.root.title("Love Live Character Sorter")
        self.root.geometry("800x700")  # Increased height for group selection
        self.root.configure(bg="#f0f0f8")

        # Initialize character data
        self.all_characters = CHARACTER_DATA
        self.characters = CHARACTER_DATA[:]  # Start with all characters
        self.char_names = [char["name"] for char in self.characters]

        # Get unique groups in order of appearance
        self.groups = []
        seen = set()
        for char in self.all_characters:
            if char["group"] not in seen:
                seen.add(char["group"])
                self.groups.append(char["group"])
        self.group_vars = {group: tk.BooleanVar(value=True) for group in self.groups}

        # Initialize tournament state
        self.wins = {char["name"]: 0 for char in self.characters}
        self.matchups = []
        self.current_matchup = 0
        self.comparisons_done = 0
        self.skipped_comparisons = 0
        self.total_possible_matchups = math.comb(len(self.char_names), 2)

        # Initialize propagation graph
        self.graph = {name: set() for name in self.char_names}
        self.quick_mode = tk.BooleanVar(value=False)

        # Create matchup pairs
        self.create_matchups()

        # Initialize images dictionary
        self.images = {}

        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create header
        self.header = ttk.Label(
            self.main_frame,
            text="Love Live Character Tournament",
            font=("Arial", 20, "bold"),
            foreground="#ff66aa"
        )
        self.header.pack(pady=10)

        # Create progress label with center alignment
        self.progress_frame = ttk.Frame(self.main_frame)
        self.progress_frame.pack(fill=tk.X, pady=5)
        self.progress_label = ttk.Label(
            self.progress_frame,
            text=self.get_progress_text(),
            font=("Arial", 12),
            anchor="center"  # Center align text
        )
        self.progress_label.pack(fill=tk.X, expand=True)

        # ====== GROUP SELECTION PANEL ======
        group_frame = ttk.LabelFrame(self.main_frame, text="Group Selection", padding=10)
        group_frame.pack(fill=tk.X, padx=20, pady=10)

        # Create select all/none buttons
        btn_frame = ttk.Frame(group_frame)
        btn_frame.pack(fill=tk.X, pady=5)

        ttk.Button(
            btn_frame,
            text="Select All",
            command=lambda: self.toggle_all_groups(True)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_frame,
            text="Select None",
            command=lambda: self.toggle_all_groups(False)
        ).pack(side=tk.LEFT, padx=5)

        # Create group checkboxes in a wrapping frame
        self.group_container = ttk.Frame(group_frame)
        self.group_container.pack(fill=tk.X, padx=5, pady=5)

        # Create group checkbuttons
        for group in self.groups:
            cb = ttk.Checkbutton(
                self.group_container,
                text=group,
                variable=self.group_vars[group],
                command=self.update_character_selection
            )
            cb.pack(side=tk.LEFT, padx=10, pady=2)
        # ====== END GROUP SELECTION ======

        # Create matchup frame
        self.matchup_frame = ttk.Frame(self.main_frame)
        self.matchup_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configure grid layout with fixed spacer
        self.matchup_frame.columnconfigure(0, weight=1)  # Left button column
        self.matchup_frame.columnconfigure(1, weight=0)  # Spacer column (fixed width)
        self.matchup_frame.columnconfigure(2, weight=1)  # Right button column
        self.matchup_frame.rowconfigure(0, weight=1)

        # Create character buttons
        self.char1_btn = ttk.Button(
            self.matchup_frame,
            text="",
            command=lambda: self.record_choice(0),
            width=20
        )

        # Create fixed-width spacer
        self.BUTTON_SPACING = 100
        self.spacer = ttk.Frame(self.matchup_frame, width=self.BUTTON_SPACING)

        self.char2_btn = ttk.Button(
            self.matchup_frame,
            text="",
            command=lambda: self.record_choice(1),
            width=20
        )

        # Grid placement
        self.char1_btn.grid(row=0, column=0, sticky="nsew")
        self.spacer.grid(row=0, column=1)
        self.char2_btn.grid(row=0, column=2, sticky="nsew")

        # ====== SETTINGS PANEL ======
        self.settings_frame = ttk.LabelFrame(self.main_frame, text="Settings", padding=10)
        self.settings_frame.pack(fill=tk.X, padx=20, pady=10)

        # Quick mode toggle
        self.quick_mode_check = ttk.Checkbutton(
            self.settings_frame,
            text="Quick Mode",
            variable=self.quick_mode,
            command=self.reset_tournament
        )
        self.quick_mode_check.pack(anchor=tk.W, padx=5, pady=2)

        # Info label about quick mode
        ttk.Label(
            self.settings_frame,
            text="Use transitive relationships to reduce comparisons.",
            font=("Arial", 9),
            foreground="#666666"
        ).pack(anchor=tk.W, padx=5)
        # ====== END SETTINGS PANEL ======

        # Create instruction label
        self.instruction = ttk.Label(
            self.main_frame,
            text="Select your favorite character between the two!",
            font=("Arial", 10, "italic")
        )
        self.instruction.pack(pady=5)

        # Create results button (initially hidden)
        self.results_btn = ttk.Button(
            self.main_frame,
            text="View Results",
            command=self.show_results,
            state=tk.DISABLED
        )
        self.results_btn.pack(pady=10)

        # Start with first matchup
        self.show_matchup()

    def toggle_all_groups(self, state):
        """Toggle all group checkboxes to specified state"""
        for group in self.groups:
            self.group_vars[group].set(state)
        self.update_character_selection()

    def update_character_selection(self):
        """Update character selection based on group checkboxes"""
        selected_groups = [group for group, var in self.group_vars.items() if var.get()]

        # Filter characters based on selected groups
        self.characters = [char for char in self.all_characters if char["group"] in selected_groups]

        # Check if we have enough characters
        if len(self.characters) >= 2:
            # Reset tournament with new character selection
            self.reset_tournament()
        else:
            # Not enough characters - disable buttons and clear UI
            self.char1_btn.config(text="", image=None, state=tk.DISABLED)
            self.char2_btn.config(text="", image=None, state=tk.DISABLED)
            self.progress_label.config(text="Select at least 2 characters from groups")
            self.results_btn.config(state=tk.DISABLED)

    def get_progress_text(self):
        """Generate progress text based on current mode"""
        if self.quick_mode.get():
            if self.total_possible_matchups > 0:
                progress_percent = (self.comparisons_done + self.skipped_comparisons) / self.total_possible_matchups * 100
                return (
                    f"Comparisons: {self.comparisons_done} made, {self.skipped_comparisons} skipped\n"
                    f"Progress: {progress_percent:.1f}%"
                )
            else:
                return "Select at least 2 characters from groups"
        else:
            if len(self.matchups) > 0:
                return f"Matchup {self.current_matchup+1} of {len(self.matchups)}"
            else:
                return "Select at least 2 characters from groups"

    def create_matchups(self):
        """Create all possible character matchups"""
        names = [char["name"] for char in self.characters]
        self.matchups = []
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                self.matchups.append((names[i], names[j]))
        random.shuffle(self.matchups)
        self.total_possible_matchups = len(self.matchups)

    def get_character_by_name(self, name):
        """Get character data by name"""
        for char in self.characters:
            if char["name"] == name:
                return char
        return None

    def load_image(self, image_url, size=(200, 200)):
        try:
            # Try the modern approach first
            from PIL.Image import Resampling
            resample_filter = Resampling.LANCZOS
        except ImportError:
            # Fallback to legacy constant. Shouldn't be necessary though.
            resample_filter = Image.LANCZOS

        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img = img.resize(size, resample_filter)  # Use the determined filter
            return ImageTk.PhotoImage(img)
        except:
                # Placeholder if no image found
                img = Image.new('RGB', size, color='#ffccdd')
                return ImageTk.PhotoImage(img)

    def show_matchup(self):
        """Display the current matchup"""
        # Check if we have enough characters
        if len(self.characters) < 2:
            self.char1_btn.config(state=tk.DISABLED)
            self.char2_btn.config(state=tk.DISABLED)
            return

        # In quick mode, skip already determined matchups
        if self.quick_mode.get():
            while self.current_matchup < len(self.matchups):
                char1_name, char2_name = self.matchups[self.current_matchup]

                # Check if relationship is already known
                if self.is_known_relationship(char1_name, char2_name):
                    self.skipped_comparisons += 1
                    self.current_matchup += 1
                    self.progress_label.config(text=self.get_progress_text())
                else:
                    break

        # Check if tournament is complete
        if self.current_matchup >= len(self.matchups):
            if len(self.matchups) > 0:  # Only show completion if we had matchups
                self.results_btn.config(state=tk.NORMAL)
                messagebox.showinfo("Sorting Complete", "All matchups completed! Click 'View Results' to see the rankings.")
            return

        char1_name, char2_name = self.matchups[self.current_matchup]
        char1 = self.get_character_by_name(char1_name)
        char2 = self.get_character_by_name(char2_name)

        # Update progress label
        self.progress_label.config(text=self.get_progress_text())

        # Load images
        if char1_name not in self.images:
            self.images[char1_name] = self.load_image(char1["image_url"])
        if char2_name not in self.images:
            self.images[char2_name] = self.load_image(char2["image_url"])

        # Update buttons
        self.char1_btn.config(
            text=f"{char1['name']}",
            image=self.images[char1_name],
            compound=tk.TOP,
            state=tk.NORMAL
        )
        self.char2_btn.config(
            text=f"{char2['name']}",
            image=self.images[char2_name],
            compound=tk.TOP,
            state=tk.NORMAL
        )

    def is_known_relationship(self, char1, char2):
        """Check if relationship between two characters is already known"""
        # Check if char1 is known to be better than char2
        if char2 in self.graph[char1]:
            return True

        # Check if char2 is known to be better than char1
        if char1 in self.graph[char2]:
            return True

        return False

    def update_graph(self, winner, loser):
        """Update the propagation graph with a new comparison result"""
        # Add direct relationship
        self.graph[winner].add(loser)

        # Propagate transitive relationships
        # Winner is better than everyone loser is better than
        for char in list(self.graph[loser]):
            self.graph[winner].add(char)

        # Everyone better than winner is also better than loser
        for char in [c["name"] for c in self.characters]:
            if winner in self.graph[char]:
                self.graph[char].add(loser)
                # Also add everyone loser is better than
                for sub_char in self.graph[loser]:
                    self.graph[char].add(sub_char)

    def record_choice(self, choice_index):
        """Record the user's choice and move to next matchup"""
        char1_name, char2_name = self.matchups[self.current_matchup]

        # Record the win
        winner = char1_name if choice_index == 0 else char2_name
        loser = char2_name if choice_index == 0 else char1_name
        self.wins[winner] += 1
        self.comparisons_done += 1

        # Update propagation graph in quick mode
        if self.quick_mode.get():
            self.update_graph(winner, loser)

        # Move to next matchup
        self.current_matchup += 1
        self.progress_label.config(text=self.get_progress_text())
        self.show_matchup()

    def reset_tournament(self):
        """Reset tournament when quick mode is toggled or groups change"""
        # Reset data structures
        self.wins = {char["name"]: 0 for char in self.characters}
        self.graph = {char["name"]: set() for char in self.characters}
        self.current_matchup = 0
        self.comparisons_done = 0
        self.skipped_comparisons = 0

        # Recreate matchups
        self.create_matchups()

        # Update UI
        self.progress_label.config(text=self.get_progress_text())
        self.results_btn.config(state=tk.DISABLED)
        self.show_matchup()

    def show_results(self):
        """Display tournament results and statistics"""
        # Create results window
        results_window = tk.Toplevel(self.root)
        results_window.title("Sorting Results")
        results_window.geometry("900x700")
        results_window.configure(bg="#f0f0f8")

        # Create notebook for tabs
        notebook = ttk.Notebook(results_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Character rankings tab
        rankings_frame = ttk.Frame(notebook)
        notebook.add(rankings_frame, text="Character Rankings")

        # Create treeview for rankings
        columns = ("Rank", "Character", "Wins", "Year", "Group")
        tree = ttk.Treeview(rankings_frame, columns=columns, show="headings")

        # Define column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        tree.column("Character", width=200)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(rankings_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)

        # Sort characters by wins
        sorted_chars = sorted(self.wins.items(), key=lambda x: x[1], reverse=True)

        # Populate treeview
        for rank, (name, wins) in enumerate(sorted_chars, 1):
            char = self.get_character_by_name(name)
            tree.insert("", tk.END, values=(rank, name, wins, char["year"], char["group"]))

        # Year statistics tab
        year_frame = ttk.Frame(notebook)
        notebook.add(year_frame, text="Year Statistics")

        # Calculate wins by year
        year_wins = {}
        for char in self.characters:
            year = char["year"]
            if year not in year_wins:
                year_wins[year] = 0
            year_wins[year] += self.wins[char["name"]]

        # Create chart for year statistics
        year_canvas = tk.Canvas(year_frame, bg="white")
        year_canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Draw bar chart
        max_wins = max(year_wins.values()) if year_wins else 1
        bar_width = 100
        spacing = 50
        start_x = 100
        start_y = 400
        scale = 300 / max_wins

        # Draw bars and labels
        for i, (year, wins) in enumerate(sorted(year_wins.items())):
            x0 = start_x + i * (bar_width + spacing)
            y0 = start_y
            y1 = start_y - wins * scale
            bar_height = wins * scale

            # Draw bar
            year_canvas.create_rectangle(x0, y0, x0 + bar_width, y1, fill="#ff99cc", outline="black")

            # Draw value
            year_canvas.create_text(
                x0 + bar_width / 2, y1 - 20,
                text=f"{wins} wins",
                font=("Arial", 10, "bold")
            )

            # Draw year label
            year_canvas.create_text(
                x0 + bar_width / 2, start_y + 30,
                text=f"Year {year}",
                font=("Arial", 12, "bold")
            )

        # Group statistics tab
        group_frame = ttk.Frame(notebook)
        notebook.add(group_frame, text="Group Statistics")

        # Calculate wins by group
        group_wins = {}
        for char in self.characters:
            group = char["group"]
            if group not in group_wins:
                group_wins[group] = 0
            group_wins[group] += self.wins[char["name"]]

        # Create pie chart
        pie_canvas = tk.Canvas(group_frame, bg="white")
        pie_canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Draw pie chart
        total_wins = sum(group_wins.values()) if group_wins else 1
        colors = ["#ff99cc", "#99ccff", "#99ff99", "#ffcc99", "#cc99ff"]

        start_angle = 0
        center_x, center_y = 300, 250
        radius = 200

        # Draw pie slices - FIXED 100% SLICE ISSUE
        for i, (group, wins) in enumerate(group_wins.items()):
                    # Calculate angle for this slice
                    angle = 360 * wins / total_wins

                    # Handle full circle case (100% slice)
                    if angle == 360:
                        # Draw full circle instead of arc
                        pie_canvas.create_oval(
                            center_x - radius, center_y - radius,
                            center_x + radius, center_y + radius,
                            fill=colors[i % len(colors)], outline="black"
                        )
                        label_x = center_x
                        label_y = center_y
                    else:
                        # Draw pie slice
                        pie_canvas.create_arc(
                            center_x - radius, center_y - radius,
                            center_x + radius, center_y + radius,
                            start=start_angle, extent=angle,
                            fill=colors[i % len(colors)], outline="black"
                        )
                        # Calculate label position
                        mid_angle = start_angle + angle / 2
                        label_x = center_x + radius * 0.7 * math.cos(math.radians(mid_angle))
                        label_y = center_y - radius * 0.7 * math.sin(math.radians(mid_angle))

                    # Draw group label
                    pie_canvas.create_text(
                        label_x, label_y,
                        text=f"{group}\n({wins} wins)",
                        font=("Arial", 10, "bold"),
                        justify=tk.CENTER
                    )

                    # Update start angle for next slice
                    start_angle += angle

        # Draw title
        pie_canvas.create_text(
            center_x, center_y - radius - 20,
            text="Wins by Group",
            font=("Arial", 14, "bold")
        )

        # Blood Type Statistics Tab - MODIFIED TO IGNORE '-' VALUES
        blood_frame = ttk.Frame(notebook)
        notebook.add(blood_frame, text="Blood Type")

        # Calculate wins by blood type - filter out '-' values
        blood_wins = {}
        for char in self.characters:
            bt = char["blood_type"]
            if bt == '-':  # Skip unknown blood types
                continue
            if bt not in blood_wins:
                blood_wins[bt] = 0
            blood_wins[bt] += self.wins[char["name"]]

        if not blood_wins:  # Handle case where no valid blood types
            no_data_label = ttk.Label(
                blood_frame,
                text="No blood type data available for selected characters",
                font=("Arial", 12)
            )
            no_data_label.pack(expand=True, padx=20, pady=20)
        else:
            # Create pie chart
            blood_canvas = tk.Canvas(blood_frame, bg="white")
            blood_canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            # Draw pie chart
            total_wins = sum(blood_wins.values()) if blood_wins else 1
            colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]

            start_angle = 0
            center_x, center_y = 300, 250
            radius = 200

            # Draw pie slices - FIXED 100% SLICE ISSUE
            for i, (bt, wins) in enumerate(blood_wins.items()):
                        # Calculate angle for this slice
                        angle = 360 * wins / total_wins

                        # Handle full circle case (100% slice)
                        if angle == 360:
                            # Draw full circle instead of arc
                            blood_canvas.create_oval(
                                center_x - radius, center_y - radius,
                                center_x + radius, center_y + radius,
                                fill=colors[i % len(colors)], outline="black"
                            )
                            label_x = center_x
                            label_y = center_y
                        else:
                            # Draw pie slice
                            blood_canvas.create_arc(
                                center_x - radius, center_y - radius,
                                center_x + radius, center_y + radius,
                                start=start_angle, extent=angle,
                                fill=colors[i % len(colors)], outline="black"
                            )
                            # Calculate label position
                            mid_angle = start_angle + angle / 2
                            label_x = center_x + radius * 0.7 * math.cos(math.radians(mid_angle))
                            label_y = center_y - radius * 0.7 * math.sin(math.radians(mid_angle))

                        # Draw blood type label
                        blood_canvas.create_text(
                            label_x, label_y,
                            text=f"Type {bt}\n({wins} wins)",
                            font=("Arial", 10, "bold"),
                            justify=tk.CENTER
                        )

                        # Update start angle for next slice
                        start_angle += angle

            # Draw title
            blood_canvas.create_text(
                center_x, center_y - radius - 20,
                text="Wins by Blood Type",
                font=("Arial", 14, "bold")
            )

        # Height Analysis Tab with Improved Layout
        height_frame = ttk.Frame(notebook)
        notebook.add(height_frame, text="Height Analysis")

        # Filter out characters with invalid height (height must be >0)
        valid_height_chars = [char for char in self.characters if char["height"] > 0]

        if valid_height_chars:
            # Calculate height statistics
            overall_avg = sum(char["height"] for char in valid_height_chars) / len(valid_height_chars)
            user_total = 0
            user_count = 0

            for char in valid_height_chars:
                wins = self.wins[char["name"]]
                user_total += char["height"] * wins
                user_count += wins

            user_avg = user_total / user_count if user_count > 0 else 0

            # Determine preference
            diff = user_avg - overall_avg
            if abs(diff) < 0.5:
                preference = "You have no significant height preference."
            elif diff > 0:
                preference = "Your preferences lean toward taller characters."
            else:
                preference = "Your preferences lean toward shorter characters."

            # Create analysis frame
            analysis_frame = ttk.Frame(height_frame)
            analysis_frame.pack(fill=tk.X, padx=20, pady=10)

            # Display height statistics
            stats_text = (
                f"Overall Average Height: {overall_avg:.1f} cm\n"
                f"Your Preferred Average Height: {user_avg:.1f} cm\n\n"
                f"{preference}"
            )

            stats_label = ttk.Label(
                analysis_frame,
                text=stats_text,
                font=("Arial", 12),
                justify=tk.CENTER
            )
            stats_label.pack(pady=10)

            # Create container frame for canvas and scrollbar
            chart_container = ttk.Frame(height_frame)
            chart_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            # Create horizontal scrollbar
            hscrollbar = ttk.Scrollbar(chart_container, orient=tk.HORIZONTAL)
            hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

            # Create canvas with horizontal scrollbar
            height_canvas = tk.Canvas(
                chart_container,
                bg="white",
                xscrollcommand=hscrollbar.set,
                height=450  # Increased height for better spacing
            )
            height_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            hscrollbar.config(command=height_canvas.xview)

            # Calculate required canvas width
            bar_width = 60
            spacing = 30
            total_width = 100 + len(valid_height_chars) * (bar_width + spacing)

            # Set canvas scroll region
            height_canvas.config(scrollregion=(0, 0, total_width, 450))

            # Create inner frame for drawing
            inner_frame = tk.Frame(height_canvas)
            height_canvas.create_window((0, 0), window=inner_frame, anchor="nw")

            # Draw reference lines
            inner_frame.update_idletasks()
            inner_canvas = tk.Canvas(
                inner_frame,
                bg="white",
                width=total_width,
                height=450
            )
            inner_canvas.pack()

            # Draw base line and axes
            baseline_y = 350
            inner_canvas.create_line(50, baseline_y, total_width - 50, baseline_y, fill="black")  # X-axis
            inner_canvas.create_line(50, 50, 50, baseline_y, fill="black")  # Y-axis

            # Draw labels
            inner_canvas.create_text(25, 200, text="Wins", angle=90, font=("Arial", 10))
            inner_canvas.create_text(total_width/2, baseline_y + 40, text="Characters (sorted by height)", font=("Arial", 10))

            # Find maximum wins for scaling
            max_wins = max(self.wins.values()) if self.wins.values() else 1
            max_bar_height = 250
            scale_factor = max_bar_height / max_wins

            # Sort characters by height
            sorted_chars = sorted(valid_height_chars, key=lambda c: c["height"])

            # Draw bars for each character
            x_pos = 100
            for char in sorted_chars:
                wins = self.wins[char["name"]]
                bar_height = wins * scale_factor

                # Draw bar - fixed to start at baseline and extend upward
                inner_canvas.create_rectangle(
                    x_pos, baseline_y,
                    x_pos + bar_width, baseline_y - bar_height,
                    fill="#ff99cc", outline="black"
                )

                # Draw character name at bottom with padding
                inner_canvas.create_text(
                    x_pos + bar_width/2, baseline_y + 25,  # Increased padding below bars
                    text=char['name'],
                    font=("Arial", 9),
                    justify=tk.CENTER
                )

                # Draw height and win count inside bar
                # Position text at top third of bar for better visibility
                text_y = baseline_y - bar_height + 15 if bar_height > 30 else baseline_y - bar_height - 10

                # Draw height at top of bar
                inner_canvas.create_text(
                    x_pos + bar_width/2, baseline_y - bar_height - 15,  # Above bar
                    text=f"{char['height']} cm",
                    font=("Arial", 9),
                    fill="#333333"
                )

                # Draw win count inside bar (centered vertically)
                inner_canvas.create_text(
                    x_pos + bar_width/2, (baseline_y + (baseline_y - bar_height)) / 2,
                    text=f"{wins} wins",
                    font=("Arial", 9, "bold"),
                    fill="#000000"
                )

                x_pos += bar_width + spacing

            # Draw title
            inner_canvas.create_text(
                total_width/2, 20,
                text="Character Popularity by Height",
                font=("Arial", 14, "bold")
            )
        else:
            # Handle case where no valid height data
            no_data_label = ttk.Label(
                height_frame,
                text="No valid height data available for selected characters",
                font=("Arial", 12)
            )
            no_data_label.pack(expand=True, padx=20, pady=20)



if __name__ == "__main__":
    root = tk.Tk()
    app = LoveLiveTournament(root)
    root.mainloop()
