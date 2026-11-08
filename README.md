# LetsLearningAgent

本仓库记录 Agent 开发工程师一年学习计划（2026-11 至 2027-10，每周约 15 小时）。

## 学习计划

- 一年总任务：[LEARNING.md](LEARNING.md)
- 周计划索引：[plan/README.md](plan/README.md)
- 每周文件：`plan/week-01.md` 至 `plan/week-48.md`

先读 [LEARNING.md](LEARNING.md)，确认阶段、知识地图和作品集，再从 [plan/README.md](plan/README.md) 进入当周。

## 第 1 周代码

周二的文本函数和周三的 FastAPI 在 `code/week01/`。本地开发使用 Conda 环境 `LearningAgent`（Python 3.12）。条目数据只存在于进程内存中，重启后清空。

### Conda 本地开发

还没有该环境时，在 `code/week01/` 创建并激活：

```bash
cd code/week01
conda env create -f environment.yml
conda activate LearningAgent
pytest
python -m uvicorn app.main:app --reload
```

环境已经存在时，激活后安装依赖再启动：

```bash
conda activate LearningAgent
cd code/week01
pip install -r requirements.txt
pytest
python -m uvicorn app.main:app --reload
```

启动后访问 `http://127.0.0.1:8000/health`，交互文档在 `http://127.0.0.1:8000/docs`。

### Docker

在 `code/week01/` 构建镜像、启动容器、检查健康接口，然后停止：

```bash
cd code/week01
docker compose build
docker compose up -d
curl http://127.0.0.1:8000/health
docker compose down
```

`curl` 应返回 `{"status":"ok"}`。容器内的启动命令是 `python -m uvicorn app.main:app --host 0.0.0.0 --port 8000`，并把容器的 8000 端口映射到本机 8000。
