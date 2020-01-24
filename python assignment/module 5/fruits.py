fruit={'apple':{'binomial_name':'malus domestica','major_producer':['china,US,Turkey'],
                'nutrition':{'carbohydrates':'13.81g','fat':'0.17g','protein':'0.26g'}},
       'banana':{'binomial_name':'musa','major_producer':['china,INDIA,Turkey'],
                'nutrition':{'carbohydrates':'17.81g','fat':'3.17g','protein':'1.26g'}},
       'guava':{'binomial_name':'Psidium guajava','major_producer':['china,INDIA,sri lanka'],
                'nutrition':{'carbohydrates':'11.81g','fat':'2.17g','protein':'1.10g'}}}
l1=[fruit['apple']['nutrition']['carbohydrates'],
    fruit['banana']['nutrition']['carbohydrates'],
    fruit['guava']['nutrition']['carbohydrates']]
print('maximum carbohydrates =',max(l1))

l2=[fruit['apple']['nutrition']['fat'],
    fruit['banana']['nutrition']['fat'],
    fruit['guava']['nutrition']['fat']]
print('maximum fat =',max(l2))

l3=[fruit['apple']['nutrition']['protein'],
    fruit['banana']['nutrition']['protein'],
    fruit['guava']['nutrition']['protein']]
print('maximum protein =',max(l3))




