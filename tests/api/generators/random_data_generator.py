from faker import Faker


fake = Faker()


def get_random_str(str_len: int) -> str:
    return fake.text(max_nb_chars=str_len)


def get_random_int(min_value: int = 1, max_value: int = 1000) -> int:
    return fake.random_int(min=min_value, max=max_value)


def get_random_email_str() -> str:
    return fake.email()
