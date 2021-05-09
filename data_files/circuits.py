
def half_sub(a, b):
    borrow = ~a & b
    out   = a ^ b
    return out, borrow

def full_sub(a, b, bin):
    out, b1 = half_sub(a, b)
    out, b2 = half_sub(out, bin)
    bout = b1 | b2
    return out, bout


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" 