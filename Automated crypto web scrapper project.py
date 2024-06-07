#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[5]:


url = 'https://coinmarketcap.com/currencies/bitcoin/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[7]:





# In[10]:





# In[11]:


print(soup)


# In[ ]:


<span data-role="coin-name" title="Bitcoin" class="sc-d1ede7e3-0 bEFegK">Bitcoin<span> <span data-role="coin-name" title="Bitcoin" class="sc-d1ede7e3-0 bEFegK">Bitcoin<span class="sc-d1ede7e3-0 bwRagp coin-name-mobile"> price</span>&nbsp;</span>


# In[17]:


soup.find('span',class_ ='sc-d1ede7e3-0 bEFegK' ).text


# In[18]:


crypto_name = soup.find('span',class_ ='sc-d1ede7e3-0 bEFegK' ).text

print(crypto_name)


# In[31]:


print(crypto_nam)


# In[30]:


crypto_nam


# In[29]:


crypto_nam = crypto_name.replace('price','')


# In[23]:


crypto_price = soup.find('span', class_='sc-d1ede7e3-0 fsQm base-text').text


# In[25]:


final_price = crypto_price.replace('$','')


# In[26]:


final_price


# In[36]:


from datetime import datetime

dt = datetime.now()
print(dt)


# In[38]:


dict = {'Crypto Name':crypto_nam,
       'Price': final_price,
       'time': dt}

df = pd.DataFrame([dict])
df


# In[35]:


from datetime import datetime

dt = datetime.now()
print(dt)


# In[40]:


df.to_csv(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv')


# In[41]:


import os 


# In[43]:


if os.path.exists(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv'):
    df.to_csv(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv', mode ='a', header = False, )
else :
    df.to_csv(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv')


# ## Let's put all together
# 

# In[50]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os 
import time
from datetime import datetime


# In[55]:


def automated_call():

    url = 'https://coinmarketcap.com/currencies/bitcoin/'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html')

    crypto_name = soup.find('span',class_ ='sc-d1ede7e3-0 bEFegK' ).text

    crypto_nam = crypto_name.replace('price','')

    crypto_price = soup.find('span', class_='sc-d1ede7e3-0 fsQm base-text').text

    final_price = crypto_price.replace('$','')

    dt = datetime.now()

    dict = {'Crypto Name':crypto_nam,
           'Price': final_price,
           'time': dt}

    df = pd.DataFrame([dict])

    if os.path.exists(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv'):
        df.to_csv(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv', mode ='a', header = False, index = False )
    else :
        df.to_csv(r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv')


# In[56]:


while True:  
    automated_call()
    time.sleep(10)


# In[ ]:


print(crypto_nam)


# In[ ]:


crypto_nam


# In[ ]:




