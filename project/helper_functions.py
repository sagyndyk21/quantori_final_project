from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        input_sequences = [line.strip() for line in file]

    return input_sequences


def conversion_format(input_sequence: str, output_sequence: str) -> str:
    return f'{input_sequence} ----> {output_sequence}'
