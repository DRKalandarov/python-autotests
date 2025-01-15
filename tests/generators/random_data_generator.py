from faker import Faker


fake = Faker()


def get_random_str(str_len: int) -> str:
    return fake.text(max_nb_chars=str_len)


def get_random_int() -> int:
    return fake.random_int(min=1, max=1000)
