from cryptography.hazmat.primitives.asymmetric import dh


def generate_p(g=2, key_size=1024) -> tuple[int, int]:
    parameters = dh.generate_parameters(generator=g, key_size=key_size)
    numbers = parameters.parameter_numbers()
    return numbers.p


def main():
    p = generate_p()
    print(p)


if __name__ == '__main__':
    main()
