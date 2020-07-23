
import sys
import json





"""
def read_tsv(file_name: str) -> list:
    ret=[]
    with open(fule_name,'r') as handle:
        for line in handle:
            if line.startswith("\t")
            continue
        splitted = line.strip().split("\t")
        d = dict(zip(header, splitted))
        ret.append(d)
    return ret

file_name=sys.argv[1]
ret=read_tsv(file_name)
print(ret)

"""

"""
def read_tsv(file_name: str) -> list
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret
file_name = sys.argv[1]
ret=read_tsv(file_name)
print(ret)
"""
"""
def read_txt(file_name: str) -> str:
    ret=""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

file_name = sys.argv[1]
txt = read_txt(file_name)
print(txt)
"""
"""
def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret
file_name = sys.argv[1]
ret = read_csv(file_name)
print(ret)
"""



