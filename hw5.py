#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_single_digit(digit):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits[digit]

def read_number(number):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    
    if number < 0 or number > 999:
        print('잘못된 입력입니다. 세 자리 정수를 입력하세요.')
        return
    
    if number == 0:
        return '영'
    else:
        hundred = number // 100
        ten = (number % 100) // 10
        one = number % 10
        
        result = ''
        if hundred != 0:
            result += read_single_digit(hundred) 
        if ten != 0:
            result += read_single_digit(ten) 
        if one != 0:
            result += read_single_digit(one)
        return result

def main():
    number = input('세 자리 정수 입력: ')
    if not number.isdigit():
        print('잘못된 입력입니다. 숫자를 입력하세요.')
    else:
        number = int(number)
        print(read_number(number))

if __name__ == '__main__':
    main()


# In[ ]:




