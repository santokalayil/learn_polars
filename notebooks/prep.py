from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).parent
SYS_PATH = CURRENT_DIR.parent

if str(SYS_PATH) not in sys.path:
    sys.path.append(str(SYS_PATH))

DATA_DIR = SYS_PATH / "data"
