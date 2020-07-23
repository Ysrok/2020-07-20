

seq="ATGTTATAG"
import sys
def comp1(seq):
    comp = ""
    for s in seq:
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "T":
            comp += "A"
        elif s == "G":
            comp += "C"
    return comp

def comp2(seq):
    d_comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()
    seq = sys.argv[1]
    c1=comp1(seq)
    c2=comp2(seq)
    print(seq)
    print(c1)
    print(c2)
