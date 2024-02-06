def ip_to_binary(ip_address):
    # Rozdělení IP adresy na části
    parts = ip_address.split('.')
    # Inicializace prázdného řetězce pro binární reprezentaci
    binary_representation = ''
 
    # Procházení každé části IP adresy
    for part in parts:
        # Převedení části IP adresy na binární a přidání k výslednému řetězci
        binary_representation += bin(int(part))[2:].zfill(8)
        # Zfill(8) zajišťuje, že každý segment bude mít délku 8 bitů
 
    return binary_representation
 
# Příklad použití
ip_address = '198.128.95.125'
binary_ip = ip_to_binary(ip_address)
print(binary_ip)