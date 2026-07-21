from pathlib import Path

APP_NAME = "Personal Finance Dashboard"
APP_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"
DATABASE_DIR = BASE_DIR / "database"
DOCS_DIR = BASE_DIR / "docs"

DATABASE_FILE = DATABASE_DIR / "finance.db"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 760

FONT_FAMILY = "Segoe UI"