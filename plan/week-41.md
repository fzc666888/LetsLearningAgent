# 第 41 周 · 作品 P5：只读 MCP 与安全边界

- **日期**：2027-08-09～2027-08-15
- **阶段**：3 · 生产化与求职
- **知识层级**：L5
- **投入**：约 15 小时（作品约 9 小时，求职约 6 小时）

## 本周目标

检查器或官方示例客户端能调用这个只读工具；说明文档包含安全边界。

## 完成标准

- 按官方文档安装 Python SDK，并实现一个搜索笔记的工具。
- 该工具只读，参数里的路径限制在语料目录内。
- 用 MCP Inspector 或文档中的客户端完成一次调用，结果记入笔记。
- P5 说明包含威胁边界：它不写文件、不读取环境变量的值。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【作品】阅读 MCP 介绍和构建服务器文档。列出工具、资源和提示三类原语，标出本周只做工具。 |
| 周二 | 2.5h | 【作品】按文档创建本地服务器，注册 `search_notes`。返回片段和来源路径。 |
| 周三 | 2.5h | 【作品】加入目录限制。为越界路径写测试或用 Inspector 记录一次拒绝。 |
| 周四 | 2.5h | 【作品 1.5h】用 Inspector 完成一次成功调用，截图或复制文本进 `notes/p5.md`。【求职 1h】用四句话解释 MCP：谁是客户端，谁是服务器，工具由谁决定调用。 |
| 周五 | 2h | 【求职】把这四句话扩成一分钟面试回答，并写一个追问：为什么第一版只做只读。 |
| 周末 | 3h | 【求职】阅读 MCP 安全最佳实践和本地服务器安全文档。把你采纳的三条写进 P5 说明，并在 README 加上作品 P5。 |

## Checklist

- [ ] 只读工具可被调用
- [ ] 越界路径被拒绝
- [ ] Inspector 或客户端记录已保存
- [ ] 面试回答已写
- [ ] README 含 P5

## 参考链接

- [MCP 介绍](https://modelcontextprotocol.io/docs/getting-started/intro)
- [构建 MCP 服务器](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)
- [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- [MCP 安全最佳实践](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [本地 MCP 服务器安全](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/local-server-security)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
