from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def site_output_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("pelican-output")


@pytest.fixture(scope="session")
def build_site(site_output_dir: Path) -> Path:
    repo_root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [
            "make",
            "html",
            "USE_UV=1",
            "CONFFILE=tests/pelicanconf_test.py",
            f"OUTPUTDIR={site_output_dir}",
        ],
        cwd=repo_root,
        check=True,
    )
    return site_output_dir


def test_site_build(build_site: Path) -> None:
    assert (build_site / "index.html").is_file()
