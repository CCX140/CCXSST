from dataWarpper import DataWarpper

w = DataWarpper(period=1)
w.load_csv("../archive/btc1minNoNaN.csv")
print(w.ma(nb_periods=20,cursor=1000000))
print(w.price(cursor=1000000))