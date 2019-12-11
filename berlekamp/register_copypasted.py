def lfsr(seed, mask):
    result = seed
    nbits = mask.bit_length() - 1
    while True:
        result = (result << 1)
        xor = result >> nbits
        if xor != 0:
            result ^= mask
        yield xor, result
