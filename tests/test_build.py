from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def site_output_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("pelican-output")


@pytest.fixture(scope="session")
def build_site(site_output_dir: Path) -> tuple[Path, str]:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            "make",
            "html",
            "USE_UV=1",
            "CONFFILE=tests/pelicanconf_test.py",
            f"OUTPUTDIR={site_output_dir}",
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return site_output_dir, f"{result.stdout}\n{result.stderr}".strip()


def test_site_build(build_site: tuple[Path, str]) -> None:
    site_output_dir, _ = build_site
    assert (site_output_dir / "index.html").is_file()


def test_site_build_has_no_pelican_errors(build_site: tuple[Path, str]) -> None:
    _, output = build_site
    error_lines = [
        line
        for line in output.splitlines()
        if re.search(r"\\b(ERROR|CRITICAL)\\b", line)
    ]
    assert not error_lines, "Pelican reported errors:\\n" + "\\n".join(error_lines)
