# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:06:49 2023

@author: mokecome
"""

import pymysql
import pandas as pd
import sqlalchemy

#df插入數據到mysql
class MySQL_CRUD:
    def __init__(self):
        DATABASE_TYPE = "mysql"
        DRIVER = "pymysql"
        USERNAME = "root"
        PASSWORD = "123456"
        HOST = "20.168.12.154"
        PORT = 3306
        DATABASE_NAME = "telco_db"
        engine_url = f"{DATABASE_TYPE}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
        self.engine = sqlalchemy.create_engine(engine_url)
    def insert_df_to_sql(self,df,table_name):
        df.to_sql(table_name,self.engine, if_exists="replace", index=False)
    
if __name__ == '__main__':
    mysql=MySQL_CRUD()
    for name in ['B肝帶原','C肝帶原','B+C肝帶原']:
        df=pd.read_excel('data.xlsx',sheet_name=name)
        mysql.insert_df_to_sql(df,name)

    # 建立连接
    # connection = pymysql.connect(
    #     host='localhost',  # 数据库地址
    #     user='root',  # 数据库用户名
    #     passwd=123456,  # 数据库密码
    #     db='telco_db',  # 数据库名
    #     charset='utf8'  # 字符集选择utf8
    # )
    # cursor = connection.cursor()
    
    # cursor.close()
    
    #数据探索、数据质量校验、数据分析和数据分析报告编写->每个数据分析环节都实时的给与大模型当前最需要的指导信息，从而更好的引导模型分阶段完成每个数据分析环节
    #定制化代码解释器采用的策略是，先让分析师就某个阶段、围绕当前数据集尽可能的提出关键性问题，并审核、总结记录，然后再让大模型根据当前阶段的关键问题问答进行汇总、基于这些关键问题的问答内容来进行本环节的数据分析报告编写。
    #进行多轮对话的过程中，每次大模型的回答结果最好先经过人工验证、再进行本地的记录，从而避免一些错误信息出现。