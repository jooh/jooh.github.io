from pathlib import Path

from bs4 import BeautifulSoup
from pelican import Pelican
from pelican.settings import read_settings


def test_mermaid_draft_with_production_theme(tmp_path: Path) -> None:
    """Preserve diagram source and code highlighting in a themed draft page."""
    repo_root = Path(__file__).resolve().parents[1]
    content_dir = tmp_path / "content"
    content_dir.mkdir()
    (content_dir / "diagram.md").write_text(
        "Title: Diagram\nDate: 2026-11-07\nStatus: draft\n\n"
        "```mermaid\nflowchart TD\n    review -->|P1 & above| fix\n"
        "    fix --> review\n```\n\n"
        '```python\nprint("hello")\n```\n',
        encoding="utf-8",
    )
    output_dir = tmp_path / "output"
    settings = read_settings(
        path=str(repo_root / "publishconf.py"),
        override={
            "PATH": str(content_dir),
            "OUTPUT_PATH": str(output_dir),
            "THEME": str(repo_root / "pelican-themes" / "pelican-bootstrap3"),
            "THEME_TEMPLATES_OVERRIDES": [str(repo_root / "templates")],
            "STATIC_PATHS": [],
            "PLUGINS": [],
        },
    )
    Pelican(settings).run()

    page = BeautifulSoup(
        (output_dir / "drafts" / "diagram.html").read_text(encoding="utf-8"),
        "html.parser",
    )
    diagram = page.select_one(".mermaid")
    assert diagram is not None
    assert "review -->|P1 & above| fix" in diagram.get_text()
    assert diagram.find("span") is None
    assert page.select_one(".highlight span") is not None
    assert page.select_one("footer") is not None
    renderer = page.find("script", attrs={"type": "module"})
    assert renderer is not None
    assert "mermaid@12.3.0" in renderer.get_text()
    assert not (output_dir / "diagram.html").exists()
