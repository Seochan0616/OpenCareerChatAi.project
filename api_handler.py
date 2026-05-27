import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def get_ai_response(prompt):

```
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

try:

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]

except Exception as e:

    return f"오류 발생: {str(e)}"
```
