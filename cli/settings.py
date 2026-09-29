from __future__ import annotations

import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from cli.paths import ROOT


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(ROOT / ".env", ROOT / ".env.local"),
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )
    openrouter_api_key: str = ""


@lru_cache
def settings() -> Settings:
    loaded = Settings()
    if loaded.openrouter_api_key:
        os.environ.setdefault("OPENROUTER_API_KEY", loaded.openrouter_api_key)
    return loaded
