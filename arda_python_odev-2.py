#!/usr/bin/env python
# coding: utf-8

# In[180]:


#Kullanıcı Tanımlama Programı
user=[]
ad=input("Enter Your Name : ")
user.append(ad)
soy=input("Enter Your Surname : ")
user.append(soy)
yas=int(input("Enter Your Age : "))
user.append(yas)
tarih = int(input("Enter Your  Birth Date (Just Year!): "))
user.append(tarih)
for i in user:
    print(i)
if tarih >=2002:
    print("!!!!You can't go out because it's too dangerous!!!!")
elif tarih <= 2002:
    print("!!!!You can go out to the street!!!!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




