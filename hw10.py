#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import os

FILENAME = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f"# {i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def show_scores(scores):
    print("개인점수: ", end="")
    for score in scores:
        print(score, end=" ")
    print()

def save_scores(scores, filename):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():
    if os.path.exists(FILENAME):
        print("[파일 읽기]")
        scores = load_scores(FILENAME)
    else:
        print("[점수 입력]")
        scores = input_scores()
        save_scores(scores, FILENAME)
    
    print("[점수 출력]")
    show_scores(scores)
    
    average = get_average(scores)
    print(f"평균: {average:.1f}")


main()


# In[ ]:




