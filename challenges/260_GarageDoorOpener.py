## https://old.reddit.com/r/dailyprogrammer/comments/4cb7eh/20160328_challenge_260_easy_garage_door_opener/

STATES = {
    ("button_clicked", "OPEN"): "CLOSING",
    ("button_clicked", "CLOSED"): "OPENING",
    ("button_clicked", "OPENING"): "STOPPED_WHILE_OPENING",
    ("button_clicked", "CLOSING"): "STOPPED_WHILE_CLOSING",
    ("button_clicked", "STOPPED_WHILE_OPENING"): "CLOSING",
    ("button_clicked", "STOPPED_WHILE_CLOSING"): "OPENING",
    ("cycle_complete", "OPENING"): "OPEN",
    ("cycle_complete", "CLOSING"): "CLOSED",
    ("block_detected", "CLOSING"): "EMERGENCY_OPENING",
    ("block_detected", "OPENING"): "EMERGENCY_CLOSING",
    ("cycle_complete", "EMERGENCY_OPENING"): "OPEN_BLOCKED",
    ("cycle_complete", "EMERGENCY_CLOSING"): "CLOSED_BLOCKED",
    ("block_cleared", "OPEN_BLOCKED"): "OPEN",
    ("block_cleared", "CLOSED_BLOCKED"): "CLOSED",
}

# with bonus challenge
def door_state(clicks):
    state = "CLOSED"
    state_string, input_string = "Door: {}", "> {}."
    all_states = [state_string.format(state)]
    for click in clicks:
        all_states.append(input_string.format(click.capitalize().replace("_", " ")))
        state = STATES.get((click, state), state)
        all_states.append(state_string.format(state))
    return all_states

input_1 = """button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete""".split("\n")
output_1 = """Door: CLOSED
> Button clicked.
Door: OPENING
> Cycle complete.
Door: OPEN
> Button clicked.
Door: CLOSING
> Button clicked.
Door: STOPPED_WHILE_CLOSING
> Button clicked.
Door: OPENING
> Button clicked.
Door: STOPPED_WHILE_OPENING
> Button clicked.
Door: CLOSING
> Cycle complete.
Door: CLOSED""".split("\n")

input_2 = """button_clicked
cycle_complete
button_clicked
block_detected
button_clicked
cycle_complete
button_clicked
block_cleared
button_clicked
cycle_complete""".split("\n")
output_2 = """Door: CLOSED
> Button clicked.
Door: OPENING
> Cycle complete.
Door: OPEN
> Button clicked.
Door: CLOSING
> Block detected.
Door: EMERGENCY_OPENING
> Button clicked.
Door: EMERGENCY_OPENING
> Cycle complete.
Door: OPEN_BLOCKED
> Button clicked.
Door: OPEN_BLOCKED
> Block cleared.
Door: OPEN
> Button clicked.
Door: CLOSING
> Cycle complete.
Door: CLOSED""".split("\n")

assert door_state(input_1) == output_1
assert door_state(input_2) == output_2
