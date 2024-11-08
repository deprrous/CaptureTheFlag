# Manual implementation of xtime function
def xtime(a):
    if a & 0x80: 
        return ((a << 1) ^ 0x1B) & 0xFF  
    else:
        return (a << 1) & 0xFF 

def mix_columns(state):
    print("MixColumns Step:")
    for i in range(4):
        a = state[i * 4:i * 4 + 4]

        temp0 = xtime(a[0]) ^ xtime(a[1]) ^ a[2] ^ a[3]
        temp1 = a[0] ^ xtime(a[1]) ^ xtime(a[2]) ^ a[3]
        temp2 = a[0] ^ a[1] ^ xtime(a[2]) ^ xtime(a[3])
        temp3 = xtime(a[0]) ^ a[1] ^ a[2] ^ xtime(a[3])

        print(f"Mixing Column {i}:")
        print(f"{{{xtime(a[0]):02X}}} * {{02}} = {format(xtime(a[0]), '08b')}")
        print(f"{{{xtime(a[1]):02X}}} * {{03}} = {format(xtime(a[1]), '08b')}")
        print(f"{{{a[2]:02X}}} = {format(a[2], '08b')}")
        print(f"{{{a[3]:02X}}} = {format(a[3], '08b')}")
        print(f"Result: {temp0:02X}\n")

        state[i * 4] = temp0
        state[i * 4 + 1] = temp1
        state[i * 4 + 2] = temp2
        state[i * 4 + 3] = temp3

    print(f"Updated state after MixColumns: {state}\n")

def inv_mix_columns(state):
    print("InvMixColumns Step:")
    for i in range(4):
        a = state[i * 4:i * 4 + 4]

        temp0 = xtime(xtime(a[0] ^ a[2])) ^ xtime(a[1]) ^ a[3]
        temp1 = a[0] ^ xtime(xtime(a[1] ^ a[3])) ^ xtime(a[2])
        temp2 = a[0] ^ a[1] ^ xtime(xtime(a[2] ^ a[0])) ^ xtime(a[3])
        temp3 = xtime(a[0]) ^ a[1] ^ a[2] ^ xtime(xtime(a[3]))

        print(f"Unmixing Column {i}:")
        print(f"{{{xtime(xtime(a[0] ^ a[2])):02X}}} * {{0E}} = {format(xtime(xtime(a[0] ^ a[2])), '08b')}")
        print(f"{{{xtime(a[1]):02X}}} * {{0B}} = {format(xtime(a[1]), '08b')}")
        print(f"{{{a[2]:02X}}} = {format(a[2], '08b')}")
        print(f"{{{a[3]:02X}}} = {format(a[3], '08b')}")
        print(f"Result: {temp0:02X}\n")

        state[i * 4] = temp0
        state[i * 4 + 1] = temp1
        state[i * 4 + 2] = temp2
        state[i * 4 + 3] = temp3

    print(f"Updated state after InvMixColumns: {state}\n")

# Example state
state = [
0x0e ,0xce ,0xf2 ,0xd9,
0x36 ,0x72,0x6b ,0x2b,
0x34, 0x25, 0x17 ,0x55,
0xae, 0xb6 ,0x4e ,0x88
]


mix_columns(state)
for i in range(0,16,4):
    print("prev",[hex(j) for j in state[i:i+4]])

inv_mix_columns(state)
for i in range(0,16,4):
    print("after",[hex(j) for j in state[i:i+4]])
