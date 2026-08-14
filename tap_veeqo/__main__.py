"""Veeqo entry point.

Copyright (c) 2026 Meltano.
"""

from __future__ import annotations

from tap_veeqo.tap import TapVeeqo

TapVeeqo.cli()
