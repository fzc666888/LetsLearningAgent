# 第 2 周 · 配置、日志与可测试的模型客户端

- **日期**：2026-11-09～2026-11-15
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

配置从环境变量进入程序，模型调用经过统一客户端，单测不访问外网。

## 完成标准

- 设置类只读取 `OPENAI_API_KEY`、`OPENAI_BASE_URL`、`OPENAI_MODEL`，缺失密钥时给出明确错误。
- 日志包含级别和请求标识，输出里不出现环境变量的值。
- 客户端设置超时，并对 429 与 5xx 最多重试 2 次。
- 客户端单测全部使用 mock，`pytest` 在无网络、无密钥时通过。
- `scripts/llm_hello.py` 改为调用该客户端，真实调用仍打印 token 用量。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】用 pydantic-settings 写配置。提交一份只含变量名的示例（值为空）：`OPENAI_API_KEY`、`OPENAI_BASE_URL`、`OPENAI_MODEL`。确认 `.env` 已被忽略。 |
| 周二 | 2.5h | 【工程】加结构化日志：时间、级别、logger 名、消息。为每次出站请求生成一个短请求 id 并写入日志。写一条测试，断言日志文本里没有把环境变量值拼进去。 |
| 周三 | 2.5h | 【工程】用 httpx 封装同步客户端：连接超时与读取超时分开设置；仅对 429 和 5xx 重试，最多 2 次；把网络错误和 HTTP 错误分成两种异常。 |
| 周四 | 2.5h | 【工程】用 monkeypatch 或 respx 伪造 HTTP 响应。覆盖成功、429 后成功、4xx 不重试、超时。测试不发起真实网络请求。 |
| 周五 | 2h | 【LLM】阅读消息角色（system / developer / user / assistant）和 token 的含义。用自己的话写半页笔记：一次调用里哪些字段会计入 prompt token。 |
| 周末 | 3h | 【LLM】让 `llm_hello.py` 走新客户端。真实调用各跑一次 temperature 0 与 0.7，把两段回复和 token 用量记在笔记里。密钥仍只来自 `OPENAI_API_KEY`。 |

## Checklist

- [ ] 配置只来自环境变量名
- [ ] 日志不含密钥值
- [ ] 重试规则有单测
- [ ] 无网络时 pytest 通过
- [ ] hello 脚本打印 token 用量
- [ ] 笔记写清消息角色

## 参考链接

- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [FastAPI 设置](https://fastapi.tiangolo.com/advanced/settings/)
- [logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [HTTPX](https://www.python-httpx.org/)
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [十二要素：配置](https://12factor.net/config)
- [提示工程：消息角色](https://developers.openai.com/api/docs/guides/prompt-engineering)
