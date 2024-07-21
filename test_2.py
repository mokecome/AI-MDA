import litellm
# azure call
response = litellm.completion(
    model = "azure/4o_nita_20240702",             # model = azure/<your deployment name> 
    api_base ='https://openai-nita-20240702.openai.azure.com',                                      # azure api base
    api_version = '2024-02-15-preview',                                   # azure api version
    api_key = '0ca06086f7b54085adbb541d3e16da10',                                       # azure api key
    messages = [{"role": "user", "content": "'C:/Users/User/Desktop/copilot/AI-MDA/data/data.xlsx',這個數據集各列代表什麼?"}],
)
print(response.choices[0].message.content)


from interpreter import interpreter
interpreter.offline = True
interpreter.llm.model = "ollama/gemma2:latest"
interpreter.llm.api_base = "http://localhost:11434"

interpreter.chat("how many files are on my desktop?")
