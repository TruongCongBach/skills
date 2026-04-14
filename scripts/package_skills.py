#!/usr/bin/env python3
"""Package repo skills into per-skill archives plus a bundle archive."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
IGNORED_PARTS = {"__pycache__"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}
IGNORED_NAMES = {".DS_Store"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create zip archives for all skills in the repository."
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Optional list of skill folder names to package",
    )
    args = parser.parse_args()

    skill_dirs = collect_skill_dirs(args.only)
    DIST_DIR.mkdir(exist_ok=True)

    for skill_dir in skill_dirs:
        output = DIST_DIR / f"{skill_dir.name}.zip"
        build_archive(output, [skill_dir])
        print(f"built: {output.relative_to(ROOT)}")

    bundle_output = DIST_DIR / "skills-bundle.zip"
    build_archive(bundle_output, skill_dirs)
    print(f"built: {bundle_output.relative_to(ROOT)}")
    return 0


def collect_skill_dirs(only: list[str] | None) -> list[Path]:
    skill_dirs = sorted(
        path for path in SKILLS_DIR.iterdir() if path.is_dir() and (path / "SKILL.md").exists()
    )
    if not only:
        return skill_dirs

    wanted = set(only)
    selected = [path for path in skill_dirs if path.name in wanted]
    missing = sorted(wanted - {path.name for path in selected})
    if missing:
        raise SystemExit(f"unknown skill names: {', '.join(missing)}")
    return selected


def build_archive(output: Path, roots: list[Path]) -> None:
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for root in roots:
            for file_path in sorted(root.rglob("*")):
                if not file_path.is_file():
                    continue
                if should_skip(file_path):
                    continue
                archive.write(file_path, file_path.relative_to(ROOT))


def should_skip(file_path: Path) -> bool:
    if any(part in IGNORED_PARTS for part in file_path.parts):
        return True
    if file_path.suffix in IGNORED_SUFFIXES:
        return True
    if file_path.name in IGNORED_NAMES:
        return True
    return False


if __name__ == "__main__":
    raise SystemExit(main())
