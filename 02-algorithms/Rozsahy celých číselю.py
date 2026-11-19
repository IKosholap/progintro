# 8 bitů: 0 až 255, -128 až 127
#16 bitů: 0 až 65535, -32768 až 32767
#32 bitů: 0 až 4294967295, -2147483648 až 2147483647
#64 bitů: 0 až 18446744073709551615, -9223372036854775808 až 9223372036854775807

cisla = [8,16,32,64]

for c in cisla:
    i = 2**c
    
    unsingned_min = 0
    unsingned_max = i-1
    signed_min = int(i/2*(-1))
    signed_max = int((i/2)-1)
    print(f"{c:02d} bitu: {unsingned_min} az {unsingned_max}, {signed_min} az {signed_max}")
    