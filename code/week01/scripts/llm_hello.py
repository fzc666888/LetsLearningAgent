"""发送一句短提示，并打印回复与 token 用量。

密钥只从环境变量读取，不会写入文件或打印出来。
"""

import os
import sys

from openai import OpenAI

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-chat"
PROMPT = "用一句话打个招呼。"


def main() -> None:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("缺少环境变量 DEEPSEEK_API_KEY", file=sys.stderr)
        sys.exit(1)

    base_url = os.environ.get("DEEPSEEK_BASE_URL") or DEEPSEEK_BASE_URL
    model = os.environ.get("DEEPSEEK_MODEL") or DEFAULT_MODEL

    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
    )
    reply = response.choices[0].message.content or ""
    usage = response.usage
    prompt_tokens = usage.prompt_tokens if usage is not None else "未知"
    completion_tokens = usage.completion_tokens if usage is not None else "未知"

    print(reply)
    print(f"prompt_tokens: {prompt_tokens}")
    print(f"completion_tokens: {completion_tokens}")


if __name__ == "__main__":
    main()
