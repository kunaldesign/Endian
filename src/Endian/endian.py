def big_to_little_str(big_endian_hex):
    endian_hex = big_endian_hex
    k = 2
    o = 0
    endian_hex_convert= ""
    for i in range(int(len(endian_hex)/2)):
        y = endian_hex[o:k]
        endian_hex_convert = y+endian_hex_convert
        k += 2
        o += 2
    return endian_hex_convert
