from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def site_output_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("pelican-output")


def _run_make_build(
    *,
    target: str,
    output_dir: Path,
    repo_root: Path,
    extra_args: list[str],
) -> tuple[Path, str]:
    result = subprocess.run(
        [
            "make",
            target,
            "USE_UV=1",
            *extra_args,
            f"OUTPUTDIR={output_dir}",
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return output_dir, f"{result.stdout}\n{result.stderr}".strip()


@pytest.fixture(scope="session")
def build_site(site_output_dir: Path) -> tuple[Path, str]:
    repo_root = Path(__file__).resolve().parents[1]
    return _run_make_build(
        target="html",
        output_dir=site_output_dir,
        repo_root=repo_root,
        extra_args=["CONFFILE=tests/pelicanconf_test.py"],
    )


@pytest.fixture(scope="session")
def publish_site_output_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("pelican-publish-output")


@pytest.fixture(scope="session")
def build_publish_site(publish_site_output_dir: Path) -> tuple[Path, str]:
    repo_root = Path(__file__).resolve().parents[1]
    return _run_make_build(
        target="publish",
        output_dir=publish_site_output_dir,
        repo_root=repo_root,
        extra_args=["PUBLISHCONF=tests/publishconf_test.py"],
    )


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


def test_publish_build(build_publish_site: tuple[Path, str]) -> None:
    site_output_dir, _ = build_publish_site
    assert (site_output_dir / "index.html").is_file()


def test_publish_build_has_no_pelican_errors(
    build_publish_site: tuple[Path, str],
) -> None:
    _, output = build_publish_site
    error_lines = [
        line
        for line in output.splitlines()
        if re.search(r"\\b(ERROR|CRITICAL)\\b", line)
    ]
    assert not error_lines, "Pelican reported errors:\\n" + "\\n".join(error_lines)
