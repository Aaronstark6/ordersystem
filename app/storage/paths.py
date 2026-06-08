from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

TEMPLATES_DIR = DATA_DIR / "templates"
UPLOADS_DIR = DATA_DIR / "uploads"
RUNTIME_DIR = DATA_DIR / "runtime"
CACHE_DIR = DATA_DIR / "cache"
EXPORTS_DIR = DATA_DIR / "exports"
SAMPLES_DIR = DATA_DIR / "samples"
