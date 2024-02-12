def is_valid_binary(binary):
    return all(bit == '0' or bit == '1' for bit in binary)

def binary_to_ip(binary_ip):
    if len(binary_ip) != 32:
        return "Neplatná IP adresa! IP adresa musí mít 32 bity."

    parts = [binary_ip[i:i+8] for i in range(0, 32, 8)]
    decimal_parts = []
    for part in parts:
        decimal_parts.append(str(int(part, 2)))

    return '.'.join(decimal_parts)

print("Chceš počítat binární do desítkové (1) nebo desítkovou do binární (2)?")
vyber = int(input("Váš výběr: "))

if vyber == 1:
    print("Vybral jsi si převod z binární do desítkové.")
    binary_ip = input("Zadej binární IP adresu: ")
    if not is_valid_binary(binary_ip):
        print("Neplatná IP adresa! Zadejte prosím platnou binární IP adresu.")
    else:
        decimal_ip = binary_to_ip(binary_ip)
        print(decimal_ip)
elif vyber == 2:
    print("Vybral jsi si převod z desítkové do binární.")
    # V tomto případě bychom potřebovali funkci pro převod z desítkového formátu na binární.
else:
    print("Nesprávný výběr.")

