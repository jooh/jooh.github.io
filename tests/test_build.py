from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pytest


PELICAN_ERROR_LOG_PATTERN = re.compile(r"\b(ERROR|CRITICAL)\b")
IGNORED_ERROR_SUBSTRINGS = ("Skipping",)


@dataclass(frozen=True)
class BuildSpec:
    name: str
    target: str
    config_arg: str
    config_path: str
    expected_site_name: str


@dataclass(frozen=True)
class BuildResult:
    spec: BuildSpec
    output_dir: Path
    output: str


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


def _extract_actionable_pelican_errors(output: str) -> list[str]:
    errors = [
        line for line in output.splitlines() if PELICAN_ERROR_LOG_PATTERN.search(line)
    ]
    return [
        line
        for line in errors
        if not any(ignored in line for ignored in IGNORED_ERROR_SUBSTRINGS)
    ]


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture(
    scope="session",
    params=[
        BuildSpec(
            name="html",
            target="html",
            config_arg="CONFFILE",
            config_path="tests/pelicanconf_test.py",
            expected_site_name="Test Site",
        ),
        BuildSpec(
            name="publish",
            target="publish",
            config_arg="PUBLISHCONF",
            config_path="tests/publishconf_test.py",
            expected_site_name="Johan Carlin",
        ),
    ],
    ids=lambda spec: spec.name,
)
def build_result(
    request: pytest.FixtureRequest,
    tmp_path_factory: pytest.TempPathFactory,
    repo_root: Path,
) -> BuildResult:
    spec = request.param
    output_dir = tmp_path_factory.mktemp(f"pelican-{spec.name}-output")
    output_dir, output = _run_make_build(
        target=spec.target,
        output_dir=output_dir,
        repo_root=repo_root,
        extra_args=[f"{spec.config_arg}={spec.config_path}"],
    )
    return BuildResult(spec=spec, output_dir=output_dir, output=output)


def test_site_build(build_result: BuildResult) -> None:
    assert (build_result.output_dir / "index.html").is_file()


def test_site_build_has_no_pelican_errors(build_result: BuildResult) -> None:
    error_lines = _extract_actionable_pelican_errors(build_result.output)
    assert not error_lines, "Pelican reported errors:\n" + "\n".join(error_lines)


def test_site_index_contains_site_name(build_result: BuildResult) -> None:
    index_html = (build_result.output_dir / "index.html").read_text(encoding="utf-8")
    assert build_result.spec.expected_site_name in index_html
