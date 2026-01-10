from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys

import pytest


@dataclass(frozen=True)
class SiteBuild:
    output_dir: Path
    result: subprocess.CompletedProcess[str]


@pytest.fixture(scope="session")
def site_build(tmp_path_factory: pytest.TempPathFactory) -> SiteBuild:
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = tmp_path_factory.mktemp("site-build") / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pelican",
            str(repo_root / "content"),
            "-s",
            str(repo_root / "pelicanconf.py"),
            "-o",
            str(output_dir),
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )

    return SiteBuild(output_dir=output_dir, result=result)
