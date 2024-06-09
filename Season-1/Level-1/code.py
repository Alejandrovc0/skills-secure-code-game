'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

# Solution:
# The code is vulnerable to a payment imbalance attack.
# The attacker can trick the system by sending a payment followed by a payment reversal.
# This results in a zero net, which is incorrect.
# The solution is to check if the net is zero after processing all items.
# If the net is not zero, return a message indicating a payment imbalance.
# Otherwise, return a message indicating full payment received.


from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000
MIN_QUANTITY = 0
MAX_QUANTITY = 100
MAX_TOTAL = 100000

def validorder(order: Order):
    payments = Decimal('0')
    expenses = Decimal('0')


    for item in order.items:
        if item.type == 'payment':
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT:
                expenses += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"
    
    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    
    else:
        return "Order ID: %s - Full payment received!" % order.id