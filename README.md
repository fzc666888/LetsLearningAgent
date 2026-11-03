# LetsLearningAgent

本仓库记录 Agent 开发工程师一年学习计划（2026-11 至 2027-10，每周约 15 小时）。

## 学习计划

- 一年总任务：[LEARNING.md](LEARNING.md)
- 周计划索引：[plan/README.md](plan/README.md)
- 每周文件：`plan/week-01.md` 至 `plan/week-48.md`

先读 [LEARNING.md](LEARNING.md)，确认阶段、知识地图和作品集，再从 [plan/README.md](plan/README.md) 进入当周。

## 第 1 周代码

周二的文本函数和周三的 FastAPI 在 `code/week01/`。使用已创建的 Conda 环境 `LearningAgent`（Python 3.12）。

```bash
conda activate LearningAgent
cd code/week01
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

启动后访问 `http://127.0.0.1:8000/health`，交互文档在 `http://127.0.0.1:8000/docs`。条目数据只存在于进程内存中，重启后清空。
