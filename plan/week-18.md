# 第 18 周 · 时延、用量与命中文档日志

- **日期**：2027-03-01～2027-03-07
- **阶段**：1 · LLM 与 RAG
- **知识层级**：L2
- **投入**：约 15 小时（应用约 11 小时，阅读约 4 小时）

## 本周目标

一次提问对应一条 JSONL 追踪；字段固定，测试能读回。

## 完成标准

- 每条追踪含 `request_id`、`latency_ms`、`prompt_tokens`、`completion_tokens`、`source_ids`。
- mock 生成路径也会写追踪，token 允许为 0。
- 日志文件按日期滚动或覆盖策略在 README 里有一句说明。
- 笔记对比你的 JSONL 和 OpenTelemetry 里 span 的相似处。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【应用】定义追踪记录的 Pydantic 模型。写追加 JSONL 的函数，并用测试读回。 |
| 周二 | 2.5h | 【应用】在提问流程结束时写一条追踪。测量从进入服务到返回的毫秒数。 |
| 周三 | 2.5h | 【应用】从模型响应中取出 token 用量；mock 客户端返回你指定的用量，测试断言写进了文件。 |
| 周四 | 2.5h | 【应用】把检索到的 source id 按排名写入追踪。确认错误请求也会留下 request id。 |
| 周五 | 2h | 【应用 1h】真实提问两次，打开 JSONL 核对字段。【阅读 1h】打开 OpenTelemetry Python 入门，看 span 的名字和属性。 |
| 周末 | 3h | 【阅读】读 OpenTelemetry Python 入门的主要步骤，并浏览 LangSmith 文档首页对追踪的说明。写一页：你现在的 JSONL 够排错，还缺哪两个字段才会接近 span。 |

## Checklist

- [ ] JSONL 字段固定
- [ ] mock 路径也会记录
- [ ] 时延单位是毫秒
- [ ] 真实两次提问已核对
- [ ] 笔记对照了 span

## 参考链接

- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/getting-started/)
- [LangSmith](https://docs.smith.langchain.com/)
- [十二要素：日志](https://12factor.net/logs)
- [Python logging](https://docs.python.org/3/howto/logging.html)
