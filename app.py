"""Minimal Tkinter front-end for the calculator."""

from __future__ import annotations

from functools import partial
import tkinter as tk
from tkinter import ttk

from calculator import Calculator


class CalculatorApp:
    """Render a simple UI that wires buttons to calculator operations."""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.calculator = Calculator()

        self.master.title("Simple Calculator")
        self.master.resizable(False, False)

        self._build_ui()

    def _build_ui(self) -> None:
        padding = {"padx": 10, "pady": 5}

        ttk.Label(self.master, text="First number").grid(row=0, column=0, **padding)
        self.entry_left = ttk.Entry(self.master, width=20)
        self.entry_left.grid(row=0, column=1, **padding)
        self.entry_left.bind(
            "<FocusIn>", lambda _event: self._set_active_entry(self.entry_left)
        )

        ttk.Label(self.master, text="Second number").grid(row=1, column=0, **padding)
        self.entry_right = ttk.Entry(self.master, width=20)
        self.entry_right.grid(row=1, column=1, **padding)
        self.entry_right.bind(
            "<FocusIn>", lambda _event: self._set_active_entry(self.entry_right)
        )

        self.active_entry = self.entry_left
        self.entry_left.focus()

        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=2, column=0, columnspan=2, **padding)

        keypad_frame = ttk.Frame(button_frame)
        keypad_frame.grid(row=0, column=0, sticky="nsew", padx=5)
        keypad_layout = [
            ("7", "8", "9"),
            ("4", "5", "6"),
            ("1", "2", "3"),
            (".", "0", "Clear"),
        ]

        for row_index, row_values in enumerate(keypad_layout):
            for col_index, label in enumerate(row_values):
                if label == "Clear":
                    command = self._clear_active_entry
                else:
                    command = partial(self._on_keypad_press, label)
                ttk.Button(
                    keypad_frame,
                    text=label,
                    command=command,
                    width=6,
                ).grid(row=row_index, column=col_index, sticky="nsew", padx=2, pady=2)

        for column in range(3):
            keypad_frame.grid_columnconfigure(column, weight=1)

        operations = [
            ("Add", self.calculator.add),
            ("Subtract", self.calculator.subtract),
            ("Multiply", self.calculator.multiply),
            ("Divide", self.calculator.divide),
        ]
        operations_frame = ttk.Frame(button_frame)
        operations_frame.grid(row=0, column=1, sticky="ns", padx=5)

        for idx, (label, operation) in enumerate(operations):
            ttk.Button(
                operations_frame,
                text=label,
                command=lambda op=operation, lbl=label: self._on_calculate(op, lbl),
                width=12,
            ).grid(row=idx, column=0, sticky="ew", pady=2)

        self.result_var = tk.StringVar(value="Result: ")
        ttk.Label(self.master, textvariable=self.result_var).grid(
            row=3, column=0, columnspan=2, **padding
        )

    def _on_calculate(self, operation, operation_name: str) -> None:
        try:
            left = self._parse_number(self.entry_left.get())
            right = self._parse_number(self.entry_right.get())
            result = operation(left, right)
        except ValueError as exc:
            self.result_var.set(f"Error: {exc}")
            return

        formatted = f"{result:.10g}"  # keeps it tidy without losing precision
        self.result_var.set(f"{operation_name}: {formatted}")

    def _on_keypad_press(self, value: str) -> None:
        self.active_entry.insert(tk.END, value)

    def _clear_active_entry(self) -> None:
        self.active_entry.delete(0, tk.END)

    def _set_active_entry(self, entry: ttk.Entry) -> None:
        self.active_entry = entry

    @staticmethod
    def _parse_number(raw: str) -> float:
        try:
            return float(raw)
        except ValueError as exc:
            raise ValueError("Enter a valid number.") from exc


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
