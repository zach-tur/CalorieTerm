import os
import rich

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table
from rich.text import Text


def summary_print():
    console = Console()

    fiber_label = Text("Fiber", justify="right")
    fat_label = Text("Fat", justify="right")
    carbs_label = Text("Carbs", justify="right")
    protein_label = Text("Protein", justify="right")

    fiber_bar = ProgressBar(total=100, completed=110, complete_style="tan")
    fat_bar = ProgressBar(total=100, completed=50, complete_style="yellow")
    carbs_bar = ProgressBar(total=100, completed=50, complete_style="green")
    protein_bar = ProgressBar(total=100, completed=50, complete_style="red")

    fiber_stats = Text("105g / 25g", justify="center")
    fat_stats = Text("10g / 30g", justify="center")
    carbs_stats = Text("50g / 105g", justify="center")
    protein_stats = Text("25g / 150g", justify="center")

    table = Table(show_header=False, box=None)
    table.add_column("labels", width=7)
    table.add_column("bars", width=24)
    table.add_column("stats", width=10)

    table.add_row(fiber_label, fiber_bar, fiber_stats, style="bold tan")
    table.add_row(fat_label, fat_bar, fat_stats, style="bold yellow")
    table.add_row(carbs_label, carbs_bar, carbs_stats, style="bold green")
    table.add_row(protein_label, protein_bar, protein_stats, style="bold red3")

    console.print(table, justify="center")
    return


def table_today():
    console = Console()

    table = Table(
        title="Today's log", box=None, width=91, title_style="bold italic white"
    )
    table.add_column("Description", min_width=20, justify="center", header_style="bold")
    table.add_column("Amount", min_width=8, justify="center", header_style="bold")
    table.add_column(
        "Fiber",
        min_width=8,
        justify="center",
        style="tan",
        header_style="bold tan",
    )
    table.add_column(
        "Fat",
        min_width=12,
        justify="center",
        style="yellow",
        header_style="bold yellow",
    )
    table.add_column(
        "Carbs",
        min_width=12,
        justify="center",
        style="green",
        header_style="bold green",
    )
    table.add_column(
        "Protein",
        min_width=12,
        justify="center",
        style="red3",
        header_style="bold red3",
    )

    table.add_row("banana", "79g", "5g", "0g / 0cal", "20g / 60cal", "0g / 0cal")
    console.print(table, justify="center")


# for entry functions:
# - args to input new daily item:
#   calterm add banana 50g
#   if item banana doesn't exist in food library, prompt for:
#       item "banana" doesn't exist in library; add new item into library?
#       on no, terminate, on yes prompt for:
#           item name (prefill with banana), weight, fat, carbs, protein, fiber
#           add to library
#           prompt again confirming daily entry for previous args entered for "banana"
# - args to check specific day
#   calterm check 20250815 (iso-date)


def main():
    console = Console()
    console.print(
        "\nCalorieTerm",
        justify="center",
        style="bold white",
    )
    print()
    summary_print()
    print()
    table_today()


if __name__ == "__main__":
    main()
