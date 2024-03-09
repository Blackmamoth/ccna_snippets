binary = "01100100110010010010000111111101"
ip = "248.87.255.152"


def bin_to_ipv4(binary: str) -> str:
    octets: list[str] = []
    i = 0
    print()
    while i != len(binary):
        octets.append(binary[i:i+8])
        i += 8
    nums = [int(octet, 2) for octet in octets]
    return ".".join(str(num) for num in nums)


def ipv4_to_bin(ip: str) -> str:
    decimals: list[str] = [str(f"{int(decimal):b} ")
                           for decimal in ip.split(".")]
    binary = ""
    for decimal in decimals:
        while len(str(decimal)) <= 8:
            decimal = "0" + decimal
        binary += decimal
    # binary = "".join(f"{decimal:b} " for decimal in decimals)
    return binary


print(ipv4_to_bin(ip))

print(bin_to_ipv4(binary))
