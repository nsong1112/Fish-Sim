#Read simple and scrubbed bathymetric charts to create a usable simulation map

import numpy as np
from pathlib import Path

for item in (Path.cwd() / "Templates").iterdir():
    print(item.name)

template_image = input("Which template would you like to create a map from?")

print(template_image)