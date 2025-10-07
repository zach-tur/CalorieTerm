import json
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


console = Console()
args = sys.argv
print(args)

todays_date = date.today().strftime("%-m/%-d/%Y")
input_date = None

goal_fat = 0
goal_carbs = 0
goal_protein = 0
goal_fiber = 0


def load_log_entries(log_file_path, console_obj, target_date=None):
    entries = []
    try:
        with open(log_file_path, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        entry = json.loads(line)
                        if target_date is None or entry.get("date") == target_date:
                            entries.append(entry)
                    except json.JSONDecodeError:
                        console_obj.print(
                            f"Skipping malformed log entry: {line.strip()}",
                            style="italic yellow",
                        )
    except FileNotFoundError:
        console_obj.print(f"Log file '{log_file_path}' not found.", style="italic blue")
    except Exception as e:
        console_obj.print(
            f"Error reading log file '{log_file_path}': {e}", style="italic red"
        )
    return entries


def setup_log_files(base_log_dir="./logs"):
    console = Console()
    log_file_name = "full_log.log"
    goals_file_name = "current_goals.log"
    log_paths = {}

    try:
        os.makedirs(base_log_dir, exist_ok=True)
    except OSError as e:
        console.print(f"Error creating log directory: {e}", style="italic red")
        return None

    log_paths["food_log"] = os.path.join(base_log_dir, "food_log.txt")
    log_paths["current_goals"] = os.path.join(base_log_dir, "current_goals.txt")

    return log_paths


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
# Library currently not added, so these lines are for future additions:
#   if item banana doesn't exist in food library, prompt for:
#       item "banana" doesn't exist in library; add new item into library?
#       on no, terminate, on yes prompt for:
#           item name (prefill with banana), weight, fat, carbs, protein, fiber
#           add to library
#           prompt again confirming daily entry for previous args entered for "banana"
#
# - args to edit existing entry (need item # for each entry, listed in order of entry)
#       calterm edit date line_item edit_item edit_amount
#       calterm edit today 1 fat 5g
#       calterm edit 20250815 5 protein 16g
#


def date_input():
    global input_date
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
    return input_date


# TODO remove date arg from command line, prompt for date instead when check is used
def log_check(log_path):
    console.print(f"Checking log...", style="red italic", justify="center")
    return


def log_add(log_path):
    console = Console()

    console.print(f"Adding new entry to log...", style="red italic", justify="center")

    # TODO edit to use month and day only (e.g. 910 for sep 10), which defaults to current year.
    # can view previous year by just typing in the year (e.g. 91024 for sep 10 2024)
    try:
        global input_date
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
        input_integers = []
        # Input of item to add
        while True:
            item_inputs = console.input(
                Text(
                    f"Enter item name, weight, fat, carbs, protein, and fiber (e.g. banana 105 0 27 1 3):\n--> ",
                    style="bold",
                )
            )
            input_list = item_inputs.split()

            # Input validations
            if len(input_list) != 6:
                console.print(
                    f"Invalid input:\n{input_list}\nTry again", style="italic red"
                )
                continue

            is_valid_input = True
            for input in input_list[1:]:
                try:
                    input_int = int(input)
                    input_integers.append(input_int)
                    continue
                except ValueError:
                    is_valid_input = False
                    console.print(
                        f"Inputs are not integers:\n{input_list}\nTry again",
                        style="italic red",
                    )
                    break

            if is_valid_input == True:
                item_dict = {
                    "entry": 0,
                    "date": input_date,
                    "name": input_list[0],
                    "weight": input_integers[0],
                    "fat": input_integers[1],
                    "carbs": input_integers[2],
                    "protein": input_integers[3],
                    "fiber": input_integers[4],
                }

                # add item to log file here
                with open("log_path", "a") as f:
                    json_line = json.dumps(item_dict)
                    f.write(json_line + "\n")

                console.print(
                    Text.assemble(
                        (f"Added item to log for {item_dict['date']}:\n", "bold"),
                        (
                            f"{item_dict['name']} {item_dict['weight']}g:  ",
                            "blue bold italic",
                        ),
                        (f"Fat {item_dict['fat']}g  ", "yellow"),
                        (f"Carbs {item_dict['carbs']}g  ", "green"),
                        (f"Protein {item_dict['protein']}g  ", "red3"),
                        (f"Fiber {item_dict['fiber']}g", "tan"),
                        ("\n"),
                    )
                )

                break

    except Exception as e:
        console.print(f"Error: {e}")


def log_edit(log_path=None):
    console = Console()
    console.print(f"Editing entry in log...", style="red italic", justify="center")
    return


# def library_add():
#     console = Console()
#     console.print(
#         f"Adding new entry to library...", style="red italic", justify="center"
#     )
#     return


# def library_edit():
#    console = Console()
#    console.print(f"Editiing entry in library...", style="red italic", justify="center")
#    return


def date_output():
    console = Console()
    try:
        # if args[1] == "check":
        # entered_date = date.fromisoformat(arfile_pathgs[2]).strftime("%-m/%-d/%Y")
        if input_date:
            console.print(
                f"Prior - {input_date}",
                style="bold italic red",
                justify="center",
                highlight=False,
            )

        else:
            console.print(
                f"Today - {todays_date}",
                style="bold italic",
                justify="center",
                highlight=False,
            )

    except Exception as e:
        console.print(f"Error: {e}")


# TODO set this up, required for display to function accurately
def set_goals(goals_path="None"):
    console = Console()
    console.print("Current goals:\n")
    pass


def main(args):
    console = Console()
    console.print(
        "\nCalorieTerm",
        justify="center",
        style="bold white",
    )

    file_paths = setup_log_files()
    if file_paths == None:
        console.print(
            "FATAL ERROR: Could not set up log files. Exiting.", style="red bold"
        )
        return
    log_path = file_paths["food_log"]
    goals_path = file_paths["current_goals"]

    # arg check for which function to run
    try:
        match args[1]:
            case "check":
                log_check(log_path)
                return
            case "add":
                match args[2]:
                    case "log":
                        log_add(log_path)
                    # case "lib":
                    #    library_add()
            case "edit":
                match args[2]:
                    case "log":
                        log_edit(log_path)
                        return
                    # case "library":
                    #    library_edit()
                    #    return
                    case _:
                        return
            case "goals":
                set_goals(goals_path)
            case _:
                print("case _:")
                return

        date_output()
        print()
        summary_print()
        print()
        table_today()
        print()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main(args)
