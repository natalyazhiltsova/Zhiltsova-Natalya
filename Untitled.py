#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Элементы списка вводятся по одному в строке, строка режется на части по пробелам, элемнты списка преобразуются в числа
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
min(numbers)


# In[33]:


#Элементы списка вводятся по одному в строке, строка режется на части по пробелам, элемнты списка преобразуются в числа
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
max(numbers)


# In[39]:


numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in numbers:
    if i==0:
        numbers.remove(i)
print(numbers)


# In[40]:


numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
a=int(input("Введите число: "))
for i in numbers:
    if i==a:
        numbers.remove(i)
print(numbers)


# In[ ]:




