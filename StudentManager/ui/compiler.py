import os

if __name__ == '__main__':
    r = os.listdir(r'./prebuild/')
    for i in r:
        if '.ui' in i:
            f = i.replace('.', '_') + ".py"
            os.system(f"pyside6-uic ./prebuild/{i} > {f}")
