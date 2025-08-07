
import requests, base64

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = False


headers = {
  "Authorization": "Bearer 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",
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "model": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
  "messages": [{"role":"user","content":"Qual o nome do 1º presidente do Brasil ?"}],
  "max_tokens": 512,
  "temperature": 1.00,
  "top_p": 1.00,
  "frequency_penalty": 0.00,
  "presence_penalty": 0.00,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
