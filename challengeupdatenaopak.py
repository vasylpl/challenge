def binary_to_ip(binary_address):
    # Rozdělení binární IP adresy na čtyři části po osmi bitech
    parts = [binary_address[i:i+8] for i in range(0, len(binary_address), 8)]
    # Převedení každé části na desítkovou hodnotu a následně na řetězec
    decimal_parts = [str(int(part, 2)) for part in parts]
    # Spojení částí IP adresy s tečkami
    ip_address = '.'.join(decimal_parts)
    return ip_address
 
# Příklad použití
binary_ip = '11000110100000000101111101111101'
ip_address = binary_to_ip(binary_ip)
print(ip_address)