import tkinter as tk


class PomoApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.bg = "#ff7575"
        self.root.configure(bg=self.bg)
        self.root.geometry("750x750")
        self.root.title("Pomodoro")
        self.timer_text = tk.StringVar(value="25:00")

    def set_window(self):
        """
        Controls the styling of the main window. Controls the window background color, and timer number.
        """

        formatting = {
            "bg": self.bg,
            "fg": "#fff",
            "borderwidth": 0,
            "font": ("Helvetica", 20),
        }

        # setting buttons and time label
        self.pomodoro = tk.Button(
            self.root,
            text="Pomodoro",
            command=lambda: self.reset_window("#ff7575", "25:00"),
            **formatting
        )
        self.short_break = tk.Button(
            self.root,
            text="Short Break",
            command=lambda: self.reset_window("#c261ff", "05:00"),
            **formatting
        )
        self.long_break = tk.Button(
            self.root,
            text="Long Break",
            command=lambda: self.reset_window("#2ba0ff", "30:00"),
            **formatting
        )

        self.timer = tk.Label(
            self.root,
            textvariable=self.timer_text,
            fg="#fff",
            bg=self.bg,
            font=("Helvetica", 100),
        )

    def set_grid(self):
        """
        Creates the window grid, and assigns the apps buttons and label to their respective positions
        """

        tk.Tk.grid_rowconfigure(self.root, index=0, weight=1)
        tk.Tk.grid_rowconfigure(self.root, index=1, weight=1)
        tk.Tk.grid_rowconfigure(self.root, index=2, weight=1)

        tk.Tk.grid_columnconfigure(self.root, index=0, weight=1)
        tk.Tk.grid_columnconfigure(self.root, index=1, weight=1)
        tk.Tk.grid_columnconfigure(self.root, index=2, weight=1)

        self.pomodoro.grid(row=0, column=0)
        self.short_break.grid(row=0, column=1)
        self.long_break.grid(row=0, column=2)
        self.timer.grid(row=1, column=1)

    def reset_window(self, color: str, time: str):
        """
        In charge of resetting the window when buttons are pressed. Changes the background color and the time of timer label.

        Parameters
        ----------
        color : str
            hex value of a color to reset the window background to
        time : str
            time value to reset the timer label to
        """
        self.bg = color
        self.timer_text = tk.StringVar(value=time)
        self.set_window()
        self.set_grid()
        self.root.configure(bg=color)

    def __call__(self):
        self.set_window()
        self.set_grid()
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PomoApp(root)
    app()
