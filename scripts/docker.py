"""Code also from: https://github.com/THEGOLDENPRO/devgoldy.xyz"""

import sys
sys.path.insert(0, '.')

import os
from app import __version__

os.system(
    f"docker build -t r3tr0ananas/ananas_moe:{__version__} --build-arg ARCH=amd64 ."
)

os.system(
    "docker build -t r3tr0ananas/ananas_moe:latest --build-arg ARCH=amd64 ."
)