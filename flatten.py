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