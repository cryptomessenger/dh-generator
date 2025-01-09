import random
from cryptography.hazmat.primitives.asymmetric import dh
from datetime import datetime


def generate() -> str:
    g = random.choice([2, 5])
    parameters = dh.generate_parameters(generator=g, key_size=2048)
    numbers = parameters.parameter_numbers()
    result = f'{numbers.g}_{numbers.p}'
    return result


def main():
    print('Generating...\n')
    start = datetime.now()
    parameters = generate()
    print(f'Parameters: {parameters}')
    time_spent = datetime.now() - start
    seconds = round(time_spent.total_seconds())
    print(f'\nTime spent: {seconds} sec')
    input()


if __name__ == '__main__':
    main()
