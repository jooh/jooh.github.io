from __future__ import annotations

def test_site_build_produces_index(site_build) -> None:
    index_path = site_build.output_dir / "index.html"
    assert index_path.is_file(), f"Expected build to produce {index_path}"
