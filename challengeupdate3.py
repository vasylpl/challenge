print("Chceš počítat binární do desítkové (1) nebo desítkovou do binární (2)?")
vyber = int(input("Váš výběr: "))

if vyber == 1:
    print("Vybral jsi si převod z binární do desítkové.")
    def ip_to_binary(ip_address):
        parts = ip_address.split('.')
        binary_representation = ''
        for part in parts:
            binary_representation += bin(int(part))[2:].zfill(8)
            binary_representation += '.'
        binary_representation = binary_representation[:-1]
        return binary_representation

    ip_address = '198.128.95.125'
    binary_ip = ip_to_binary(ip_address)
    print(binary_ip)
elif vyber == 2:
    print("Vybral jsi si převod z desítkové do binární:")
    def binary_to_ip(binary_address):
        parts = [binary_address[i:i+8] for i in range(0, len(binary_address), 8)]
        decimal_parts = [str(int(part, 2)) for part in parts]
        ip_address = '.'.join(decimal_parts)
        return ip_address

    binary_ip = '11000110100000000101111101111101'
    ip_address = binary_to_ip(binary_ip)
    print(ip_address)
else:
    print("Nesprávný výběr.")