#!/usr/bin/env python
# coding: utf-8

# In[1]:


def exchange(amount):
    five_hundred_count = amount // 500
    remaining_amount = amount % 500
    hundred_count = remaining_amount // 100
    remaining_amount %= 100
    fifty_count = remaining_amount // 50
    remaining_amount %= 50
    ten_count = remaining_amount // 10

    print('500원 동전의 개수:', five_hundred_count)
    print('100원 동전의 개수:', hundred_count)
    print('50원 동전의 개수:', fifty_count)
    print('10원 동전의 개수:', ten_count)
    
def get_integer(prompt):
    res = int(input(prompt))
    return res

            
amount = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(amount)


# In[ ]:




