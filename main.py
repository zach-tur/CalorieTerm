import os
import rich

from rich import print
from rich.console import Console
from rich.table import Table


def summary_print():
    console = Console()

    fiber_label = console.print(
        "Fiber",
        justify="right",
        style="bold tan",
    )

    fat_label = console.print(
        "Fat",
        justify="right",
        style="bold yellow",
    )

    carbs_label = console.print(
        "Carbs",
        justify="right",
        style="bold green",
    )

    protein_label = console.print(
        "Protein",
        justify="right",
        style="bold red",
    )

    fiber_bar = "|=========>----------|"
    fat_bar = "|=========>----------|"
    carbs_bar = "|=========>----------|"
    protein_bar = "|=========>----------|"

    fiber_stats = "50%, 5g"
    fat_stats = "100%, 35g"
    carbs_stats = "35%, 55g"
    protein_stats = "5%, 85g"

    fiber_summ = fiber_bar

    console.print()
    return


def table_today():
    console = Console()

    table = Table(title="Today's log", width=91)
    table.add_column("Description", min_width=20, justify="center", style="bold")
    table.add_column("Amount", min_width=8, justify="center", style="bold")
    table.add_column("Fiber", min_width=8, justify="center", style="bold tan")
    table.add_column("Fat", min_width=12, justify="center", style="bold yellow")
    table.add_column("Carbs", min_width=12, justify="center", style="bold green")
    table.add_column("Protein", min_width=12, justify="center", style="bold red")

    table.add_row("banana", "79g", "5g", "0g / 0cal", "20g / 60cal", "0g / 0cal")
    console.print(table)


def main():
    console = Console(width=91)
    console.print(
        "\nCalorieTerm",
        justify="center",
        style="bold red3",
    )
    summary_print()
    table_today()


if __name__ == "__main__":
    main()
