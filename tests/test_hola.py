from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_hola_prints_hola_mundo() -> None:
    script = Path(__file__).resolve().parents[1] / "hola.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "Hola Mundo"
