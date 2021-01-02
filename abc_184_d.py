# -*- coding: utf-8 -*-
class CalcMemo:
    
    def __init__(self):
        self.memo_dict = {(100, 100, 100): 0}

    def calc_e(self, x, y, z):
        if x == 100 or y == 100 or z == 100:
            return 0

        xyz = x + y + z
        xyz_tuple = (x, y, z)

        if xyz_tuple in self.memo_dict.keys():
            return self.memo_dict[xyz_tuple]

        self.memo_dict[xyz_tuple] = x/xyz*(self.calc_e(x + 1, y, z) + 1) + \
            y/xyz*(self.calc_e(x, y + 1, z) + 1) + z/xyz*(self.calc_e(x, y, z + 1) + 1)
        return self.memo_dict[xyz_tuple]
    

def main():
    x, y, z = map(int, input().split())
    a = CalcMemo()
    print(a.calc_e(x, y, z))


if __name__ == "__main__":
    main()
    
