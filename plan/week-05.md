# 第 5 周 · 测试夹具、代码检查与持续集成

- **日期**：2026-11-30～2026-12-06
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

推送后 GitHub Actions 能跑 pytest；本地有 ruff；结构化输出先用夹具测解析，不依赖密钥。

## 完成标准

- 数据库和 TestClient 都来自 pytest 夹具。
- 覆盖率报告能生成，并在笔记里写下当前百分比。
- `ruff check` 通过。
- GitHub Actions 在 push 时运行 pytest，工作流文件里没有密钥值。
- 给定一段模型 JSON 文本，解析器能得到 Pydantic 对象；非法 JSON 有失败测试。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】把建库、会话和 TestClient 收成 `conftest.py` 夹具。旧测试改为使用夹具，行为保持不变。 |
| 周二 | 2.5h | 【工程】接入 coverage，生成终端报告。把百分比和未覆盖的主要模块记在笔记里，本周先补最关键的一条分支。 |
| 周三 | 2.5h | 【工程】加入 ruff。修正它报出的问题。在 README 增加一条检查命令。 |
| 周四 | 2.5h | 【工程】添加 GitHub Actions 工作流：安装依赖并运行 pytest。工作流使用仓库代码，不写入 `OPENAI_API_KEY` 的值。 |
| 周五 | 2h | 【LLM】阅读结构化输出文档。设计一个「抽取标题和三个要点」的 Pydantic 模型，字段带描述。 |
| 周末 | 3h | 【LLM】实现解析函数：合法 JSON 进入模型，缺字段或类型不对时返回明确错误。用夹具文件测试成功和失败。真实调用留到下周。 |

## Checklist

- [ ] 夹具复用完成
- [ ] 覆盖率有记录
- [ ] ruff 通过
- [ ] CI 工作流可运行
- [ ] JSON 解析有成功和失败测试

## 参考链接

- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [coverage](https://coverage.readthedocs.io/en/latest/)
- [Ruff](https://docs.astral.sh/ruff/)
- [GitHub Actions 测试 Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Actions 中的密钥](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [结构化输出](https://developers.openai.com/api/docs/guides/structured-outputs)
- [结构化输出示例](https://developers.openai.com/cookbook/examples/structured_outputs_intro)
