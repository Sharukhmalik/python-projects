from selenium import webdriver


# In[1]:


from datetime import datetime
import os
import sys


# In[ ]:


# Mad Money is an American finance television program hosted by Jim Cramer that began airing on CNBC on March 14, 2005. Its main focus is investment and speculation, particularly in public company stocks. Mad Money. Genre. Talk show.


# In[28]:


#### import all required libraries and run selenium in headless mode, and will extract data of mad money you tube videos


# In[2]:


from selenium.webdriver.chrome.options import Options


# In[3]:


from selenium.webdriver.chrome.service import Service


# In[29]:


#### youtube url for mad money playlist


# In[4]:


website = "https://www.youtube.com/playlist?list=PLVbP054jv0KpV2leJ9HHIMqZEkCPX-iPV"


# In[30]:


#### path for driver location


# In[5]:


path = "/Users/sharukh-malik/Downloads/chrome_driver/"


# In[4]:


# get path of executable that we are going to create


# In[3]:


appliaction_path = os.path.dirname(sys.executable)


# In[5]:


# customize the file name with date


# In[6]:


now = datetime.now()


# In[7]:


# use string from time to get time in string format


# In[8]:


month_day_year = now.strftime("%m%d%Y")


# In[9]:


month_day_year


# In[6]:


# headless mode


# In[7]:


options = Options()


# In[8]:


options.headless = True


# In[9]:


service = Service(excecutable_path = path)


# In[10]:


driver  = webdriver.Chrome(service = service, options=options)


# In[11]:


driver.get(website)


# In[31]:


#### xpath taken from inspect page of madmoney ypu tube page


# In[12]:


containers = driver.find_elements(by = "xpath", value='//div[@id="content"]//div[@id="contents"]//div[@id="content"]//div[@id="meta"]')


# In[14]:


titles = []
views = []
channel = []
links = []


# In[15]:


import pandas as pd


# In[32]:


### based on available I have target three features title, views, channel, links


# In[16]:


for container in containers:
    title = container.find_element(by = "xpath", value='./h3/a').get_attribute("title")
    tag = container.find_element(by = "xpath", value='.//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]').text
    view = container.find_element(by = "xpath", value='.//span[1][contains(@class, "style-scope yt-formatted-string")]').text
    
    link = container.find_element(by = "xpath", value='.//h3//a[@id="video-title"]').get_attribute("href")
    

# 
    titles.append(title)
    views.append(view.split(" ")[0])
    channel.append(tag.split(" ")[0])
    links.append(link)


# In[18]:


titles


# In[19]:


views


# In[20]:


channel


# In[21]:


links


# In[25]:


my_dict = {"titles":titles, "channel": channel, "total_views": views, "video_link":links}


# In[26]:


df = pd.DataFrame(my_dict)


# In[27]:


df


# In[ ]:


file_name = f'news-{month_day_year}.csv'


# In[ ]:


final = os.path.join(appliaction_path, file_name)


# In[ ]:


df.to_csv(final)


# In[ ]:


driver.quit()


# In[ ]:





# In[ ]:




