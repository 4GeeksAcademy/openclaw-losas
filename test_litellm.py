#!/usr/bin/env python3
"""Send a minimal test request to a LiteLLM-compatible Chat Completions API."""

import json
import os
import sys
import urllib.error
import urllib.request


base_url = os.environ.get("LITELLM_BASE_URL", "http://localhost:4000").rstrip("/")
model = os.environ.get("LITELLM_MODEL", "gpt-6-luna")
api_key = os.environ.get("LITELLM_API_KEY")

payload = json.dumps(
    {
        "model": model,
        "messages": [{"role": "user", "content": "Reply with exactly: LOCAL AI OK"}],
        "temperature": 0,
    }
).encode("utf-8")
headers = {"Content-Type": "application/json"}
if api_key:
    headers["Authorization"] = f"Bearer {api_key}"

request = urllib.request.Request(
    f"{base_url}/v1/chat/completions", data=payload, headers=headers, method="POST"
)
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    answer = result["choices"][0]["message"]["content"]
    if isinstance(answer, list):
        answer = " ".join(part.get("text", "") for part in answer if isinstance(part, dict))
    print(f"API responded for model {model!r}:")
    print(answer)
except (urllib.error.URLError, TimeoutError, KeyError, IndexError, json.JSONDecodeError) as exc:
    print(f"Test failed: {exc}", file=sys.stderr)
    sys.exit(1)
