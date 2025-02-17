import json
import os
import random
from cryptography.hazmat.primitives.asymmetric import dh


def generate_dh_parameters(key_size=2048) -> str:
    g = random.choice([2, 5])
    parameters = dh.generate_parameters(generator=g, key_size=key_size)
    numbers = parameters.parameter_numbers()
    return f'{numbers.g}_{numbers.p}'


def main() -> None:
    key_size = 2048
    filename = 'dh_parameters.json'
    number_of_parameters = int(input('Number of parameters: '))
    save = input(f'Save to {filename}? [Y/n]: ')
    for _ in range(number_of_parameters):
        parameters = generate_dh_parameters(key_size)
        print(f'\n{parameters}')
        if save.lower() != 'n':
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump({}, file, indent=4)
            with open(filename, 'r') as file:
                data = json.load(file)
            with open(filename, 'w') as file:
                if str(key_size) not in data:
                    data[str(key_size)] = []
                data[str(key_size)].append(parameters)
                json.dump(data, file, indent=4)
            print(f'\nSaved in {filename}')
    input('\nPress Enter to exit')


if __name__ == '__main__':
    main()
