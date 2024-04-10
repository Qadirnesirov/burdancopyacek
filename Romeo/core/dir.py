import os
import sys
from os import listdir, mkdir

from Zatra.logging import LOGGER


def dirr():
    if "helper" not in listdir():
        LOGGER(__name__).warning(
            f"köməkçi qovluq tapılmadı. Lütfən, deponu yenidən klonlayın."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Kataloqlar Yenilənib.")
  
