"""Regenerate project thumbnails after updating a screenshot. Requires Pillow."""

import json
from pathlib import Path

from PIL import Image

root = Path(__file__).resolve().parents[1]
projects = root / "public/image/projects"
previews = projects / "previews"
previews.mkdir(exist_ok=True)
sizes = {}
for path in sorted(projects.glob("*.webp")):
    with Image.open(path) as image:
        sizes[path.stem] = image.size
        image.thumbnail((560, image.height), Image.Resampling.LANCZOS)
        image.save(previews / path.name, quality=85, method=6)

(root / "src/assets/project-sizes.json").write_text(
    json.dumps(sizes, separators=(",", ":")) + "\n", encoding="utf-8"
)
