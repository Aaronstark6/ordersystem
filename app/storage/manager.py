from pathlib import Path

from app.storage.paths import (
    CACHE_DIR,
    EXPORTS_DIR,
    RUNTIME_DIR,
    SAMPLES_DIR,
    TEMPLATES_DIR,
    UPLOADS_DIR,
)


_CATEGORY_DIRS = {
    "templates": TEMPLATES_DIR,
    "uploads": UPLOADS_DIR,
    "runtime": RUNTIME_DIR,
    "cache": CACHE_DIR,
    "exports": EXPORTS_DIR,
    "samples": SAMPLES_DIR,
}


def ensure_storage_dirs() -> None:
    for directory in _CATEGORY_DIRS.values():
        directory.mkdir(parents=True, exist_ok=True)


def get_templates_dir() -> Path:
    return TEMPLATES_DIR


def get_uploads_dir() -> Path:
    return UPLOADS_DIR


def get_runtime_dir() -> Path:
    return RUNTIME_DIR


def get_cache_dir() -> Path:
    return CACHE_DIR


def get_exports_dir() -> Path:
    return EXPORTS_DIR


def get_samples_dir() -> Path:
    return SAMPLES_DIR


def resolve_storage_path(category: str, filename: str) -> Path:
    try:
        base_dir = _CATEGORY_DIRS[category]
    except KeyError as exc:
        raise ValueError(f"Unsupported storage category: {category}") from exc

    candidate = Path(filename)
    if candidate.is_absolute() or candidate.drive:
        raise ValueError("Storage filename must be relative.")
    if ".." in candidate.parts:
        raise ValueError("Storage filename must not contain path traversal.")

    resolved_base = base_dir.resolve(strict=False)
    resolved_path = (base_dir / candidate).resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_base)
    except ValueError as exc:
        raise ValueError("Resolved storage path must remain inside its category.") from exc

    return resolved_path
