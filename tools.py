tools_content=[{'name': 'sql_inter',
'description': '用于获取telco_db数据库中各张表的有关相关信息，核心功能是将输入的SQL代码传输至telco_db数据库所在的MySQL环境中进行运行，并最终返回SQL代码运行结果。本函数是借助pymysql来连接MySQL数据库。',
'parameters': {'type': 'object',
 'properties': {'sql_query': {'type': 'string',
   'description': '字符串形式的SQL查询语句，用于执行对MySQL中telco_db数据库中各张表进行查询，并获得各表中的各类相关信息'}},
 'required': ['sql_query']}},
  
  
 {'name': 'extract_data',
'description': '用于借助pymysql，将MySQL中的telco_db数据库中的表读取并保存到本地Python环境中',
'parameters': {'type': 'object',
 'properties': {'sql_query': {'type': 'string',
   'description': '字符串形式的SQL查询语句，用于提取MySQL中telco_db数据库中的某张表'},
  'df_name': {'type': 'string',
   'description': '将MySQL数据库中提取的表格进行本地保存时的变量名'}},
 'required': ['sql_query', 'df_name']}},
  
 {'name': 'python_inter',
'description': '用于对telco_db数据库中各张数据表进行查询和处理，并获取最终查询或处理结果',
'parameters': {'type': 'object',
 'properties': {'py_code': {'type': 'string',
   'description': '用于执行对telco_db数据库中各张数据表进行操作的Python代码'}},
 'required': ['py_code']}},
 
 {'name': 'fig_inter',
'description': '用於執行一段包含可視化繪圖的Python代碼，並最終獲取一個圖片類型對象',
'parameters': {'type': 'object',
 'properties': {'py_code': {'type': 'string',
   'description': '字符串形式的Python代碼，用於根據需求進行繪圖，代碼中必須包含Figure對象創建過程'},
  'fname': {'type': 'string',
   'description': 'py_code代碼中創建的Figure變量名，以字符串形式表示'},
  'g': {'type': 'string', 'description': '字符串形式變量，表示環境變量，無需設定，保持默認參數即可'}},
 'required': ['py_code', 'fname']}}  
]
