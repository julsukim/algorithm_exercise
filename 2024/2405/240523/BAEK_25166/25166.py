price, coogie = map(int, input().split())

ari = (1 << 10) - 1

if price & ~ari == 0:
    print("No thanks")
else:
    rest = price - ari
    if rest & ~coogie == 0:
        print("Thanks")
    else:
        print("Impossible")
