import pathlib
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Paths
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
APP_DIR = PROJECT_ROOT / "app"
STATIC_DIR = APP_DIR / "static"
DATA_DIR = PROJECT_ROOT / "data"
CHROMA_DIR = PROJECT_ROOT / "chroma"





