# 第 7 周 · 可重复构建的镜像与提示对比

- **日期**：2026-12-14～2026-12-20
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

容器以非 root 用户运行，健康检查通过；两份提示的差异被记录下来。

## 完成标准

- Dockerfile 分为构建阶段和运行阶段，镜像里不包含测试缓存。
- 进程不以 root 运行。Compose 的 healthcheck 能在本地变绿。
- README 同时写下 Conda 路径和 uv 路径，并说明容器运行靠环境变量注入配置。
- 两份提示各调用一次，笔记含回复要点、时延和 token。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】把 Dockerfile 改成多阶段。运行阶段只复制虚拟环境或安装好的依赖与源码。 |
| 周二 | 2.5h | 【工程】添加非 root 用户。确认应用仍能监听端口。补 `.dockerignore`，排除 `.env`、`.git` 和缓存目录。 |
| 周三 | 2.5h | 【工程】在 Compose 里配置 healthcheck，请求 `/health`。用环境变量把 `OPENAI_MODEL` 传进容器，不把密钥写进 Compose 文件。 |
| 周四 | 2.5h | 【工程】更新 README：Conda 或 uv 均可，本仓库推荐 Conda 亦可。写出本地启动和 `docker compose up` 两条路径。跑一次容器内 `/health` 为 200。 |
| 周五 | 2h | 【LLM】写两份提示：一份只有任务句，一份包含角色、步骤和输出格式。先在笔记里预测哪一份更稳。 |
| 周末 | 3h | 【LLM】用客户端对两份提示各调用一次，temperature 固定为 0。记录时延、token 和回复是否遵守格式。写出你愿意留在模板库里的那一版，并说明原因。 |

## Checklist

- [ ] 多阶段镜像可构建
- [ ] 容器内非 root
- [ ] healthcheck 通过
- [ ] README 含 Conda 与 uv
- [ ] 提示对比表已写下

## 参考链接

- [多阶段构建](https://docs.docker.com/build/building/multi-stage/)
- [Dockerfile 参考](https://docs.docker.com/reference/dockerfile/)
- [Compose 服务](https://docs.docker.com/reference/compose-file/services/)
- [FastAPI Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [十二要素：配置](https://12factor.net/config)
- [提示工程](https://developers.openai.com/api/docs/guides/prompt-engineering)
