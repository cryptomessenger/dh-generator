import random
from cryptography.hazmat.primitives.asymmetric import dh


def generate(key_size=1024) -> str:
    g = random.choice([2, 5])
    parameters = dh.generate_parameters(generator=g, key_size=key_size)
    numbers = parameters.parameter_numbers()
    return f'{numbers.g}_{numbers.p}'


def main():
    parameters = generate()
    print(parameters)


if __name__ == '__main__':
    main()
