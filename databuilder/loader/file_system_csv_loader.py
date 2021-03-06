import csv
import logging

from pyhocon import ConfigTree  # noqa: F401
from typing import Any  # noqa: F401

from databuilder.loader.base_loader import Loader


class FileSystemCSVLoader(Loader):
    """
    Loader class to write csv files to Local FileSystem
    """
    def init(self, conf):
        # type: (ConfigTree) -> None
        """
        Initialize file handlers from conf
        :param conf:
        """
        self.conf = conf
        self.file_path = self.conf.get_string('file_path')
        self.file_mode = self.conf.get_string('mode', 'w')

        self.file_handler = open(self.file_path, self.file_mode)

    def load(self, record):
        # type: (Any) -> None
        """
        Write record object as csv to file
        :param record:
        :return:
        """
        if not record:
            return

        if not hasattr(self, 'writer'):
            self.writer = csv.DictWriter(self.file_handler,
                                         fieldnames=vars(record).keys())
            self.writer.writeheader()

        self.writer.writerow(vars(record))
        self.file_handler.flush()

    def close(self):
        # type: () -> None
        """
        Close file handlers
        :return:
        """
        try:
            self.file_handler.close()
        except Exception as e:
            logging.warning("Failed trying to close a file handler! %s",
                            str(e))

    def get_scope(self):
        # type: () -> str
        return "loader.filesystem.csv"
