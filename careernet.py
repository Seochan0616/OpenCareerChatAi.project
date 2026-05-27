import requests
import streamlit as st

CAREERNET_API_KEY = st.secrets["CAREERNET_API_KEY"]

def search_job(keyword):
url = "https://www.career.go.kr/cnet/openapi/getOpenApi"

```
params = {
    "apiKey": CAREERNET_API_KEY,
    "svcType": "api",
    "svcCode": "JOB",
    "contentType": "json",
    "gubun": "job_nm",
    "searchJobNm": keyword
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    jobs = []

    if "dataSearch" in data:
        for item in data["dataSearch"]["content"]:

            name = item.get("job_nm", "정보 없음")
            summary = item.get("summary", "설명 없음")

            jobs.append({
                "name": name,
                "summary": summary
            })

    return jobs

except Exception as e:
    return [{
        "name": "오류",
        "summary": str(e)
    }]
```
