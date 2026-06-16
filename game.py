import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 680)

class GuessKingGiftGame(App):
    def build(self):
        self.level = 1
        self.total_levels = 400
        self.max_range = self.level * 10
        self.jackpot = random.randint(1, self.max_range)
        self.chances = 3 + (self.level // 50)
        self.current_chance = 1

        self.gifts_pool = [
            "🧠 Einstein's Brain Crystal", "🍎 Newton's Gravity Apple", 
            "🔭 Galileo's Cosmic Telescope", "💡 Edison's First Bulb", 
            "🧭 Columbus's Golden Compass", "📐 Pythagoras's Secret Scale",
            "🚀 Space Explorer Badge", "💎 Logic Diamond", "⚔️ Mind Warrior Shield"
        ]

        Window.clearcolor = (0.95, 0.97, 1, 1)
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        # Kivy mein add_widget use hota hai
        self.title_label = Label(text="👑 GUESS KING 👑\n[BRAIN BOOSTER]", font_size='26sp', color=(0.1, 0.3, 0.6, 1), bold=True, halign='center')
        self.layout.add_widget(self.title_label)

        self.iq_label = Label(text="⚡ MIND RANK: NOVICE BRAIN 🧠", font_size='15sp', color=(0.2, 0.6, 0.2, 1), bold=True)
        self.layout.add_widget(self.iq_label)

        self.gift_label = Label(text="🏆 Inventory: 0 Gifts Unlocked", font_size='14sp', color=(0.7, 0.4, 0, 1), bold=True)
        self.layout.add_widget(self.gift_label)

        self.status_label = Label(
            text=f"Level: {self.level}/{self.total_levels}\nMath Range: 1 to {self.max_range}\nRemaining Attempts: {self.chances}",
            font_size='16sp', color=(0.2, 0.2, 0.3, 1), halign='center'
        )
        self.layout.add_widget(self.status_label)

        self.hint_label = Label(text="Analyze the range and guess the number!", font_size='16sp', color=(0.4, 0.4, 0.5, 1), italic=True)
        self.layout.add_widget(self.hint_label)

        self.user_input = TextInput(text='', multiline=False, input_filter='int', font_size='28sp', size_hint=(1, 0.25))
        self.layout.add_widget(self.user_input)

        self.btn = Button(text="SUBMIT ANSWER 🎯", font_size='20sp', bold=True, background_color=(0.15, 0.45, 0.85, 1))
        self.btn.bind(on_press=self.check_guess)
        self.layout.add_widget(self.btn)

        return self.layout

    def update_mind_rank(self):
        if self.level <= 10: return "⚡ MIND RANK: NOVICE BRAIN 🧠"
        elif self.level <= 30: return "🔥 MIND RANK: SHARP MIND 🔎"
        elif self.level <= 100: return "🎓 MIND RANK: MATH SCHOLAR 📝"
        else: return "👑 MIND RANK: EINSTEIN GENIUS 🚀"

    def get_math_hint(self, guess):
        hints = ["Think BIGGER number! 📈" if guess < self.jackpot else "Think SMALLER number! 📉"]
        hints.append("Hint: It's an EVEN number! 🔢" if self.jackpot % 2 == 0 else "Hint: It's an ODD number! 🔢")
        return random.choice(hints)

    def check_guess(self, instance):
        if not self.user_input.text: return
        
        guess = int(self.user_input.text)
        self.user_input.text = '' 

        if guess == self.jackpot:
            reward = random.choice(self.gifts_pool)
            self.gift_label.text = f"🎁 UNLOCKED: {reward}!"
            self.hint_label.text = f"🎉 Brilliant! Level {self.level} Solved! 🎉"
            
            self.level += 1
            if self.level > self.total_levels:
                self.hint_label.text = "🏆 ULTIMATE GUESS KING GENIUS! 🏆"
                self.btn.disabled = True
                return
            
            self.max_range = self.level * 10
            self.jackpot = random.randint(1, self.max_range)
            self.chances = 3 + (self.level // 50)
            self.current_chance = 1
        else:
            self.hint_label.text = self.get_math_hint(guess)
            self.current_chance += 1
            
            if self.current_chance > self.chances:
                self.hint_label.text = f"💥 Game Over! Correct number was: {self.jackpot}"
                self.btn.disabled = True

        self.iq_label.text = self.update_mind_rank()
        if self.current_chance <= self.chances:
            self.status_label.text = f"Level: {self.level}/{self.total_levels}\nMath Range: 1 to {self.max_range}\nRemaining Attempts: {self.chances - self.current_chance + 1}"

if __name__ == '__main__':
    GuessKingGiftGame().run()