# 第 17 周 · 入库与问答 API

- **日期**：2027-02-22～2027-02-28
- **阶段**：1 · LLM 与 RAG
- **知识层级**：L2
- **投入**：约 15 小时（应用约 11 小时，阅读约 4 小时）

## 本周目标

`POST /ingest` 与 `POST /ask` 可用；测试使用假嵌入和假生成，CI 不需要密钥。

## 完成标准

- 入库接口接受本地允许目录下的 Markdown 路径，拒绝目录之外的路径。
- 提问接口返回答案、来源 id 和请求 id。
- TestClient 覆盖成功入库、非法路径、空库提问。
- OpenAPI 里能看到两个接口的字段说明。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【应用】设计请求和响应模型。提问响应包含 `answer`、`sources`、`request_id`。 |
| 周二 | 2.5h | 【应用】实现入库接口，复用第 12 周的切块和哈希。路径必须落在配置的语料目录内，并用测试锁住拒绝逻辑。 |
| 周三 | 2.5h | 【应用】实现提问接口，检索与生成都通过可替换依赖注入。假生成器返回固定答案。 |
| 周四 | 2.5h | 【应用】补齐三类集成测试，并更新 OpenAPI 描述。跑通 pytest。 |
| 周五 | 2h | 【应用 1h】用真实笔记走一遍入库和提问，把请求 id 记下来。【阅读 1h】看 FastAPI 大项目结构文档，对照你的路由是否还薄。 |
| 周末 | 3h | 【阅读】阅读 FastAPI 测试文档和错误处理文档。写一页：这个 API 还有哪些响应没有固定结构，下一周日志要带哪些字段。 |

## Checklist

- [ ] 入库与提问接口可用
- [ ] 路径越界被拒绝
- [ ] 测试不需要密钥
- [ ] OpenAPI 有字段说明
- [ ] 笔记列出待记录的日志字段

## 参考链接

- [FastAPI 测试](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI 大项目结构](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI 错误处理](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [请求体](https://fastapi.tiangolo.com/tutorial/body/)
