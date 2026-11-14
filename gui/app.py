
import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path

from data.units import UNIT_DATABASE
from core.engine import ConversionEngine


DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"
HISTORY_FILE = DATA_FOLDER / "conversion_history.json"
FAVOURITES_FILE = DATA_FOLDER / "favourites.json"

MAX_HISTORY = 100


class UniversalConverterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Convert")
        self.root.geometry("850x610")
        self.root.minsize(760, 560)
        self.root.configure(bg="#f0f0f0")

        # Application icon
        icon_path = (
            Path(__file__).resolve().parent.parent
            / "assets"
            / "icon.ico"
        )

        if icon_path.exists():
            try:
                self.root.iconbitmap(str(icon_path))
            except tk.TclError:
                pass

        self.engine = ConversionEngine()
        self.categories = list(UNIT_DATABASE.keys())
        self.category_buttons = {}

        self.history = self.load_json(HISTORY_FILE)
        self.favourites = self.load_json(FAVOURITES_FILE)

        self.create_menu()
        self.create_interface()
        self.select_category(self.categories[0])

    # --------------------------------------------------
    # DATA STORAGE
    # --------------------------------------------------

    def load_json(self, path):
        try:
            if path.exists():
                with path.open("r", encoding="utf-8") as file:
                    data = json.load(file)

                if isinstance(data, list):
                    return data

        except (OSError, json.JSONDecodeError):
            pass

        return []

    def save_json(self, path, data):
        try:
            DATA_FOLDER.mkdir(parents=True, exist_ok=True)

            with path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save data:\n{error}"
            )

    # --------------------------------------------------
    # MENU BAR
    # --------------------------------------------------

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        options_menu = tk.Menu(menu_bar, tearoff=0)
        options_menu.add_command(
            label="Settings",
            command=lambda: messagebox.showinfo(
                "Options",
                "Settings will be added later."
            )
        )

        history_menu = tk.Menu(menu_bar, tearoff=0)
        history_menu.add_command(
            label="View History",
            command=self.show_history
        )
        history_menu.add_command(
            label="Clear History",
            command=self.clear_history
        )

        favourites_menu = tk.Menu(menu_bar, tearoff=0)
        favourites_menu.add_command(
            label="Add Current Conversion",
            command=self.add_favourite
        )
        favourites_menu.add_command(
            label="View Favourites",
            command=self.show_favourites
        )

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(
            label="About",
            command=lambda: messagebox.showinfo(
                "About Convert",
                "Universal Converter\n"
                "Engineering Edition\n"
                "Version 1.0.0"
            )
        )

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Options", menu=options_menu)
        menu_bar.add_cascade(label="History", menu=history_menu)
        menu_bar.add_cascade(label="Favourites", menu=favourites_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    # --------------------------------------------------
    # MAIN INTERFACE
    # --------------------------------------------------

    def create_interface(self):
        main = tk.Frame(self.root, bg="#f0f0f0")
        main.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=8
        )

        # Category buttons
        self.category_frame = tk.Frame(
            main,
            bg="#f0f0f0"
        )
        self.category_frame.pack(
            fill="x",
            pady=(0, 10)
        )

        for column in range(7):
            self.category_frame.grid_columnconfigure(
                column,
                weight=1
            )

        for index, category in enumerate(self.categories):
            row = index // 7
            column = index % 7

            button = tk.Button(
                self.category_frame,
                text=category,
                font=("Arial", 8),
                relief="raised",
                borderwidth=1,
                bg="#e8e8e8",
                activebackground="#dcdcdc",
                wraplength=100,
                height=2,
                command=lambda name=category:
                    self.select_category(name)
            )

            button.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=1,
                pady=1
            )

            self.category_buttons[category] = button

        # Unit selection area
        selection_area = tk.Frame(
            main,
            bg="#f0f0f0",
            relief="groove",
            borderwidth=2
        )
        selection_area.pack(
            fill="both",
            expand=True
        )

        selection_area.grid_columnconfigure(0, weight=1)
        selection_area.grid_columnconfigure(1, weight=0)
        selection_area.grid_columnconfigure(2, weight=1)
        selection_area.grid_rowconfigure(0, weight=1)

        # Input unit list
        input_frame = tk.LabelFrame(
            selection_area,
            text="Input",
            bg="#f0f0f0",
            font=("Arial", 9)
        )
        input_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(8, 3),
            pady=8
        )

        self.input_list = tk.Listbox(
            input_frame,
            font=("Arial", 9),
            selectmode=tk.SINGLE,
            exportselection=False,
            activestyle="none"
        )
        self.input_list.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(3, 0),
            pady=3
        )

        input_scroll = tk.Scrollbar(
            input_frame,
            orient="vertical",
            command=self.input_list.yview
        )
        input_scroll.pack(
            side="right",
            fill="y",
            pady=3
        )

        self.input_list.config(
            yscrollcommand=input_scroll.set
        )

        # Direction indicator and swap button
        direction_frame = tk.Frame(
            selection_area,
            bg="#f0f0f0",
            width=65
        )
        direction_frame.grid(
            row=0,
            column=1,
            sticky="ns"
        )
        direction_frame.grid_propagate(False)

        tk.Label(
            direction_frame,
            text="☞",
            font=("Segoe UI Symbol", 23),
            bg="#f0f0f0"
        ).place(
            relx=0.5,
            rely=0.42,
            anchor="center"
        )

        self.swap_button = tk.Button(
            direction_frame,
            text="⇄ Swap",
            font=("Arial", 8),
            relief="raised",
            borderwidth=1,
            bg="#e8e8e8",
            command=self.swap_units
        )
        self.swap_button.place(
            relx=0.5,
            rely=0.57,
            anchor="center"
        )

        # Output unit list
        output_frame = tk.LabelFrame(
            selection_area,
            text="Output",
            bg="#f0f0f0",
            font=("Arial", 9)
        )
        output_frame.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(3, 8),
            pady=8
        )

        self.output_list = tk.Listbox(
            output_frame,
            font=("Arial", 9),
            selectmode=tk.SINGLE,
            exportselection=False,
            activestyle="none"
        )
        self.output_list.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(3, 0),
            pady=3
        )

        output_scroll = tk.Scrollbar(
            output_frame,
            orient="vertical",
            command=self.output_list.yview
        )
        output_scroll.pack(
            side="right",
            fill="y",
            pady=3
        )

        self.output_list.config(
            yscrollcommand=output_scroll.set
        )

        # Bottom conversion fields
        bottom = tk.Frame(
            main,
            bg="#f0f0f0"
        )
        bottom.pack(
            fill="x",
            pady=(10, 0)
        )

        bottom.grid_columnconfigure(1, weight=1)

        tk.Label(
            bottom,
            text="Input:",
            font=("Arial", 9),
            bg="#f0f0f0"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=3,
            pady=4
        )

        self.input_value = tk.Entry(
            bottom,
            font=("Arial", 10),
            relief="sunken",
            borderwidth=1
        )
        self.input_value.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=4
        )
        self.input_value.insert(0, "1")

        self.input_unit_label = tk.Label(
            bottom,
            text="",
            font=("Arial", 9),
            bg="#f0f0f0",
            anchor="w",
            width=20
        )
        self.input_unit_label.grid(
            row=0,
            column=2,
            sticky="w",
            padx=8
        )

        tk.Label(
            bottom,
            text="Output:",
            font=("Arial", 9),
            bg="#f0f0f0"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=3,
            pady=4
        )

        self.output_value = tk.Entry(
            bottom,
            font=("Arial", 10),
            relief="sunken",
            borderwidth=1,
            state="readonly"
        )
        self.output_value.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=4
        )

        self.output_unit_label = tk.Label(
            bottom,
            text="",
            font=("Arial", 9),
            bg="#f0f0f0",
            anchor="w",
            width=20
        )
        self.output_unit_label.grid(
            row=1,
            column=2,
            sticky="w",
            padx=8
        )

        # Event bindings
        self.input_list.bind(
            "<<ListboxSelect>>",
            self.update_unit_labels
        )
        self.output_list.bind(
            "<<ListboxSelect>>",
            self.update_unit_labels
        )
        self.input_value.bind(
            "<KeyRelease>",
            self.perform_conversion
        )

    # --------------------------------------------------
    # CATEGORY AND UNIT SELECTION
    # --------------------------------------------------

    def select_category(self, category):
        self.selected_category = category

        for name, button in self.category_buttons.items():
            if name == category:
                button.config(
                    relief="sunken",
                    bg="#d0d0d0"
                )
            else:
                button.config(
                    relief="raised",
                    bg="#e8e8e8"
                )

        units = list(UNIT_DATABASE[category].keys())

        self.input_list.delete(0, tk.END)
        self.output_list.delete(0, tk.END)

        for unit in units:
            self.input_list.insert(tk.END, unit)
            self.output_list.insert(tk.END, unit)

        if units:
            self.input_list.selection_set(0)
            self.output_list.selection_set(
                1 if len(units) > 1 else 0
            )

        self.update_unit_labels()

    def swap_units(self):
        input_selection = self.input_list.curselection()
        output_selection = self.output_list.curselection()

        if not input_selection or not output_selection:
            return

        input_index = input_selection[0]
        output_index = output_selection[0]

        self.input_list.selection_clear(0, tk.END)
        self.output_list.selection_clear(0, tk.END)

        self.input_list.selection_set(output_index)
        self.output_list.selection_set(input_index)

        self.update_unit_labels()

    def update_unit_labels(self, event=None):
        input_selection = self.input_list.curselection()
        output_selection = self.output_list.curselection()

        if input_selection:
            unit = self.input_list.get(input_selection[0])
            self.input_unit_label.config(text=unit)

        if output_selection:
            unit = self.output_list.get(output_selection[0])
            self.output_unit_label.config(text=unit)

        self.perform_conversion()

    # --------------------------------------------------
    # CONVERSION ENGINE CONNECTION
    # --------------------------------------------------

    def format_result(self, result):
        if result == 0:
            return "0"

        result = result.normalize()

        if abs(result) >= 1e12 or abs(result) < 1e-9:
            return format(result, ".15E")

        return format(result, "f")

    def perform_conversion(self, event=None):
        input_selection = self.input_list.curselection()
        output_selection = self.output_list.curselection()

        if not input_selection or not output_selection:
            self.set_output("")
            return

        value = self.input_value.get().strip()

        if not value:
            self.set_output("")
            return

        from_unit = self.input_list.get(input_selection[0])
        to_unit = self.output_list.get(output_selection[0])

        try:
            result = self.engine.convert(
                value,
                self.selected_category,
                from_unit,
                to_unit
            )

            self.set_output(self.format_result(result))

            self.add_to_history(
                value,
                from_unit,
                to_unit,
                result
            )

        except (ValueError, ArithmeticError):
            self.set_output("")

    def set_output(self, value):
        self.output_value.config(state="normal")
        self.output_value.delete(0, tk.END)
        self.output_value.insert(0, value)
        self.output_value.config(state="readonly")

    # --------------------------------------------------
    # CONVERSION HISTORY
    # --------------------------------------------------

    def add_to_history(self, value, from_unit, to_unit, result):
        entry = {
            "category": self.selected_category,
            "input": str(value),
            "from_unit": from_unit,
            "output": self.format_result(result),
            "to_unit": to_unit
        }

        if (
            self.history
            and self.history[0].get("category") == entry["category"]
            and self.history[0].get("from_unit") == from_unit
            and self.history[0].get("to_unit") == to_unit
        ):
            self.history[0] = entry
        else:
            self.history.insert(0, entry)

        self.history = self.history[:MAX_HISTORY]
        self.save_json(HISTORY_FILE, self.history)

    def show_history(self):
        window = tk.Toplevel(self.root)
        window.title("Conversion History")
        window.geometry("700x400")
        window.minsize(500, 300)
        window.configure(bg="#f0f0f0")

        tk.Label(
            window,
            text="Previous Conversions",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        list_frame = tk.Frame(
            window,
            bg="#f0f0f0"
        )
        list_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        history_list = tk.Listbox(
            list_frame,
            font=("Consolas", 9),
            activestyle="none"
        )
        history_list.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            list_frame,
            orient="vertical",
            command=history_list.yview
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        history_list.config(
            yscrollcommand=scrollbar.set
        )

        if not self.history:
            history_list.insert(
                tk.END,
                "No conversion history yet."
            )
        else:
            for entry in self.history:
                line = (
                    f"{entry.get('input', '')} "
                    f"{entry.get('from_unit', '')} = "
                    f"{entry.get('output', '')} "
                    f"{entry.get('to_unit', '')} "
                    f"[{entry.get('category', '')}]"
                )
                history_list.insert(tk.END, line)

        tk.Button(
            window,
            text="Close",
            font=("Arial", 9),
            command=window.destroy
        ).pack(
            side="right",
            padx=10,
            pady=10
        )

    def clear_history(self):
        if not self.history:
            messagebox.showinfo(
                "History",
                "There is no conversion history to clear."
            )
            return

        confirm = messagebox.askyesno(
            "Clear History",
            "Are you sure you want to delete all conversion history?"
        )

        if confirm:
            self.history.clear()
            self.save_json(HISTORY_FILE, self.history)

            messagebox.showinfo(
                "History",
                "Conversion history cleared."
            )

    # --------------------------------------------------
    # FAVOURITES
    # --------------------------------------------------

    def add_favourite(self):
        input_selection = self.input_list.curselection()
        output_selection = self.output_list.curselection()

        if not input_selection or not output_selection:
            messagebox.showwarning(
                "Favourites",
                "Select both input and output units first."
            )
            return

        from_unit = self.input_list.get(input_selection[0])
        to_unit = self.output_list.get(output_selection[0])

        favourite = {
            "category": self.selected_category,
            "from_unit": from_unit,
            "to_unit": to_unit
        }

        if favourite in self.favourites:
            messagebox.showinfo(
                "Favourites",
                "This conversion is already in your favourites."
            )
            return

        self.favourites.append(favourite)
        self.save_json(FAVOURITES_FILE, self.favourites)

        messagebox.showinfo(
            "Favourites",
            f"Saved {from_unit} to {to_unit}."
        )

    def show_favourites(self):
        window = tk.Toplevel(self.root)
        window.title("Favourite Conversions")
        window.geometry("600x350")
        window.minsize(450, 250)
        window.configure(bg="#f0f0f0")

        tk.Label(
            window,
            text="Your Favourite Conversions",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        list_frame = tk.Frame(
            window,
            bg="#f0f0f0"
        )
        list_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        favourite_list = tk.Listbox(
            list_frame,
            font=("Arial", 9),
            activestyle="none",
            exportselection=False
        )
        favourite_list.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            list_frame,
            orient="vertical",
            command=favourite_list.yview
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        favourite_list.config(
            yscrollcommand=scrollbar.set
        )

        def refresh_list():
            favourite_list.delete(0, tk.END)

            for favourite in self.favourites:
                line = (
                    f"{favourite['category']}: "
                    f"{favourite['from_unit']} → "
                    f"{favourite['to_unit']}"
                )
                favourite_list.insert(tk.END, line)

            if not self.favourites:
                favourite_list.insert(
                    tk.END,
                    "No favourites saved."
                )

        def apply_selected():
            selection = favourite_list.curselection()

            if not selection or not self.favourites:
                return

            favourite = self.favourites[selection[0]]
            window.destroy()
            self.apply_favourite(favourite)

        def remove_selected():
            selection = favourite_list.curselection()

            if not selection or not self.favourites:
                return

            index = selection[0]
            del self.favourites[index]

            self.save_json(FAVOURITES_FILE, self.favourites)
            refresh_list()

        refresh_list()

        button_frame = tk.Frame(
            window,
            bg="#f0f0f0"
        )
        button_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        tk.Button(
            button_frame,
            text="Apply",
            width=10,
            command=apply_selected
        ).pack(
            side="left",
            padx=(0, 5)
        )

        tk.Button(
            button_frame,
            text="Remove",
            width=10,
            command=remove_selected
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_frame,
            text="Close",
            width=10,
            command=window.destroy
        ).pack(side="right")

        favourite_list.bind(
            "<Double-Button-1>",
            lambda event: apply_selected()
        )

    def apply_favourite(self, favourite):
        category = favourite.get("category")
        from_unit = favourite.get("from_unit")
        to_unit = favourite.get("to_unit")

        if category not in UNIT_DATABASE:
            messagebox.showerror(
                "Favourites",
                "This favourite uses an unknown category."
            )
            return

        units = list(UNIT_DATABASE[category].keys())

        if from_unit not in units or to_unit not in units:
            messagebox.showerror(
                "Favourites",
                "One or more saved units are no longer available."
            )
            return

        self.select_category(category)

        input_index = units.index(from_unit)
        output_index = units.index(to_unit)

        self.input_list.selection_clear(0, tk.END)
        self.output_list.selection_clear(0, tk.END)

        self.input_list.selection_set(input_index)
        self.output_list.selection_set(output_index)

        self.update_unit_labels()


def main():
    root = tk.Tk()
    UniversalConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
