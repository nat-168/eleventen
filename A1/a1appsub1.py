# a script to receive user input and provide an answer.

"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Katherine Son ks2395, River Strumwasser rns88
Date:   9/14/23
"""

import a1

src = input("Enter source currency: ")
dst = input("Enter target currency: ")
amt = input("Enter original amount: ")
fin = a1.exchange(src, dst, amt)
print('You can exchange '+str(amt)+' '+src+' for '+str(fin)+' '+dst+'.')
