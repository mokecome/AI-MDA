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
with open('datafile/liver_medical_data_dictionary.md', 'r', encoding='utf-8') as f:
    md_content = f.read()  
with open('datafile/DA2 instruct.md', 'r', encoding='utf-8') as f: #數據分析報告格式
    report_content = f.read()

functions=tools_content

p1 = InterProject(project_name='測試項目', part_name='測試文檔',upload_to_google_drive =True)
print(p1.folder_id)
last_message = p1.get_doc_content()
if last_message == '':
    #agent實例
    mategen_test = MateGen(api_key = api_key,      # 设置api_key
                    system_content_list=[md_content,report_content],
                    model ="4o_nita_20240702",           # 设置模型
                    available_functions=AvailableFunctions(functions_list=[sql_inter,extract_data,python_inter,fig_inter],functions=functions, function_call="auto")
                    ,project=p1)
else:
    mategen_test = MateGen(api_key = api_key,      # 设置api_key
                    system_content_list=[md_content,report_content],
                    model ="4o_nita_20240702",           # 设置模型
                    available_functions=AvailableFunctions(functions_list=[sql_inter,extract_data,python_inter,fig_inter],functions=functions, function_call="auto")
                    ,project=p1, 
                    messages=last_message,
                    #,is_enhanced_mode=True
                    )

##########################################################################
# 确保 recording 目录存在
if not os.path.exists('recording'):
    os.makedirs('recording')

@app.route('/')
def index():
    return render_template('index.html')

'''
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['filename']
    if file :   # 確認有檔案'
        os.makedirs('./' ,exist_ok=True)
        #檢查當前目錄下的文件是否有相同文件名，如果有，比較是否內容相同，如果相同，刪除舊文件
        df = pd.read_excel('./'+file.filename)
        file.save(os.path.join('./', file.filename))
        print('更新')
    else:
        errorMsg='僅允許上傳excel檔案'
    #返回文件
    try:
        #讀取資料夾名為filename的文件
        #filename = request.args.get('filename')
        df2 = pd.read_excel('data/data.xlsx')
        if not df.equals(df2):
            p1.clear_content()
            for q in ['請幫我介紹telco_db數據庫的資料表','接下來請圍繞已經讀取到Python環境中的表來進行字段類型的設置，請根據每個字段的業務解釋
            ，來調整字段類型。若要調整字段類型，直接在原始表格上進行修改即可。'
            ,'分析telco_db数据库中的表，帮我梳理一个数据分析的基本思路','請幫我產生一個數據分析報告']:
                mategen_test.chat(question=q)
            mategen_test.upload_messages()

        df.to_excel('data/data.xlsx',index=False)

    except:
        pass
'''  


@app.route('/dashboard')
def dashboard():
    df = pd.read_excel('data.xlsx')
    #資料清整
    df = df.drop_duplicates()
    return render_template('dashboard.html')

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
    print("user_message : " + user_message)

    # 如果不在知識庫中   如果在知識庫
    try:
        mategen_test.chat(question=user_message)
        mategen_test.upload_messages()
        print(mategen_test.messages.history_messages[-1]['content'])
        return jsonify({"response": str(mategen_test.messages.history_messages[-1]['content'])})
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


    # 调用 Azure OpenAI API 进行文本处理
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version
    )
    #report_prompt  
    last_message = p1.get_doc_content()
    message_text = [
        {"role": "system", "content": "你是一個善於數據分析的專家。請根據以下內容生成合適的回應。"+last_message},
        {"role": "user", "content": user_text}
    ]

    completion = client.chat.completions.create(
        model="4o_nita_20240702",  
        messages=message_text,
        temperature=0.7,
        max_tokens=1500,
        top_p=0.90,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
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

if __name__ == "__main__":
    app.run(port=5000)
