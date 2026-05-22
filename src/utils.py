import random

def generate_acc_number():
    return random.randint(1000000, 9999999)

def generate_routing_number():
    return random.randint(1000000, 9999999)


if __name__ == "__main__":
    print(generate_routing_number())