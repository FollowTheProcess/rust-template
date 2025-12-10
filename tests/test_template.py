"""
Tests for the template generation.
"""

from __future__ import annotations

from pathlib import Path


def test_expected_files(template: Path) -> None:
    """
    Tests that a sample of the correct files have indeed
    been rendered.
    """
    expected_files = [
        ".github/workflows/CI.yml",
        ".github/workflows/labeler.yml",
        ".github/workflows/release-drafter.yml",
        ".github/workflows/release.yml",
        ".github/renovate.json",
        ".github/labels.yml",
        ".github/release-drafter.yml",
        ".gitattributes",
        ".gitignore",
        ".rustfmt.toml",
        "src/main.rs",
        "Cargo.toml",
        "LICENSE",
        "README.md",
    ]

    for file in expected_files:
        absolute_path = template.joinpath(file)
        assert absolute_path.exists(), f"{file} did not exist in generated template"


def test_no_template_tags_remaining(template: Path, template_vars: list[str]) -> None:
    """
    Tests that no Jinja template tags remain in any of the
    rendered files.
    """
    for path in template.rglob("*"):
        if not path.is_dir() and path.suffix != ".png":
            contents = path.read_text(encoding="utf-8")
            for var in template_vars:
                assert var not in contents, f"Found template tag ({var}) in {path}"
