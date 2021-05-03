import time
import threaded
from prompt_toolkit.shortcuts import CompleteStyle

import questionary


autocomplete_choices = [f"choice {i + 1}" for i in range(10)]
autocomplete_style = CompleteStyle.MULTI_COLUMN

@threaded.Threaded
def update_list():
    global autocomplete_choices

    for counter in range(10):
        time.sleep(2)
        autocomplete_choices.append(f"new choice {counter + 1}")

thread = update_list()
thread.start()

questionary.autocomplete(
    "Choose something",
    choices=autocomplete_choices,
    complete_style=autocomplete_style,
).ask()

thread.join()
