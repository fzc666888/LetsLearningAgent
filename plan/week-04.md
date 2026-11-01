# 第 4 周 · 错误模型、分页与采样参数

- **日期**：2026-11-23～2026-11-29
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

调用方能根据稳定的错误 JSON 和分页字段写客户端；你能解释采样参数如何影响长度和多样性。

## 完成标准

- 校验失败和未找到资源都返回固定结构：`code`、`message`、`request_id`。
- 列表支持 `limit` 与 `offset`，非法参数返回 422，并有测试。
- OpenAPI 文档里能看到请求和响应示例。
- 同一提示在两组采样参数下各调用一次，笔记里有时延和 token 表。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】定义错误响应模型。为 404 和请求校验失败注册处理函数，响应里带上本请求的 id。 |
| 周二 | 2.5h | 【工程】给 `GET /items` 增加 `limit`（默认 20，最大 100）和 `offset`。返回 `items` 与 `total`。 |
| 周三 | 2.5h | 【工程】为创建和列表补 OpenAPI 示例。用 TestClient 覆盖：空页、越界 offset、limit 为 0、正常第二页。 |
| 周四 | 2.5h | 【工程】把错误处理放进现有分层，避免路由里堆叠 if。跑一遍 `pytest`，修到全绿。 |
| 周五 | 2h | 【LLM】阅读采样相关说明（temperature、max output tokens）。在笔记里各用一句话定义它们。 |
| 周末 | 3h | 【LLM】写 `scripts/sampling_probe.py`。同一句提示调用两次：一次 temperature 0、较短输出上限；一次 temperature 0.7、更长上限。打印时延和 token 用量，把结果表贴进笔记。 |

## Checklist

- [ ] 错误 JSON 结构稳定
- [ ] 分页有边界测试
- [ ] OpenAPI 可见示例
- [ ] pytest 全绿
- [ ] 采样对比表已记录

## 参考链接

- [FastAPI 错误处理](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [查询参数](https://fastapi.tiangolo.com/tutorial/query-params/)
- [请求体](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic 模型](https://docs.pydantic.dev/latest/concepts/models/)
- [提示工程](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [OpenAI 快速开始](https://developers.openai.com/api/docs/quickstart)
