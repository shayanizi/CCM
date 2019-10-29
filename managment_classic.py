#!/usr/bin/python
class ManageClassic:
    def __init__(self,R,balance,stop_loss,take_profit):
        self.R=R
        self.balance=balance
        self.stop_loss=stop_loss
        self.take_profit=take_profit
    def cal_vol(self):
        return ((self.R*self.balance)/(10*self.stop_loss))
    def profit(self):
        return (self.take_profit/self.stop_loss)
M=ManageClassic(
    float(input("insert R (option 1 or 2 percent) >>")),
    float(input("plz enter your balance >>")),
    float(input("how stop loss?! >>")),
    float(input("how take profit?! >>"))
)
M2=ManageClassic.cal_vol(M)
print("your volum is >> " , M2)
M3=ManageClassic.profit(M)
print("your profit is >> ",int(M3))
