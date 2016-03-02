import random

__author__ = 'makar'
class Companies:



    def __init__(self, number_of_variate=2):
        oblig_range = 100
        self.num = number_of_variate
        self.oblig_m = 0
        self.oblig_e = 0
        self.oblig_price = 0
        self.oblig_val = []
        for i in range(self.num):
            self.oblig_val.append(random.randint(10, int(oblig_range)))
        self.calc_me()
        self.calc_e()

    def getval(self, n):
        return self.oblig_val[n]

    def setval(self, n, val):
        self.oblig_val[n] = val

    def calc_me(self):
        val_sum = 0
        for i in range(self.num):
            val_sum += int(self.oblig_val[i])
        self.oblig_m = val_sum/self.num

    def calc_e(self):
        val_sum = 0
        for i in range(self.num):
            val_sum += pow(int(self.oblig_val[i])-self.oblig_m, 2)
        self.oblig_e = val_sum/self.num

    @property
    def getm(self):
        return self.oblig_m
    @property
    def gete(self):
        return self.oblig_e