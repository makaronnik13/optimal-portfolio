__author__ = 'makar'
import random
class Owners:

    wa = 0
    wb = 0
    wc = 0
    mabc = 0
    eabc = 0
    def __init__(self, number_of_variate=3):
        self.sup_dem = []
        self.summ = 0
        self.w2 = 0
        oblig_num_range = 1000
        money_range = 5000
        self.oblig_num = []
        for i in range(number_of_variate):
            self.oblig_num.append(random.randint(0, int(oblig_num_range)))
        self.money = random.randint(-money_range, money_range)
        self.risky = random.randint(100, 300)/100

    

    def getval(self, n):
        return self.oblig_num[n]

    def setval(self, n, val):
        self.oblig_num[n] = val

    def getmoney(self):
        return self.money

    def setmoney(self, val):
        self.money = val

    def getrisky(self):
        return self.risky

    def setrisky(self, val):
        self.risky = val

    @staticmethod
    def calc_w(ae, be, ce, am, bm, cm):
        Owners.wa = ae/(ae+be+ce)
        Owners.wb = be/(ae+be+ce)
        Owners.wc = ce/(ae+be+ce)
        Owners.mabc = Owners.wa*am+Owners.wb*bm+Owners.wc*cm
        Owners.eabc = Owners.wa*ae+Owners.wb*be+Owners.wc*ce

    def calc_w2(self, per):
        self.w2 = (Owners.mabc-per*0.01)/(float(self.risky)*Owners.eabc)

    def calc_full(self, co, number_of_variate=3):
        summ = 0
        for i in range(number_of_variate):
            summ += int(self.oblig_num[i])*co[i].oblig_price
        summ += int(self.money)
        self.summ = summ

    def calc_sup_dem(self, number_of_variate = 3):
        self.sup_dem = []
        self.sup_dem.append(self.summ*self.wa*(1-self.w2))
        self.sup_dem.append(self.summ*self.wb*(1-self.w2))
        self.sup_dem.append(self.summ*self.wc*(1-self.w2))

