from cache import CacheManager
import config


class DriverManager(object):
    def __init__(self):
        self._file_manager = CacheManager(
            to_folder=config.folder, dir_name=config.folder)

    def install(self):
        raise NotImplementedError("Please Implement this method")
