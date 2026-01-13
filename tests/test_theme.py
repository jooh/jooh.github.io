import os
from pathlib import Path

import pytest


def test_theme_submodule_present() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    theme_dir = repo_root / "pelican-themes" / "pelican-bootstrap3"

    if not theme_dir.is_dir() and not os.environ.get("GITHUB_ACTIONS"):
        pytest.skip("Theme submodule not available in local environment.")

    assert theme_dir.is_dir(), "Expected pelican-bootstrap3 theme submodule to be present."
    assert (theme_dir / "templates").is_dir()
