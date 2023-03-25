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

def little_to_big_str(little_endian_hex):
    endian_hex = little_endian_hex
    k = 2
    o = 0
    endian_hex_convert= ""
    for i in range(int(len(endian_hex)/2)):
        y = endian_hex[o:k]
        endian_hex_convert = y+endian_hex_convert
        k += 2
        o += 2
    return endian_hex_convert

def endian_hex_str(normal_str):
    to_con = hex(normal_str)
    filter_str = to_con[2:]
    return filter_str.upper()

def twos_com_str(normal_str):
    to_con = len(normal_str)
    if (to_con % 2) == 0:
        change_str = normal_str
    else:
        change_str = "0" + normal_str
    return change_str