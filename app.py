from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import configparser
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import requests
import os

# 读取 config.ini 文件
config = configparser.ConfigParser()
config.read('config.ini')
azure_endpoint = config['AzureOpenAI']['azure_endpoint']
api_key = config['AzureOpenAI']['api_key']
api_version = config['AzureOpenAI']['api_version']

print("azure_endpoint : " + azure_endpoint)

# Flask 設定
app = Flask(__name__)
CORS(app) 

###################AzureOpenAI#######################################
from openai import AzureOpenAI
client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key ,
        api_version=api_version,
    )

#####################################################################
    
from metagen import *
import pandas as pd
from tools import tools_content
from custom_prompt import *
from ppt_write import *
with open('datafile/liver_medical_data_dictionary.md', 'r', encoding='utf-8') as f:
    md_content = f.read()  
with open('datafile/DA2 instruct.md', 'r', encoding='utf-8') as f: #數據分析報告格式
    report_content = f.read()

functions=tools_content

p1 = InterProject(project_name='測試項目', part_name='json文檔',upload_to_google_drive =True)
report = InterProject(project_name='測試項目', part_name='分析報告文檔',upload_to_google_drive =True)
print(p1.folder_id)

mategen_test = MateGen(api_key = api_key,      # 设置api_key
                    system_content_list=[md_content,report_content],
                    model ="4o_nita_20240702",           # 设置模型
                    available_functions=AvailableFunctions(functions_list=[sql_inter,extract_data,python_inter,fig_inter],functions=functions, function_call="auto")
                    ,project=p1,
                    #is_enhanced_mode=True
                    )

mategen_report = MateGen(api_key = api_key,      # 设置api_key
                    system_content_list=[md_content,report_content],
                    model ="4o_nita_20240702",           # 设置模型
                    available_functions=AvailableFunctions(functions_list=[sql_inter,extract_data,python_inter,fig_inter],functions=functions, function_call="auto")
                    ,project=report)

def append_doc_googledrive(folder_id=report.folder_id, doc_id=report.doc_id, dict_string=""):
    rep=''
    for j in dict_string:
         if j['role']=='assistant':
            rep=rep+j['content']+'\n'
    creds = Credentials.from_authorized_user_file('token.json')
    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    # 獲取文檔的當前长度
    document = docs_service.documents().get(documentId=doc_id).execute()
    end_of_doc = document['body']['content'][-1]['endIndex'] - 1  
    # 追加内容到文檔
    requests = [{
            'insertText': {
                'location': {'index': end_of_doc},
                'text': rep + '\n\n'   # 格式
            }
        }]
    docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
##########################################################################
# 确保 recording 目录存在
if not os.path.exists('recording'):
    os.makedirs('recording')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['filename']
    if file :  
        os.makedirs('./data' ,exist_ok=True)
        file.save(os.path.join('./data', file.filename))
        print('更新')
    else:
        errorMsg='僅允許上傳excel檔案'
    return render_template('index.html')




@app.route('/dashboard')
def dashboard():
    
    test_b = pd.read_excel("data/data.xlsx",sheet_name='B肝帶原')
    test_c = pd.read_excel("data/data.xlsx",sheet_name='C肝帶原')
    test_bc = pd.read_excel("data/data.xlsx",sheet_name='B+C肝帶原')

    def convert_to_percentage(decimal):
        """Converts a decimal value to a percentage string."""
        return f"{decimal * 100:.1f}%"

    lenb=len(test_b['狀態'])
    lenc=len(test_c['狀態'])
    lenbc=len(test_bc['狀態'])

    b_transfer = test_b['狀態'].value_counts().get('轉出',0)
    c_transfer = test_c['狀態'].value_counts().get('轉出',0)
    bc_transfer = test_bc['狀態'].value_counts().get('轉出',0)

    total_patient = lenb+lenc+lenbc
    total_trnasfer = b_transfer+c_transfer+bc_transfer
    total_transfer_rate = (total_trnasfer)/(total_patient)
    total_transfer_rate_per = convert_to_percentage(total_transfer_rate)
    str_total_transfer = f"{total_trnasfer}/{total_transfer_rate_per}" 
    

    b_close = test_b['狀態'].value_counts().get('轉出結案',1)
    c_close = test_c['狀態'].value_counts().get('轉出結案',1)
    bc_close = test_bc['狀態'].value_counts().get('轉出結案',1)
    
    total_close = b_close+c_close+bc_close
    total_close_rate = (total_close)/(total_patient)
    total_close_rate_per = convert_to_percentage(total_close_rate)
    str_total_close = f"{total_close}/{total_close_rate_per}"
    global numeric_prompt
    numeric_prompt=numeric_prompt.format(total_patient,lenb,lenc,lenbc,total_trnasfer,total_close
                                         ,'400人，佔整體比例的10%。這可能是因為多種原因造成的，例如對治療效果不滿意或交通不便。','1200人。這表明有相當一部分患者需要頻繁檢查來監控病情。','800人。這部分患者可能因年齡增加而面臨較高的肝病風險，需要特別關注。','3:2 B肝患者有2000人。這表明男性患B肝的比例高於女性。另外，B+C肝患者中，男女比例也是3:2。男性占60%，女性占40%，反映了性別在肝病中的差異。')
    print(numeric_prompt)
    return render_template('dashboard.html',totalPatients = total_patient, bPatients = lenb, cPatients = lenc, bcPatients = lenbc, transferredCases = str_total_transfer,closedCases =str_total_close)


@app.route('/talk')
def talk():
    return render_template('talk.html')

@app.route('/dialogue')
def dialogue():
    try:
        message = "這是對話頁面的一個消息"
        return render_template('dialogue.html', message=message)
    except Exception as e:
        print(f"Error rendering dialogue.html: {e}")
        return str(e), 500

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('userMessage')

    # 如果不在知識庫中   如果在知識庫
    try:
        #mategen_test.chat(question=user_message)
        #mategen_test.upload_messages()
        #print(mategen_test.messages.history_messages[-1]['content'])
        #append_doc_googledrive(folder_id=report.folder_id, doc_id=report.doc_id, dict_string=mategen_test.messages.history_messages)
        print(numeric_prompt)
        completion = client.chat.completions.create(
            model="4o_nita_20240702",  
            messages=[{"role": "system", "content": precise_prompt.format(mategen_test.messages.history_messages[-1]['content']+';'+numeric_prompt)}
                      ,{"role": "user", "content":user_message}
                    ],
            temperature=0.2,
            top_p=0.90,
        )
        response_text = completion.choices[0].message.content
        return jsonify({"response": str(response_text)})
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return jsonify({"error": "Connection error. Please check your network and API settings."}), 500
    except Exception as e:
        print(f"Unexpected error in send_message: {e}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    
speech_key = "3ba2bb6bb2f64851bdba65756efa5b2b"
service_region = "eastus"

# 新增語音轉文字和 GPT 回覆 API 端點
@app.route('/api/speech_to_text', methods=['POST'])
def speech_to_text():
    global speech_key, service_region 
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    
    # Convert audio to WAV format
    audio = AudioSegment.from_file(audio_file.stream)
    output_path = os.path.abspath(os.path.join('recording', 'recording.wav'))
    
    # 刪除先前的錄音文件
    if os.path.exists(output_path):
        os.remove(output_path)
    
    audio.export(output_path, format="wav", codec="pcm_s16le")
    
    if not os.path.isfile(output_path):
        return jsonify({"error": "Failed to save audio file"}), 500
        
    try:
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        audio_input = speechsdk.AudioConfig(filename=output_path)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        
        result = speech_recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            user_text = result.text
        else:
            return jsonify({"error": "Speech not recognized"}), 400
        
        # 重置 audio_input 和 speech_recognizer
        audio_input = None
        speech_recognizer = None
    except Exception as e:
        print(f"Error during speech recognition: {e}")  # 打印详细错误信息
        return jsonify({"error": "Failed to recognize speech"}), 500


    completion = client.chat.completions.create(
        model="4o_nita_20240702",  
        messages=[{"role": "system", "content": voice_prompt.format(numeric_prompt)},
                  {"role": "user", "content": user_text}],
        temperature=0.2,
        top_p=0.90,
    )
    response_text = completion.choices[0].message.content
    print(response_text)
    
    # 生成語音回覆前刪除先前的回覆音頻文件
    audio_response_path = os.path.join('recording', 'response.wav')
    if os.path.exists(audio_response_path):
        os.remove(audio_response_path)

    # 生成語音回覆
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaoxiaoNeural"
    # audio_response_path = os.path.join('recording', 'response.wav')
    audio_config = speechsdk.AudioConfig(filename=audio_response_path)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(response_text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return jsonify({"response_text": response_text, "audio_file": "response.wav"}), 200
    else:
        return jsonify({"error": "Failed to synthesize speech"}), 500


@app.route('/recording/<filename>', methods=['GET'])
def get_audio_file(filename):
    return send_from_directory('recording', filename)



@app.route('/report_download', methods=['POST'])
def report_download():
    '''更新報告
    report_message = report.get_doc_content()     
    message_text = [
        {"role": "system", "content": report_prompt.format(report_message+'\n'+numeric_prompt)},
        {"role": "user", "content": '請給出結論'}
    ]

    completion = client.chat.completions.create(
        model="4o_nita_20240702",  
        messages=message_text,
        temperature=0.2,
        top_p=0.90,
    )
    response_text = completion.choices[0].message.content
    print(response_text)
    '''
    # 將報告文檔下載到本地
    os.system('python ppt_write.py')
    #上傳到 Google Drive
    from googleapiclient.http import MediaFileUpload
    creds = Credentials.from_authorized_user_file('token.json')
    drive_service = build('drive', 'v3', credentials=creds)
    file_path = '本月肝炎個管成效.pptx'
    file_name = '本月肝炎個管成效.pptx'
    ##############創建媒体文件上傳對象############################################
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path, mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    file =  drive_service.files().create(body=file_metadata, media_body=media, fields='id,webContentLink').execute()
    ################開啟網頁############################################################
    #import webbrowser
    #webbrowser.open(file["webContentLink"])
    return send_from_directory('', '本月肝炎個管成效.pptx', as_attachment=True)
   



if __name__ == "__main__":
    app.run(port=5000)
