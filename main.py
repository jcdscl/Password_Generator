import random


# , 'v', 'w', 'x', 'y', 'z'
# , 'V', 'W', 'X', 'Y', 'Z'
def password_generator():
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['!', '?', '#', '.', '-', '_', '*', '+', ';', '@', '%']

    password = random.choice(special) + random.choice(lower) + random.choice(numbers) + random.choice(upper)
    password += random.choice(lower) + random.choice(lower) + random.choice(numbers) + random.choice(special)
    password += random.choice(lower) + random.choice(lower) + random.choice(numbers) + random.choice(lower)

    return password


senha = password_generator()

print("Senha gerada:\t" + senha)
