from interpreter import interpreter
interpreter.offline = True
interpreter.llm.model = "ollama/gemma2:latest"
interpreter.llm.api_base = "http://localhost:11434"

with open('datafile/liver_medical_data_dictionary.md', 'r', encoding='utf-8') as f:
    md_content = f.read()  

interpreter.chat(md_content)
interpreter.chat(" C:\Users\User\Desktop\copilot\AI-MDA\data\B.xlsx 這個數據集各列代表是什麼?")
