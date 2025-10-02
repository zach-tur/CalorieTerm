import os

# import rich
import sys
import datetime

from datetime import date
from enum import Enum
# from rich import print

from rich.console import Console
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table
from rich.text import Text


args = sys.argv
print(args)

todays_date = date.today().strftime("%-m/%-d/%Y")

goal_fat = 0
goal_carbs = 0
goal_protein = 0
goal_fiber = 0


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


# TODO change this to work for any date including today
def table_today():
    console = Console()

    table = Table(
        title="Log",
        box=None,
        width=91,
        title_style="bold italic white",
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
#   calterm add
#       input item name, weight
#   if item banana doesn't exist in food library, prompt for:
#       item "banana" doesn't exist in library; add new item into library?
#       on no, terminate, on yes prompt for:
#           item name (prefill with banana), weight, fat, carbs, protein, fiber
#           add to library
#           prompt again confirming daily entry for previous args entered for "banana"
# - args to edit existing entry
#   calterm edit today 1 40g
#   calterm edit 20250815 5 40g
#   can use either today or date, followed by line # and new amount
#
# - args to check specific day
#   calterm check 20250815 (iso-date)


# TODO remove date arg from command line, prompt for date instead when check is used
def log_check():
    console = Console()
    console.print(f"Checking log...", style="red italic", justify="center")
    return


def log_add():
    console = Console()
    console.print(f"Adding new entry to log...", style="red italic", justify="center")
    # TODO edit to use month and day only (e.g. 910 for sep 10), which defaults to current year.
    # can view previous year by just typing in the year (e.g. 91024 for sep 10 2024)
    try:
        input_date = (
            console.input(
                Text.assemble(
                    "Use todays date ",
                    (f"{todays_date}", "italic blue"),
                    " (press enter) or input date: ",
                    style="bold",
                )
            )
            or todays_date
        )

        while True:
            item_inputs = console.input(
                Text(
                    f"Enter item name, weight, fat, carbs, protein, and fiber (e.g. banana 105 0 27 1 3):\n--> ",
                    style="bold",
                )
            )
            input_list = item_inputs.split()

            if len(input_list) != 6:
                console.print(
                    f"Invalid input:\n{input_list}\nTry again", style="italic red"
                )
                continue

            is_valid_input = True
            for input in input_list[1:]:
                try:
                    input_int = int(input)
                    continue
                except ValueError:
                    is_valid_input = False
                    console.print(
                        f"Inputs are not integers:\n{input_list}\nTry again",
                        style="italic red",
                    )
                    break

            if is_valid_input == True:
                break

        console.print(
            f"Added item to log for {input_date}:\n",
            f"{input_list[0]} {input_list[1]}g:",
            f"Fat {input_list[1]}g, ",
            f"Carbs {input_list[2]}g, ",
            f"Protein {input_list[3]}g, ",
            f"Fiber {input_list[4]}g",
        )
    except Exception as e:
        console.print(f"Error: {e}")


def log_edit():
    console = Console()
    console.print(f"Editing entry in log...", style="red italic", justify="center")
    return


def library_add():
    console = Console()
    console.print(
        f"Adding new entry to library...", style="red italic", justify="center"
    )
    return


def library_edit():
    console = Console()
    console.print(f"Editiing entry in library...", style="red italic", justify="center")
    return


def date_output():
    console = Console()
    try:
        if args[1] == "check":
            entered_date = date.fromisoformat(args[2]).strftime("%-m/%-d/%Y")
            console.print(
                f"Prior - {entered_date}",
                style="bold italic red",
                justify="center",
                highlight=False,
            )

        else:
            console.print(
                f"Today - {todays_date}",
                style="italic",
                justify="center",
                highlight=False,
            )

    except Exception as e:
        console.print(f"Error: {e}")


def main(args):
    console = Console()
    console.print(
        "\nCalorieTerm",
        justify="center",
        style="bold white",
    )

    try:
        match args[1]:
            case "check":
                log_check()
                return
            case "add":
                match args[2]:
                    case "log":
                        log_add()
                    case "lib":
                        library_add()
            case "edit":
                match args[2]:
                    case "log":
                        log_edit()
                        return
                    case "library":
                        library_edit()
                        return
                    case _:
                        return
            case _:
                print("case _:")
                return

        date_output()  # need to fix how this is handled, currently not printing due to args
        print()
        summary_print()
        print()
        table_today()
        print()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main(args)
