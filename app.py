import random
import string
import json
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="@NGYT777GG 🚀")


def generate_phpsessid(length=26):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


@app.get("/")
async def home():
    return {
        "message": "Welcome to @NGYT777GG EMAIL API 🚀",
        "usage": "/lookup?email=example@gmail.com"
    }


@app.get("/lookup")
async def lookup(request: Request):
    email = request.query_params.get("email")
    if not email:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing ?email= parameter"}
        )

    fake_session_id = generate_phpsessid()
    payload = {
        "field": [
            {"email": email}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://osintdog.com",
        "Referer": "https://osintdog.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Cookie": f"PHPSESSID={fake_session_id}",
        "Sec-Ch-Ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Priority": "u=1, i"
    }

    try:
        response = requests.post(
            "https://osintdog.com/api_proxy.php",
            headers=headers,
            data=json.dumps(payload),
            verify=False
        )
        data = response.json()

        # Apply replacements like PHP
        if 'performance' in data and data['performance'].get('mode') == 'emergency':
            data['performance']['mode'] = 'balanced'
        if 'results' in data and 'emergency' in data['results']:
            emergency = data['results']['emergency']
            if emergency.get('status') == 'emergency_mode':
                emergency['status'] = 'normal take down'
            if emergency.get('message') == 'All primary services temporarily unavailable':
                emergency['message'] = 'rate limit please wait and try again'

        return JSONResponse(content=data, status_code=response.status_code)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
