#!/usr/bin/env python
# coding: utf-8

# In[5]:


liste = []
g="Giriniz :"
ad=input("Adınızı "+ g )
liste.append(ad)
soyad=input("Soyadınızı {} :".format(g))
liste.append(soyad)
yas=int(input("Yaşınızı "+ g))
liste.append(yas)
yer=input("Nerelisiniz: ")
liste.append(yer)
tarih=int(input("Doğum Yılınızı Giriniz: "))
liste.append(tarih)
print(f"Adınız :"+ liste[0])
print(f"Soyadınız : "+liste[1])
print(f"Yaşınız :",liste[2])
print(f"Memleketiniz :"+liste[3])
print(f"Doğum Tarihiniz :",liste[4])
print("Liste :", liste)
print("Listenin ilk verisi : ", type(liste[0]))
print("Listenin ikinci verisi : ", type(liste[1]))
print("Listenin üçüncü verisi : ", type(liste[2]))
print("Listenin dördüncü verisi : ", type(liste[3]))
print("Listenin beşinci verisi : ", type(liste[4]))


# In[ ]:





# In[ ]:




