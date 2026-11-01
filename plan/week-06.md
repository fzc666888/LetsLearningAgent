# 第 6 周 · 异步客户端与流式输出

- **日期**：2026-12-07～2026-12-13
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

同步路径的测试仍然不访问网络；另外有一条流式路径能逐段收到文本。

## 完成标准

- 异步客户端与同步客户端共享超时和重试规则。
- 流式脚本在终端逐段打印文本，结束时打印合计 token（若接口提供用量）。
- 一个 FastAPI 接口能以流的形式返回文本，测试使用 mock 字节块。
- 笔记用自己的话说明流式响应和一次性响应的差别。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】把 HTTP 调用补上 httpx 异步版本。重试规则与同步版一致。用 mock 测试一次成功和一次 5xx 重试。 |
| 周二 | 2.5h | 【工程】保持现有 CRUD 测试全绿。把读多写少的列表路由改成 async，确认依赖注入的数据库会话仍然正确关闭。 |
| 周三 | 2.5h | 【工程】新增流式响应接口，上游用可注入的异步生成器，便于测试。TestClient 读到拼接后的全文。 |
| 周四 | 2.5h | 【工程】为流式接口补错误用例：上游在中途失败时，客户端能看到错误而不是静默截断。记录你选择的状态码。 |
| 周五 | 2h | 【LLM】阅读流式输出文档和 MDN 的 Server-sent events。笔记里画出「客户端、你的 API、模型服务」三者的数据方向。 |
| 周末 | 3h | 【LLM】写 `scripts/llm_stream.py`，从 `OPENAI_API_KEY` 取密钥，逐段打印模型输出。把一次真实流式调用的首段延迟记在笔记里。 |

## Checklist

- [ ] 异步客户端有重试测试
- [ ] CRUD 测试仍绿
- [ ] 流式接口可用 mock 测完
- [ ] 中途失败有断言
- [ ] 真实流式脚本打通

## 参考链接

- [HTTPX](https://www.python-httpx.org/)
- [FastAPI 自定义响应](https://fastapi.tiangolo.com/advanced/custom-response/)
- [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [OpenAI 流式响应](https://developers.openai.com/api/docs/guides/streaming-responses)
- [Uvicorn](https://github.com/Kludex/uvicorn)
