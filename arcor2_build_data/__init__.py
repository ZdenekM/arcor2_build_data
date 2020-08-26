import os
from importlib import metadata

SERVICE_NAME = "ARCOR2 Build Service"
PORT = int(os.getenv("ARCOR2_BUILD_PORT", 5008))


def version() -> str:
    return metadata.version(__name__)
