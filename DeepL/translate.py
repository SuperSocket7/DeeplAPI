import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()


def translate(text, source_lang, target_lang):
    header = {
        'User-Agent': str(ua.chrome),
        'authority': 'www2.deepl.com',
        'referer': 'https://www.deepl.com/translator',
        'Content-type': 'application/json',
    }

    json = {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": [
                {
                    "kind": "default",
                    "sentences": [
                        {
                            "text": text,
                            "id": 0,
                            "prefix": ""
                        }
                    ],
                    "raw_en_context_before": [],
                    "raw_en_context_after": [],
                    "preferred_num_beams": 4,
                    "quality": "fast"
                }
            ],
            "lang": {
                "user_preferred_langs": [
                    "EN",
                    "JA"
                ],
                "source_lang_user_selected": source_lang,
                "target_lang": target_lang
            },
            "priority": -1,
            "commonJobParams": {
                "mode": "translate",
                "browserType": 1
            },
            "timestamp": int(time.time())
        },
        "id": 46500010
    }

    r = requests.post("https://www2.deepl.com/jsonrpc", headers=header, json=json)
    if r.status_code == 200:
        return r.json()['result']['translations'][0]['beams'][0]['sentences'][0]['text']
    else:
        return r.json()
