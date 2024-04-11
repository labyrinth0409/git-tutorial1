#!/usr/bin/env python
# coding: utf-8

# In[2]:


def rep_char(c, n):
  
    print(c * n)

def draw_line_string(msg):
   
    nstr = len(msg)
    rep_char('-', nstr * 2 + 4)
    print(f'* {msg} *')
    rep_char('-', nstr * 2 + 4)

def welcome_message():
   
    name = input("한국에 방문하신 교포 지인의 영어 이름을 입력하세요: ")
    msg1 = f"환영합니다, {name}님! 한국에 오신 것을 진심으로 환영합니다."
    msg2 = f"{name}님의 방문으로 인해 기쁩니다."

    
    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    
    rep_char('*', nstr + 4)
    print(f'* {msg1} *')
    print(f'* {msg2} *')
    rep_char('*', nstr + 4)


welcome_message()


# In[ ]:




