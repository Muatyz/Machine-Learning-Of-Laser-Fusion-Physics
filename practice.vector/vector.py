#导入包
import pandas as pd;
import numpy as np;
import seaborn as sns;
from sklearn import datasets;
from sklearn.linear_model import LinearRegression;

#数据清洗函数定义区
def outlier_test(data,column,method=None,z=2):
    '''上下截断点法检测异常值'''
    '''
    full_data:完整数据
    column:full_data中的指定行;
    outlier:异常值数据框
    upper:上截断点
    lower:下截断点
    method:None即为默认的上下截断点法
    '''
    if method==None:
        print(f'以{column}列为依据，使用上下截断点法检测异常值')
        print('='*70)
        column_iqr=np.quantile(data[column],0.75)-np.quantile(data[column],0.25)
        (q1,q3)=np.quantile(data[column],0.25),np.quantile(data[column],0.75)
        upper,lower=(q3+1.5*column_iqr),(q1-1.5*column_iqr)
        outlier=data[(data[column]<=lower)|(data[column]>=upper)]
        print(f'第一分位数:{q1},第三分位数:{q3},四分位极差:{column_iqr}')
        print(f'上截断点:{upper},下截断点:{lower}')
        return outlier,upper,lower
    if method=='z':
        print(f'以{column}列为依据,使用Z分数法,z分位数取{z}来检测异常值')
        print('=' * 70)
        mean,std=np.mean(data[column]),np.std(data[column])
        upper,lower=(mean+z*std),(mean-z*std)
        print(f'取{z}个Z分数,大于{upper}或者小于{lower}的被视为异常值')
        print('='*70)
        outlier=data[(data[column]<=lower)|(data[column]>=upper)]
        return outlier,upper,lower

#读取文件
df=pd.read_csv('house_prices.csv')
df.info()#显示列名，数据类型
df.head(6)#显示前6行（默认5行）

#数据清洗
outlier,upper,lower=outlier_test(data=df,column='price',method='z')
outlier.info();outlier.sample(5)
df.drop(index=outlier.index,inplace=True)

#取出自变量，因变量
data_x=df[['area','bedrooms','bathrooms']]
data_y=df['price']

#多元线性回归
model=LinearRegression()
l_model=model.fit(data_x,data_y)
print('参数权重')
print(model.coef_)
print('模型截距')
print(model.intercept_)


