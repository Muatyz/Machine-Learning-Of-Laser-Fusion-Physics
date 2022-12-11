#基本的爬虫包
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

#身份验证
cookie='_ga=GA1.2.1879784673.1667237240; _ga_HEQ0YF2VYL=GS1.1.1667268958.2.1.1667269048.0.0.0'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'Cookie':cookie,
    'Connection':'keep-alive'
    }

#发起请求,判断验证
url='https://nlte.nist.gov/FLY/USERS/heyicheng/FLYmain.html'
r=requests.get(url=url,headers=headers)
if r.status_code==200:
    print('身份验证成功')
else:
    print('身份验证失败，正在关闭程序')
    os.exit()

#driver函数准备
driver_path='D:/miniconda/msedgedriver.exe'
#忽略无用日志
options=webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches',['enable-automation','enable-logging'])
#使用Service定义driver
s=Service(driver_path)
driver=webdriver.Edge(service=s,options=options)
driver.get(url)

#计算参数上传区
para_path='D:/ml/Machine-Learning-Of-Laser-Fusion-Physics/flychk.spider/parameters/test.txt'#参数路径
#定位标题创建输入框
driver.find_element(By.NAME,'COMMENTS').send_keys('test')
print('本轮计算已命名')
#上传初始参数文件
driver.find_element(By.NAME,'runfile').send_keys(para_path)
print('文件已上传。等待服务器传回数据...')
#使用数据开始计算
submit_xpath='/html/body/span/form/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/th/table/tbody/tr[2]/td[3]/input'#定位网页元素submit
driver.find_element(By.XPATH,submit_xpath).submit()
#等待计算完成
time.sleep(5)
#下载本轮计算完成的数据



#退出浏览器s
time.sleep(60)#时间控制，需要结合后面的代码来判断是否需要继续延长时间或者取消
print('本轮计算已完成，正在关闭进程')
driver.quit()