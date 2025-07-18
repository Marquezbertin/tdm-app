import random


class DataGenerator:
    def __init__(self):
        from faker import Faker

        self.faker = Faker("pt_BR")  # Para dados brasileiros

    def generate_cpf(self):
        def dv(n):
            r = sum([(n // 10**i) % 10 * (i + 2) for i in range(8, -1, -1)]) % 11
            return 0 if r < 2 else 11 - r

        n = random.randint(10**8, 10**9 - 1)
        d1 = dv(n)
        d2 = dv(n * 10 + d1)
        return f"{n:09d}{d1}{d2}"

    def generate_data(self, data_type, count=1):
        data = []
        for _ in range(count):
            if data_type == "user":
                user = {
                    "nome": self.faker.name(),
                    "cpf": self.generate_cpf(),
                    "endereco": self.faker.street_address(),
                    "cep": self.faker.postcode(),
                    "numero": self.faker.building_number(),
                    "email": self.faker.email(),
                    "telefone": self.faker.phone_number(),
                    "cidade": self.faker.city(),
                    "estado": self.faker.estado_nome(),
                    "pais": self.faker.current_country(),
                }
                data.append(user)
            elif data_type == "customer":
                data.append(self.faker.company())
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        return data

    def configure_data_types(self, types):
        self.data_types = types

    def generate_multiple_data_types(self, count=1):
        data = {}
        for data_type in self.data_types:
            data[data_type] = self.generate_data(data_type, count)
        return data