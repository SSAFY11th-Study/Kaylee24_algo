def hex_to_bin():
    bin_str = format(int(hex_str, 16), f'0{int(N)*4}b')
    return bin_str


T = int(input())
for t in range(1, T+1):
    N, hex_str = input().split()
    print(f'#{t} {hex_to_bin()}')