import sys

def get_sys_path():
    collect=[]
    for p in sys.path:
        collect.append(p)
    return collect

print(get_sys_path())