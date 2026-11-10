from types import SimpleNamespace

import pytest

from scripts.llm_hello import main


def test_missing_api_key_exits(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
    assert "DEEPSEEK_API_KEY" in capsys.readouterr().err


def test_uses_deepseek_defaults(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    monkeypatch.delenv("DEEPSEEK_BASE_URL", raising=False)
    monkeypatch.delenv("DEEPSEEK_MODEL", raising=False)

    created: dict[str, object] = {}

    class FakeCompletions:
        def create(self, **kwargs: object) -> SimpleNamespace:
            created["request"] = kwargs
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content="你好"))],
                usage=SimpleNamespace(prompt_tokens=3, completion_tokens=2),
            )

    class FakeClient:
        def __init__(self, *, api_key: str, base_url: str | None) -> None:
            created["base_url"] = base_url
            self.chat = SimpleNamespace(completions=FakeCompletions())

    monkeypatch.setattr("scripts.llm_hello.OpenAI", FakeClient)
    main()

    assert created["base_url"] == "https://api.deepseek.com"
    assert created["request"]["model"] == "deepseek-chat"
    assert "test-key" not in capsys.readouterr().out


def test_prints_reply_and_token_usage(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    monkeypatch.setenv("DEEPSEEK_BASE_URL", "https://example.invalid/v1")
    monkeypatch.setenv("DEEPSEEK_MODEL", "test-model")

    created: dict[str, object] = {}

    class FakeCompletions:
        def create(self, **kwargs: object) -> SimpleNamespace:
            created["request"] = kwargs
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content="你好"))],
                usage=SimpleNamespace(prompt_tokens=11, completion_tokens=7),
            )

    class FakeClient:
        def __init__(self, *, api_key: str, base_url: str | None) -> None:
            created["api_key"] = api_key
            created["base_url"] = base_url
            self.chat = SimpleNamespace(completions=FakeCompletions())

    monkeypatch.setattr("scripts.llm_hello.OpenAI", FakeClient)
    main()

    output = capsys.readouterr().out
    assert "你好" in output
    assert "prompt_tokens: 11" in output
    assert "completion_tokens: 7" in output
    assert "test-key" not in output
    assert created["api_key"] == "test-key"
    assert created["base_url"] == "https://example.invalid/v1"
    assert created["request"] == {
        "model": "test-model",
        "messages": [{"role": "user", "content": "用一句话打个招呼。"}],
    }
