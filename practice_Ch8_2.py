# -*- coding: utf-8 -*-
# 8.4 発展例：住宅ローン
def findPayment(loan, r, m):
    """loanとrをfloat型として,mをint型とする
       月割りの金利をrとして,借入額loanの住宅ローンを
       mヶ月で返済する場合の毎月の返済額を返す"""
    return loan * ((r * (1 + r)**m) / ((1 + r)**m - 1))

# mortgage(モーギッジ:ローン)
# 抽象クラス
class Moortgage(object):
    """異なる種類の住宅ローンを構築するための抽象クラス"""
    def __init__(self, loan, annRate, months):
        """loanとannRateをfloat型とし、monthsをint型とする
           借入額loan, 返済月数months, 年利annRateであるような
           住宅ローンを新たに生成する"""
        self.loan = loan
        self.rate = annRate/12 # 1年の金利のため
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None  # 住宅ローンの種類(サブクラスで使用)
    
    def makePayment(self):
        """返済を行う"""
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate # 利息との相殺を計算
        self.outstanding.append(self.outstanding[-1] - reduction) # 利息との相殺後をoutstand:借入額から引く
    
    def getTotalPaid(self):
        """これまで支払った総額を返す"""
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

# 固定金利の住宅ローン
class Fixed(Moortgage):
    def __init__(self, loan, r, months):
        Moortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed,' + str(round(r * 100, 2)) + '%'
    
# ポイントありの固定金利の住宅ローン
class FixedWithPts(Moortgage):
    def __init__(self, loan, r, months, pts):
        Moortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100)]
        self.legend = 'Fixed, ' + str(round(r * 100, 2)) + '%, '\
                            + str(pts) + ' points'

# 最初はティザーレイトでその後高くなる金利
class TwoRate(Moortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Moortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12
        self.legend = str(teaserRate * 100)\
                    + '% for ' + str(self.teaserMonths)\
                    + ' months, then ' + str(round(r * 100, 2)) + '%'
    
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
                                        self.rate,
                                        self.months - self.teaserMonths)
        Moortgage.makePayment(self)

# 各住宅ローンの総コストを計算し表示する関数
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))

compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts=3.25, ptsRate=0.05, varRate1=0.045, varRate2=0.095, varMonths=48)