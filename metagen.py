import os
import copy
import glob
from io import BytesIO
import shutil
from openai import APIConnectionError
import time
import tiktoken
import pandas as pd
import json
import pymysql
import os.path
import matplotlib
import warnings
warnings.filterwarnings("ignore")
#郵件相關套件
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseUpload
import base64
import email
from email import policy
from email.parser import BytesParser
from email.mime.text import MIMEText
os.environ['SSL_VERSION'] = 'TLSv1_2'

from openai import AzureOpenAI

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
azure_endpoint = config['AzureOpenAI']['azure_endpoint']
api_key = config['AzureOpenAI']['api_key']
api_version = config['AzureOpenAI']['api_version']

client = AzureOpenAI(
  azure_endpoint = azure_endpoint, 
  api_key=api_key,
  api_version=api_version,
)

def create_or_get_folder(folder_name, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)


        # 查詢是否已存在該文件夾名
        query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false"
        results = drive_service.files().list(q=query).execute()
        items = results.get('files', [])

        if not items:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = drive_service.files().create(body=folder_metadata).execute()
            folder_id = folder['id']
        else:
            folder_id = items[0]['id']
        
    else:
        # folder_id
        folder_path = os.path.join('./', folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        folder_id = folder_path
        
    return folder_id

def create_or_get_doc(folder_id, doc_name, upload_to_google_drive=False): 
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)
        docs_service = build('docs', 'v1', credentials=creds)


        query = f"name='{doc_name}' and '{folder_id}' in parents"
        results = drive_service.files().list(q=query).execute()
        items = results.get('files', [])


        if not items:
            doc_metadata = {
                'name': doc_name,
                'mimeType': 'application/vnd.google-apps.document',
                'parents': [folder_id]
            }
            doc = drive_service.files().create(body=doc_metadata).execute()
            document_id = doc['id']
        else:
            document_id = items[0]['id']
            

    else: 
        file_path = os.path.join(folder_id, f'{doc_name}.md')
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('') 
        document_id = file_path
        
    return document_id

def get_file_content(file_id, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        service = build('drive', 'v3', credentials=creds)
        os.environ['SSL_VERSION'] = 'TLSv1_2'
        request = service.files().export_media(fileId=file_id, mimeType='text/plain')
        content = request.execute()
        decoded_content = content.decode('utf-8')
        
    else:
        with open(file_id, 'r', encoding='utf-8') as file:
            decoded_content = file.read()
    return decoded_content

def append_content_in_doc(folder_id, doc_id, dict_list, upload_to_google_drive=False):
    # 將字典列表轉換為JSON字符串
    json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)
        docs_service = build('docs', 'v1', credentials=creds)

        # 獲取文檔的當前长度
        document = docs_service.documents().get(documentId=doc_id).execute()
        end_of_doc = document['body']['content'][-1]['endIndex'] - 1  
        #修改產生格式
        report=''
        for j in dict_list:
             if j['role']=='assistant':
                 report=report+j['content']+'\n'
        # 追加Q-A内容到文檔
        requests = [{
            'insertText': {
                'location': {'index': end_of_doc},
                'text': report + '\n\n'   # 格式
            }
        }]
        docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        
    else:
        with open(doc_id, 'a', encoding='utf-8') as file:
            file.write(json_string)  # 追加JSON字符串
            
def clear_content_in_doc(doc_id, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        docs_service = build('docs', 'v1', credentials=creds)

        # 文檔長度
        document = docs_service.documents().get(documentId=doc_id).execute()
        end_of_doc = document['body']['content'][-1]['endIndex'] - 1

        # 創建删除内容的請求
        requests = [{
            'deleteContentRange': {
                'range': {
                    'startIndex': 1,  # 文檔的開始位置
                    'endIndex': end_of_doc  # 文檔的结束位置
                }
            }
        }]

        # 執行删除内容的請求
        docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        
    # 清除本地内容
    else:
        with open(doc_id, 'w') as file:
            pass  
        
def list_files_in_folder(folder_id, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)

        # 列出文件夹中的所有文件
        query = f"'{folder_id}' in parents"
        results = drive_service.files().list(q=query).execute()
        files = results.get('files', [])

        # 返回文件名列表
        file_names = [file['name'] for file in files]
        
    # 文件夹内文件
    else:
        file_names = [f for f in os.listdir(folder_id) if os.path.isfile(os.path.join(folder_id, f))]
    return file_names

def rename_doc_in_drive(folder_id, doc_id, new_name, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)

        # 创建更新请求以更改文档名称
        update_request_body = {
            'name': new_name
        }

        # 發送更新请求
        update_response = drive_service.files().update(
            fileId=doc_id,
            body=update_request_body,
            fields='id,name'
        ).execute()

        # 返回更新后的文檔信息，包括ID和新名称
        update_name = update_response['name']
        
    # 若修改本地文檔名稱
    else:
        # 分解原始路徑
        directory, old_file_name = os.path.split(doc_id)
        extension = os.path.splitext(old_file_name)[1]

        #组合新路徑
        new_file_name = new_name + extension
        new_file_path = os.path.join(directory, new_file_name)

        # 重命名文件
        os.rename(doc_id, new_file_path)
        
        update_name=new_name
    
    return update_name

def delete_all_files_in_folder(folder_id, upload_to_google_drive=False):
    if upload_to_google_drive:
        creds = Credentials.from_authorized_user_file('token.json')
        drive_service = build('drive', 'v3', credentials=creds)

        # 列出文件夾中的所有文件
        query = f"'{folder_id}' in parents"
        results = drive_service.files().list(q=query).execute()
        files = results.get('files', [])

        # 删除每個文件
        for file in files:
            file_id = file['id']
            drive_service.files().delete(fileId=file_id).execute()
            # print(f"Deleted file: {file['name']} (ID: {file_id})")
       
    else:
        for filename in os.listdir(folder_id):
            file_path = os.path.join(folder_id, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
                
class InterProject():
    def __init__(self, 
                 project_name, 
                 part_name, 
                 folder_id = None, 
                 doc_id = None, 
                 doc_content = None, 
                 upload_to_google_drive = False):
        
        # 文件夾名稱
        self.project_name = project_name
        self.part_name = part_name
        self.upload_to_google_drive = upload_to_google_drive
        
        # 若文件夾ID為空，則獲取文件夾ID
        if folder_id == None:
            folder_id = create_or_get_folder(folder_name=project_name,
                                             upload_to_google_drive = upload_to_google_drive)
        self.folder_id = folder_id
        
        # 創建或獲取文件ID其他文件名稱列表
        self.doc_list = list_files_in_folder(folder_id, 
                                             upload_to_google_drive = upload_to_google_drive)
        
   
        # 若項目文件ID為空，獲取或創建文件ID
        if doc_id == None:
            doc_id = create_or_get_doc(folder_id=folder_id, 
                                       doc_name=part_name, 
                                       upload_to_google_drive = upload_to_google_drive)
        self.doc_id = doc_id
        
        # doc具体内容，相當於多輪对话内容
        self.doc_content = doc_content
        # 若初始content不空，則將其追加入文檔内
        if doc_content != None:
            append_content_in_doc(folder_id=folder_id, 
                                  doc_id=doc_id, 
                                  qa_string=doc_content, 
                                  upload_to_google_drive = upload_to_google_drive)
            

    def get_doc_content(self):
        self.doc_content = get_file_content(file_id=self.doc_id, 
                                            upload_to_google_drive = self.upload_to_google_drive)

        return self.doc_content
    

    def append_doc_content(self, content):
        append_content_in_doc(folder_id=self.folder_id, 
                              doc_id=self.doc_id, 
                              dict_list=content, 
                              upload_to_google_drive = self.upload_to_google_drive)
    
    def clear_content(self):
        clear_content_in_doc(doc_id=self.doc_id, 
                             upload_to_google_drive = self.upload_to_google_drive)
        
    def delete_all_files(self):
        delete_all_files_in_folder(folder_id=self.folder_id, 
                                   upload_to_google_drive = self.upload_to_google_drive)
        
    def update_doc_list(self):
        self.doc_list = list_files_in_folder(self.folder_id, 
                                             upload_to_google_drive = self.upload_to_google_drive)
    
    def rename_doc(self, new_name):
        self.part_name = rename_doc_in_drive(folder_id=self.folder_id, 
                                             doc_id=self.doc_id, 
                                             new_name=new_name, 
                                             upload_to_google_drive = self.upload_to_google_drive)
        

    
 
    

        
class ChatMessages():
    def __init__(self, 
                 system_content_list=[], 
                 question='',
                 tokens_thr=None, 
                 project=None):

        self.system_content_list = system_content_list
        system_messages = []
        history_messages = []
        #用於保存全部消息的list
        messages_all = []
        #系統消息字串
        system_content = ''
        # 歷史消息字串，此時為用戶輸入資訊
        history_content = question
        # 系統消息 + 歷史消息字串
        content_all = ''
        # 輸入到 messages 中系統消息個數，初始情況為 0
        num_of_system_messages = 0
        all_tokens_count = 0
        
        encoding = tiktoken.encoding_for_model("gpt-4")
        
    
        if system_content_list != []:      
            for content in system_content_list:
                system_messages.append({"role": "system", "content": content})
                # 拼接
                system_content += content
                
            # 系统消息token
            system_tokens_count = len(encoding.encode(system_content))
            # 拼接
            messages_all += system_messages
            # 計算系统消息個數
            num_of_system_messages = len(system_content_list)
                
           
            if tokens_thr != None:
                if system_tokens_count >= tokens_thr:
                    print("system_messages 的 tokens 數量超出限制，當前系統消息將不會被輸入模型，若有必要，請重新調整外部文檔數量。")            
                    # 删除系统消息
                    system_messages = []
                    messages_all = []
                    # 系统消息個数清零
                    num_of_system_messages = 0
                    # 系统消息token数清零
                    system_tokens_count = 0
                    
            all_tokens_count += system_tokens_count
        
        # 創建首次對话消息
        if question != '':
            history_messages = [{"role": "user", "content": question}]
        # 創建全部消息列表
        messages_all += history_messages
        user_tokens_count = len(encoding.encode(question))
        
        # 計算總token數
        all_tokens_count += user_tokens_count
        

        if tokens_thr != None:
            if all_tokens_count >= tokens_thr:
                print("當前使用者問題的 tokens 數量超出限制，該訊息無法被輸入到模型中，請重新輸入使用者問題或調整外部文件數量。")  
                # 同时清空
                history_messages = []
                system_messages = []
                messages_all = []
                num_of_system_messages = 0
                all_tokens_count = 0
        
        # 全部messages信息
        self.messages = messages_all
        self.system_messages = system_messages
        self.history_messages = history_messages
        # messages信息中全部content的token数量
        self.tokens_count = all_tokens_count
        # 系统信息数量
        self.num_of_system_messages = num_of_system_messages
        self.tokens_thr = tokens_thr
        self.encoding = tiktoken.encoding_for_model("gpt-4")
        self.project = project
     
    def messages_pop(self, manual=False, index=None):
        def reduce_tokens(index):
            drop_message = self.history_messages.pop(index)
            self.tokens_count -= len(self.encoding.encode(str(drop_message)))

        if self.tokens_thr is not None:
            while self.tokens_count >= self.tokens_thr:
                reduce_tokens(-1)

        if manual:
            if index is None:
                reduce_tokens(-1)
            elif 0 <= index < len(self.history_messages) or index == -1:
                reduce_tokens(index)
            else:
                raise ValueError("Invalid index value: {}".format(index))

        # 更新messages
        self.messages = self.system_messages + self.history_messages
       

    def messages_append(self, new_messages):
        # 若新消息也是ChatMessages對象
        if isinstance(new_messages, ChatMessages):
            self.messages += new_messages.messages
            self.tokens_count += new_messages.tokens_count
        # 若是單獨一个字典，或JSON格式字典
        elif type(new_messages) is dict:
            self.messages.append(new_messages)
            self.tokens_count += len(self.encoding.encode(str(new_messages)))
        elif type(new_messages.content) is str:
            self.messages.append({'role':new_messages.role,'content':new_messages.content})
            self.tokens_count += len(self.encoding.encode(str(new_messages)))



        print(self.history_messages)    
        # 重新更新history_messages
        self.history_messages = self.messages[self.num_of_system_messages: ]
        # 再執行pop，若有需要，則會删除部分歷史消息
        self.messages_pop()
      
    def copy(self):
        system_content_str_list = [message['content'] for message in self.system_messages]
        new_obj = ChatMessages(
            system_content_list=copy.deepcopy(system_content_str_list),  # 使用深複製来複製系统消息
            question=self.history_messages[0]['content'] if self.history_messages else '',
            tokens_thr=self.tokens_thr
        )
        new_obj.history_messages = copy.deepcopy(self.history_messages)  
        new_obj.messages = copy.deepcopy(self.messages) 
        new_obj.tokens_count = self.tokens_count
        new_obj.num_of_system_messages = self.num_of_system_messages
        
        return new_obj
    
    # 增加系统消息
    def add_system_messages(self, new_system_content):
        system_content_list = self.system_content_list
        system_messages = []
        # 若是字符串，則將其轉化为list
        if type(new_system_content) == str:
            new_system_content = [new_system_content]
            
        system_content_list.extend(new_system_content)
        new_system_content_str = ''
        for content in new_system_content:
            new_system_content_str += content
        new_token_count = len(self.encoding.encode(str(new_system_content_str)))
        self.tokens_count += new_token_count
        self.system_content_list = system_content_list
        for message in system_content_list:
            system_messages.append({"role": "system", "content": message})
        self.system_messages = system_messages
        self.num_of_system_messages = len(system_content_list)
        self.messages = system_messages + self.history_messages
        
        # 再執行pop，若有需要，则會删除部分歷史消息
        self.messages_pop()
        
        
    # 删除系统消息
    def delete_system_messages(self):
        system_content_list = self.system_content_list
        if system_content_list != []:
            system_content_str = ''
            for content in system_content_list:
                system_content_str += content
            delete_token_count = len(self.encoding.encode(str(system_content_str)))
            self.tokens_count -= delete_token_count
            self.num_of_system_messages = 0
            self.system_content_list = []
            self.system_messages = []
            self.messages = self.history_messages
     
    # 清除對話消息中的function消息
    def delete_function_messages(self):
        # 用於删除外部函数消息
        history_messages = self.history_messages
        # 以後向前迭代列表
        for index in range(len(history_messages) - 1, -1, -1):
            message = history_messages[index]
            if message.function_call or message.role == "function":
                self.messages_pop(manual=True, index=index)
                
def sql_inter(sql_query, g='globals()'):
    """
    用於執行一段SQL代碼，並最終獲取SQL代碼執行結果，\
    核心功能是將輸入的SQL代碼傳輸至MySQL環境中進行運行，\
    並最終返回SQL代碼運行結果。需要注意的是，本函數是藉助pymysql來連接MySQL數據庫。
    :param sql_query: 字元串形式的SQL查詢語句，用於執行對MySQL中telco_db數據庫中各張表進行查詢，並獲得各表中的各類相關信息
    :param g: g，字元串形式變量，表示環境變量，無需設定，保持默認參數即可
    :return：sql_query在MySQL中的運行結果。
    """
    connection = pymysql.connect(
            host=config['MySQL']['host'],  # 數據庫地址
            user=config['MySQL']['user'],  # 數據庫用戶名
            passwd=config['MySQL']['mysql_pw'],  # 數據庫密碼
            db=config['MySQL']['db'],  # 數據庫名
            charset='utf8'  # 字元集選擇utf8
        )
    
    try:
        with connection.cursor() as cursor:
            # SQL查詢語句
            sql = sql_query
            cursor.execute(sql)

            # 獲取查詢結果
            results = cursor.fetchall()

    finally:
        connection.close()

    return json.dumps(results)#, ensure_ascii=True

def extract_data(sql_query,df_name,g='globals()'):
    """
    藉助 pymysql 將 MySQL 中的某張表讀取並保存到本地 Python 環境中。
    :param sql_query: 字串形式的 SQL 查詢語句，用於提取 MySQL 中的某張表。
    :param df_name: 將 MySQL 資料庫中提取的表格進行本地保存時的變數名，以字串形式表示。
    :param g: g，字串形式變量，表示環境變量，無需設定，保持默認參數即可
    :return：表格讀取和保存結果
    """
    
    connection = pymysql.connect(
            host=config['MySQL']['host'],  # 數據庫地址
            user=config['MySQL']['user'],  # 數據庫用戶名
            passwd=config['MySQL']['mysql_pw'],  # 數據庫密碼
            db=config['MySQL']['db'],  # 數據庫名
            charset='utf8'  # 字元集選擇utf8
        )
    
    
    g[df_name] = pd.read_sql(sql_query, connection)
    
    return "已成功完成 %s 變量創建" % df_name

def python_inter(py_code, g='globals()'):
    """
    專門用於執行非繪圖類python代碼，並獲取最終查詢或處理結果。若是設計繪圖操作的Python代碼，則需要調用fig_inter函數來執行。
    :param py_code: 字元串形式的Python代碼，用於執行對telco_db數據庫中各張數據表進行操作
    :param g: g，字元串形式變量，表示環境變量，無需設定，保持默認參數即可
    :return：代碼運行的最終結果
    """    
    
    global_vars_before = set(g.keys())
    try:
        exec(py_code, g)            
    except Exception as e:
        return f"代碼執行時報錯{e}"
    global_vars_after = set(g.keys())
    new_vars = global_vars_after - global_vars_before
    # 若存在新變量
    if new_vars:
        result = {var: g[var] for var in new_vars}
        return str(result)
    # 若不存在新變量，即有可能是代碼是表達式，也有可能代碼對相同變量重復賦值
    else:
        try:
            # 嘗試如果是表達式，則返回表達式運行結果
            return str(eval(py_code, g))
        # 若報錯，則先測試是否是對相同變量重復賦值
        except Exception as e:
            try:
                exec(py_code, g)
                return "已經順利執行代碼"
            except Exception as e:
                pass
            # 若不是重復賦值，則報錯
            return f"代碼執行時報錯{e}"
        
p1 = InterProject(project_name='測試項目', part_name='測試文檔',upload_to_google_drive =True)        
def upload_image_to_drive(figure, folder_id = p1.folder_id):
    folder_id = folder_id 
    creds = Credentials.from_authorized_user_file('token.json')
    drive_service = build('drive', 'v3', credentials=creds)
    
    # 1. Save image to Google Drive
    buf = BytesIO()
    figure.savefig(buf, format='png')
    buf.seek(0)
    media = MediaIoBaseUpload(buf, mimetype='image/png', resumable=True)
    file_metadata = {
        'name': 'ImageName.png',
        'parents': [folder_id],
        'mimeType': 'image/png'
    }
    image_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id,webContentLink'  # Specify the fields to be returned
    ).execute()
    
    return image_file["webContentLink"]

def fig_inter(py_code, fname, g='globals()'):
    """
    用於執行一段包含可視化繪圖的Python代碼，並最終獲取一個圖片類型對象
    :param py_code: 字元串形式的Python代碼，用於根據需求進行繪圖，代碼中必須包含Figure對象創建過程
    :param fname: py_code代碼中創建的Figure變量名，以字元串形式表示。
    :param g: g，字元串形式變量，表示環境變量，無需設定，保持默認參數即可
    :return：代碼運行的最終結果
    """    
    # 保存當前的後端
    current_backend = matplotlib.get_backend()
    
    # 設定為Agg後端
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    # 創建一個字典，用於存儲本地變量
    local_vars = {"plt": plt, "pd": pd, "sns": sns}
    
    try:
        exec(py_code, g, local_vars)       
    except Exception as e:
        return f"代碼執行時報錯{e}"
    
    # 回復默認後端
    matplotlib.use(current_backend)
    
    # 根據圖片名稱，獲取圖片對象
    fig = local_vars[fname]
    # 上传图片
    try:
        fig_url = upload_image_to_drive(fig)
        res = f"已经成功运行代码，并已将代码创建的图片存储至：{fig_url}"
        
    except Exception as e:
        res = "无法上传图片至谷歌云盘，请检查谷歌云盘文件夹ID，并检查当前网络情况"
        
    print(res)
    return res


##############################################################
class AvailableFunctions():
    def __init__(self, functions_list=[], functions=[], function_call="auto"):
        self.functions_list = functions_list
        self.functions = functions
        self.functions_dic = None
        self.function_call = None
        if functions_list != []:
            self.functions_dic = {func.__name__: func for func in functions_list}
            self.function_call = function_call
            if functions == []:
                print('請編寫工具給 functions')
       
    # 增加外部函數方法，並且同時可以更換外部函數調用規則
    def add_function(self, new_function, function_description=None, function_call_update=None):
        self.functions_list.append(new_function)
        self.functions_dic[new_function.__name__] = new_function
        if function_description == None:
            print('請編寫description給 functions')
        else:
            self.functions.append(function_description)
        if function_call_update != None:
            self.function_call = function_call_update
            
def add_task_decomposition_prompt(messages):
    # 第一個提示示例
    user_question1 = '請問谷歌雲郵箱是什麼？'
    user_message1_content = "現有用戶問題如下：“%s”。為了回答這個問題，總共需要分幾步來執行呢？\
    若無需拆分執行步驟，請直接回答原始問題。" % user_question1
    assistant_message1_content = '谷歌雲郵箱是指Google Workspace（原G Suite）中的Gmail服務，\
    它是一個安全、智能、易用的電子郵箱，有15GB的免費存儲空間，可以直接在電子郵件中接收和存儲郵件。\
    Gmail 郵箱會自動過濾垃圾郵件和病毒郵件，並且可以通過電腦或手機等移動設備在任何地方查閱郵件。\
    您可以使用搜索和標簽功能來組織郵件，使郵件處理更為高效。'

    # 第二個提示示例
    user_question2 = '請幫我介紹下OpenAI。'
    user_message2_content = "現有用戶問題如下：“%s”。為了回答這個問題，總共需要分幾步來執行呢？\
    若無需拆分執行步驟，請直接回答原始問題。" % user_question2
    assistant_message2_content = 'OpenAI是一家開發和應用友好人工智慧的公司，\
    它的目標是確保人工通用智能（AGI）對所有人都有益，以及隨著AGI部署，盡可能多的人都能受益。\
    OpenAI致力在商業利益和人類福祉之間做出正確的平衡，本質上是一家人道主義公司。\
    OpenAI開發了諸如GPT-3這樣的先進模型，在自然語言處理等諸多領域表現出色。'

    # 第三個提示示例
    user_question3 = '圍繞數據庫中的user_payments表，我想要檢查該表是否存在缺失值'
    user_message3_content = "現有用戶問題如下：“%s”。為了回答這個問題，總共需要分幾步來執行呢？\
    若無需拆分執行步驟，請直接回答原始問題。" % user_question3
    assistant_message3_content = '為了檢查user_payments數據集是否存在缺失值，我們將執行如下步驟：\
    \n\n步驟1：使用`extract_data`函數將user_payments數據表讀取到當前的Python環境中。\
    \n\n步驟2：使用`python_inter`函數執行Python代碼檢查數據集的缺失值。'

    # 第四個提示示例
    user_question4 =  '我想尋找合適的缺失值填補方法，來填補user_payments數據集中的缺失值。'
    user_message4_content = "現有用戶問題如下：“%s”。為了回答這個問題，總共需要分幾步來執行呢？\
    若無需拆分執行步驟，請直接回答原始問題。" % user_question4
    assistant_message4_content = '為了找到合適的缺失值填充方法，我們需要執行以下三步：\
    \n\n步驟1：分析user_payments數據集中的缺失值情況。通過查看各欄位的缺失率和觀察缺失值分佈，瞭解其缺失幅度和模式。\
    \n\n步驟2：確定值填補策略。基於觀察結果和特定欄位的性質確定恰當的填補策略，例如使用眾數、中位數、均值或建立模型進行填補等。\
    \n\n步驟3：進行缺失值填補。根據確定的填補策略，執行填補操作，然後驗證填補效果。'
    
    # 在保留原始問題的情況下加入Few-shot
    task_decomp_few_shot = messages.copy()
    task_decomp_few_shot.messages_pop(manual=True, index=-1)
    task_decomp_few_shot.messages_append({"role": "user", "content": user_message1_content})
    task_decomp_few_shot.messages_append({"role": "assistant", "content": assistant_message1_content})
    task_decomp_few_shot.messages_append({"role": "user", "content": user_message2_content})
    task_decomp_few_shot.messages_append({"role": "assistant", "content": assistant_message2_content})
    task_decomp_few_shot.messages_append({"role": "user", "content": user_message3_content})
    task_decomp_few_shot.messages_append({"role": "assistant", "content": assistant_message3_content})
    task_decomp_few_shot.messages_append({"role": "user", "content": user_message4_content})
    task_decomp_few_shot.messages_append({"role": "assistant", "content": assistant_message4_content})
    
    user_question = messages.history_messages[-1]["content"]

    new_question = "現有用戶問題如下：“%s”。為了回答這個問題，總共需要分幾步來執行呢？\
    若無需拆分執行步驟，請直接回答原始問題。" % user_question
    question_message = messages.history_messages[-1].copy()
    question_message["content"] = new_question
    task_decomp_few_shot.messages_append(question_message)
    
    return task_decomp_few_shot


def function_to_call(available_functions, function_call_message):
    """
    根據一條函數調用消息function_call_message，返回一條函數運行結果消息function_response_messages。
    :param available_functions: 必要參數，要求輸入一個AvailableFunctions對象，以說明當前外部函數基本情況
    :param function_call_message: 必要參數，要求輸入一條外部函數調用的message
    :return: function_response_messages，輸出又外部函數運行結果所組成的message
    """
    
    # 獲取調用外部函數的函數名稱
    function_name = function_call_message.function_call.name
    
    # 根據函數名稱獲取對應的外部函數對象
    fuction_to_call = available_functions.functions_dic[function_name]
    
    # 提取function_call_message中調用外部函數的函數參數
    # 即大模型編寫的SQL或者Python代碼
    function_args = json.loads(function_call_message.function_call.arguments)
    
    # 將參數帶入到外部函數中並運行
    try:
        # 將當前操作空間中的全局變量添加到外部函數中
        function_args['g']=globals()
        
        # 運行外部函數
        function_response = fuction_to_call(**function_args)
      
    # 若外部函數運行報錯，則提取報錯信息
    except Exception as e:
        function_response = "函數運行報錯如下:" + str(e)
        #print(function_response)
        
    # 創建function_response_messages
    # 該message包含外部函數順利運行或報錯信息
    
    function_response_messages = {
        "role": "function",
        "name": function_name,
        "content": function_response,
    }
    
    return function_response_messages




def get_gpt_response(model, 
                     messages, 
                     available_functions=None,
                     is_enhanced_mode=False):
        
    if is_enhanced_mode:
        messages = add_task_decomposition_prompt(messages)

    # 考慮到可能存在通信报错问题，因此循環調用Chat模型進行执行
    while True:
        try:
            # 若不存在外部函数
            if available_functions == None:
                response = client.chat.completions.create(
                    model=model,
                    messages=messages.messages)   
                
            # 若存在外部函数，此时functions和function_call参数信息都从AvailableFunctions对象中获取
            else:
                response = client.chat.completions.create(
                    model=model,
                    messages=messages.messages, 
                    functions=available_functions.functions, 
                    function_call=available_functions.function_call
                    )   
            break  # 如果成功获取响应，退出循环
            
        except APIConnectionError as e:
            # APIConnectionError默认是用户需求不清导致无法返回结果
            # 若开启增强模式，此时提示用户重新输入需求
            if is_enhanced_mode:
                # 創建臨时消息列表
                msg_temp = messages.copy()
                # 獲取用戶问题
                question = msg_temp.messages[-1]["content"]
                # 提醒用户修改提问的提示模板
                new_prompt = "以下是用戶提問：%s。該問題有些複雜，且用戶意圖並不清楚。\
                請編寫一段話，來引導用戶重新提問。" % question
                try:
                    msg_temp.messages[-1]["content"] = new_prompt
                    # 修改用戶问题並直接提问
                    response = client.chat.completions.create(
                        model=model,
                        messages=msg_temp.messages)
                    
                    # 打印gpt返回的提示修改原问题的描述语句
                    print(response.choices[0].message.content)
                    user_input = input("請重新輸入問題，输入“退出”可以退出當前對話")
                    if user_input == "退出":
                        print("當前模型無法返回結果，已經退出")
                        return None
                    else:
                        # 修改原始问题
                        messages.history_messages[-1]["content"] = user_input
                        
                        # 再次進行提问
                        response_message = get_gpt_response(model=model, 
                                                            messages=messages, 
                                                            available_functions=available_functions,
                                                            is_enhanced_mode=is_enhanced_mode)
                        
                        return response_message
                except APIConnectionError as e:
                    print(f"當前遇到了一個連結問題: {str(e)}")
                    print("由於Limit Rate限制，即將等待1分鐘後繼續運行...")
                    time.sleep(60)  # 等待1分钟
                    print("已等待60秒，即將開始重新調用模型並進行回答...")
               
            else:        
                # 打印错误的核心信息
                print(f"當前遇到了一個連結問題: {str(e)}")
                print("由於Limit Rate限制，即將等待1分鐘後繼續運行...")
                time.sleep(60)  # 等待1分钟
                print("已等待60秒，即將開始重新調用模型並進行回答..")
        
    return response.choices[0].message

#任務拆解和深度debug(auto_gpt)
def get_chat_response(model, 
                      messages, 
                      available_functions=None,
                      is_enhanced_mode=False, 
                      delete_some_messages=False, 
                      is_task_decomposition=False):
    
    

    # is_task_decomposition=True时，不再重新創建response_message
    if not is_task_decomposition:
        # 先獲取單次大模型調用结果
        # 此时response_message是大模型調用返回的message
        response_message = get_gpt_response(model=model, 
                                            messages=messages, 
                                            available_functions=available_functions,
                                            is_enhanced_mode=is_enhanced_mode)
    
    if is_task_decomposition or (is_enhanced_mode and response_message.function_call):
        is_task_decomposition = True
        # 在拆解任务时，将增加了任务拆解的few-shot-message命名为text_response_messages
        task_decomp_few_shot = add_task_decomposition_prompt(messages)
        # 同时更新response_message，此时response_message就是任务拆解之后的response
        response_message = get_gpt_response(model=model, 
                                            messages=task_decomp_few_shot, 
                                            available_functions=available_functions,
                                            is_enhanced_mode=is_enhanced_mode)
        # 若拆分任务的提示无效，此时response_message有可能会再次创建一个function call message
        if response_message.function_call:
            print("當前任務無需拆解，可以直接運行。")

    # 若本次调用是由修改对话需求产生，则按照参数设置删除原始message中的若干条消息
    # 需要注意的是，删除中间若干条消息，必须在创建完新的response_message之后再执行
    if delete_some_messages:
        for i in range(delete_some_messages):
            messages.messages_pop(manual=True, index=-1)
    
    # 此時，一定會有一個response_message
    # 接下来分response_message不同類型，執行不同流程
    # 若是文本响應类任务（包括普通文本响应和和复杂任务拆解审查两种情况，都可以使用相同代码）
    if not response_message.function_call:
        # 将message保存为text_answer_message
        text_answer_message = response_message 
        messages = is_text_response_valid(model=model, 
                                          messages=messages, 
                                          text_answer_message=text_answer_message,
                                          available_functions=available_functions,
                                          is_enhanced_mode=is_enhanced_mode, 
                                          delete_some_messages=delete_some_messages,
                                          is_task_decomposition=is_task_decomposition)
    
    
    
    # 若是function response任務
    elif response_message.function_call:
        # 創建调用外部函数的function_call_message
        # 在Agent中，function_call_message是一个包含SQL代码或者Python代码的JSON对象
        function_call_message = response_message 
        # 将function_call_message带入代码审查和运行函数is_code_response_valid
        # 并最终获得外部函数运行之后的问答结果
        messages = is_code_response_valid(model=model, 
                                          messages=messages, 
                                          function_call_message=function_call_message,
                                          available_functions=available_functions,
                                          is_enhanced_mode=is_enhanced_mode, 
                                          delete_some_messages=delete_some_messages)
    
    return messages    


def is_code_response_valid(model, 
                           messages, 
                           function_call_message,
                           available_functions=None,
                           is_enhanced_mode=False, 
                           delete_some_messages=False):
    
    # 字符串類型json格式的message對象
    code_json_str = function_call_message.function_call.arguments
    # 將json轉化為字典
    try:
        code_dict = json.loads(code_json_str)
    except Exception as e:
        print("json字符解析錯誤，正在重新創建代碼...")
        # 遞歸调用上層函数get_chat_response，並返回最終message結果
        # 需要注意的是，如果上層函数再次創建了function_call_message
        # 則會再次調用is_code_response_valid，而無需在當前函数中再次执行
        messages = get_chat_response(model=model, 
                                     messages=messages, 
                                     available_functions=available_functions,
                                     is_enhanced_mode=is_enhanced_mode, 
                                     delete_some_messages=delete_some_messages)
        
        return messages
        
    # 若顺利將json轉化為字典，則繼續執行以下代碼
    # 創建convert_to_markdown内部函數，用於輔助打印代碼结果
    def convert_to_markdown(code, language):
        return f"```{language}\n{code}\n```"

    # 提取代碼部分參數
    # 如果是SQL，則按照Markdown中SQL格式打印代碼
    if code_dict.get('sql_query'):
        code = code_dict['sql_query'] 
        markdown_code = convert_to_markdown(code, 'sql')
        print("即將執行以下代碼：")
        
    # 如果是Python，則按照Markdown中Python格式打印代碼
    elif code_dict.get('py_code'):
        code = code_dict['py_code']
        markdown_code = convert_to_markdown(code, 'python')
        print("即將執行以下代碼：")
        
    else:
        markdown_code = code_dict
        
    print(markdown_code)
        
    function_response_message = function_to_call(available_functions=available_functions, 
                                                 function_call_message=function_call_message)  
    

    messages = check_get_final_function_response(model=model, 
                                                 messages=messages, 
                                                 function_call_message=function_call_message,
                                                 function_response_message=function_response_message,
                                                 available_functions=available_functions,
                                                 is_enhanced_mode=is_enhanced_mode, 
                                                 delete_some_messages=delete_some_messages)
    
    return messages


def check_get_final_function_response(model, 
                                      messages, 
                                      function_call_message,
                                      function_response_message,
                                      available_functions=None,
                                      is_enhanced_mode=False, 
                                      delete_some_messages=False):
    
    
    # 獲取外部函數運行结果内容
    fun_res_content = function_response_message["content"]
    
    # 若function_response中包含错误
    if "报错" in fun_res_content or "報錯" in fun_res_content:
        print(fun_res_content)
        debug_prompt_list = ['你編寫的代碼報錯了，請根據報錯資訊修改代碼並重新執行。']
                
        # 此時msg最後一條消息是user message，而不是任何函数调用相關message
        msg_debug = messages.copy()        
        # 追加function_call_message
        # 當前function_call_message中包含编错的代码
        msg_debug.messages_append(function_call_message)
        msg_debug.messages_append(function_response_message)        
        
        #auto_gpt
        for debug_prompt in debug_prompt_list:
            msg_debug.messages_append({"role": "user", "content": debug_prompt})
            print("**From Debug Agent:**")
            print(debug_prompt)
            
            # 打印提示信息
            print("**From MateGen:**")
            msg_debug = get_chat_response(model=model, 
                                          messages=msg_debug, 
                                          available_functions=available_functions,
                                          is_enhanced_mode=False, 
                                          delete_some_messages=delete_some_messages)
        
        messages = msg_debug.copy()     
                 
    # 若function message不包含報错信息    
    # 需要将function message傳遞给模型
    else:
        print("外部函数已执行完畢，正在解析運行结果...")
        messages.messages_append(function_call_message)
        messages.messages_append(function_response_message)
        messages = get_chat_response(model=model, 
                                     messages=messages, 
                                     available_functions=available_functions,
                                     is_enhanced_mode=is_enhanced_mode, 
                                     delete_some_messages=delete_some_messages)
        
    return messages

def is_text_response_valid(model, 
                           messages, 
                           text_answer_message,
                           available_functions=None,
                           is_enhanced_mode=False, 
                           delete_some_messages=False,
                           is_task_decomposition=False):
    
    answer_content = text_answer_message.content
    
    print("模型回答：\n")
    print(answer_content)
    
    messages.messages_append(text_answer_message)

    return messages

class MateGen():
    def __init__(self, 
                 api_key,
                 model='gpt-4', 
                 system_content_list=[],
                 project=None, 
                 messages=None, 
                 available_functions=None,
                 is_enhanced_mode=False):
  
        
        self.api_key = api_key
        self.model = model
        self.project = project
        self.system_content_list = system_content_list
        tokens_thr = None
        
        if '4o' in model:
            tokens_thr = 1100000
        elif '4-0613' in model:
            tokens_thr = 7000
        else:
            tokens_thr = 1100000
            
        self.tokens_thr = tokens_thr
        
        # 創建self.messages屬性
        self.messages = ChatMessages(system_content_list=system_content_list, 
                                     tokens_thr=tokens_thr)
        

        if messages != None:
            self.messages.messages_append(messages)
        
        self.available_functions = available_functions
        self.is_enhanced_mode = is_enhanced_mode
        
    def chat(self, question=None):
        head_str = "▌ Model set to %s" % self.model
        print(head_str)
        self.messages.messages_append({"role": "user", "content": question})
        self.messages = get_chat_response(model=self.model, 
                                          messages=self.messages, 
                                          available_functions=self.available_functions,
                                          is_enhanced_mode=self.is_enhanced_mode)
       
    def reset(self):
        self.messages = ChatMessages(system_content_list=self.system_content_list)
    
    def upload_messages(self):
        if self.project == None:
            print("需要先輸入 project 參數（需要是一個 InterProject 物件），才可上傳 messages")
            return None
        else:
            self.project.append_doc_content(content=self.messages.history_messages)