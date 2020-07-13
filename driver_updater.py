# Author: Mohammed Sazid Al Rashid

import os, sys
import webdrivermanager
from pathlib import Path

import webdrivermanager


def update(pathname):
	driver_download_path = Path(pathname) / Path("webdrivers")
	drivers = webdrivermanager.AVAILABLE_DRIVERS

	for name in drivers:
		try:
			print("Downloading %s..." % name)
			driver = drivers[name](download_root=driver_download_path, link_path=pathname)
			driver.download_and_install()
		except RuntimeError:
			print("Skipping download of %s" % name)


def main():
	# Scripts folder is usually placed in the PATH. So we'll download the drivers there
	PYTHON_DIR = os.path.dirname(sys.executable)
	PYTHON_SCRIPTS_DIR = os.path.join(PYTHON_DIR,'Scripts')

	update(pathname=PYTHON_SCRIPTS_DIR)


if __name__ == '__main__':
	main()
