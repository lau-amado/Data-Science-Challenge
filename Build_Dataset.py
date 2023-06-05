#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Import libraries
import pandas as pd
import requests


# In[23]:


def build_dataframe(category_id):
    base_url = 'https://api.mercadolibre.com/sites/MCO/search'
    items_per_offset = 50
    total_items = 1000
    offsets = range(0, total_items, items_per_offset)
    
    data = []
    for offset in offsets:
        url = f'{base_url}?category={category_id}&offset={offset}'
        response = requests.get(url)
        if response.status_code == 200:
            items = response.json()['results']
            data.extend(items)
        else:
            print(f'Request failed for offset {offset}.')
            continue
    
    df = pd.DataFrame(data)
    return df


# In[22]:


cats = requests.get('https://api.mercadolibre.com/sites/MCO/categories')
cats.json()


# In[24]:


# Usage example
category_id = 'MCO1071'
df = build_dataframe(category_id)
print(df.head())

