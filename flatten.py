import ast
import tkinter as tk


def flatten(sequence) -> list:
    if sequence == []:
        # we reached the end of the sequence.
        return sequence
    element = [sequence[0]]
    if isinstance(sequence[0], list):
        # flatten current element as it is a list.
        element = flatten(sequence[0])
    # flatten rest of the sequence.
    rest_of_the_sequence = flatten(sequence[1:])
    return element + rest_of_the_sequence


def submit_click(input_text, output_text) -> None:
    input_value = ast.literal_eval(input_text.get())
    flat_list = flatten(input_value)

    # convert elements to string so .join() woud work.
    flat_list = [str(e) for e in flat_list]

    # compile list into a string that looks like a list.
    output_value = "[" + ", ".join(flat_list) + "]"
    output_text.delete(0, tk.END)
    output_text.insert(tk.END, output_value)


# create widgets
parent = tk.Tk()
input_label = tk.Label(parent, text="Input")
output_label = tk.Label(parent, text="Output")
input_text = tk.Entry(parent, width=70)
output_text = tk.Entry(parent, width=70)
submit = tk.Button(parent, text="Flatten", command=lambda: submit_click(input_text, output_text))

# layout
input_label.grid(row=0, column=0, padx=[10, 0], pady=[10, 0])
input_text.grid(row=0, column=1, padx=[0, 10], pady=[10, 0])
output_label.grid(row=1, column=0, padx=[10, 0], pady=[0, 10])
output_text.grid(row=1, column=1, padx=[0, 10], pady=[0, 10])
submit.grid(row=2, column=1, pady=[5, 5])

# start mainloop
parent.mainloop()
