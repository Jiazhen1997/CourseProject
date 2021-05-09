from . import ansi
import os
import math

def _get_terminal_columns():
    
    _, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def erase():
    
    ansi.move_cursor_line_beggining()
    ansi.erase_from_cursor_to_end()

def refresh(state):
    
    erase()
    lines, num_rows = _construct_output(state)
    for line in lines:
        print(line)
    
    ansi.move_cursor_previous_lines(num_rows)
    
    ansi.move_cursor_horizental(len(lines[0])+1)
    ansi.flush()

def _construct_output(state):
    columns = _get_terminal_columns()
    def number_of_rows(line):
        return int(math.ceil(float(len(line))/columns))
    displayed_lines = []
    
    num_rows = 0
    prompt_line = 'Path: ' + state.input
    displayed_lines.append(prompt_line)
    num_rows += number_of_rows(prompt_line)
    matches = state.get_matches()
    if matches:
        
        selected_command_index = matches.index(state.get_selected_match())
        matches_to_display = matches[max(0, selected_command_index - 10 + 1):max(10, selected_command_index + 1)]
        for index, m in enumerate(matches_to_display):
            fm = ' ' + m
            num_rows += number_of_rows(fm)
            
            for w in state.input.split(' '):
                if w:
                    fm = fm.replace(w, ansi.bold_text(w))
            
            if m == state.get_selected_match():
                fm = ansi.select_text(fm)
            displayed_lines.append(fm)
    else:
        not_found_line = 'Nothing found'
        displayed_lines.append(not_found_line)
        num_rows += number_of_rows(not_found_line)
    return displayed_lines, num_rows

