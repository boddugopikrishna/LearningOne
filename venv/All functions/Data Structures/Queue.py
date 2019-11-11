class Empty(Exception):

    pass
import re

class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self,shares):
        self.data.append(shares)

    def dequeue(self):
        if self.data == 0:
            raise Empty("Queue is Empty")
        return self.data.pop(0)

    def __str__(self):
        return self.data

def transaction_list(transaction):
    trans_list = []
    for val in transaction:
        if "buy" in val:
            x = re.findall("[\d]+", val)
            trans_list.append(("buy",int(x[0]),int(x[1])))
        else:
            x = re.findall("[\d]+", val)
            trans_list.append(("Sell", int(x[0]), int(x[1])))
    return trans_list

#print(transaction_list(["buy 20 shares at 5","Sell 10 shares at 2"]))


q = Queue()
tran_list = transaction_list(["buy 100 shares at 20","buy 20 shares at 24","buy 200 shares at 36","Sell 150 shares at 30"])
print(tran_list)
capital_gain = 0
for val in tran_list:
    print(val)
    if val[0] == 'buy':
        q.enqueue((val[1],val[2]))
        print(q.__str__())
    elif val[0] == "Sell":
        val_at_first_index = q.dequeue()
        print(val_at_first_index)
        shares, price = val_at_first_index[0], val_at_first_index[1]
        print("share = {0} and price = {1}".format(shares,price))
        if val[1] <= shares:
            print("val[1] = {0} and shares =  {1}".format(val[1],shares))
            capital_gain = val[1] * (price - val[2])
            print(capital_gain)
        else:
            remaining_Shares = val[1] - shares
            print("Remaining Share : {0}".format(remaining_Shares))
            capital_gain = shares * (val[2] - price)
            print(capital_gain)
            while remaining_Shares > 0:
                poped_val = q.dequeue()
                print(poped_val)
                shares, price = poped_val[0], poped_val[1]
                if remaining_Shares > shares:
                    print("share = {0} and price = {1}".format(shares, price))
                    capital_gain = capital_gain + shares * (val[2] - price)
                    remaining_Shares = remaining_Shares - shares
                else:
                    capital_gain = capital_gain + remaining_Shares * (val[2] - price)
                    remaining_Shares = 0
            print(capital_gain)








