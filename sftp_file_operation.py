import logging
from datetime import datetime
import pysftp as pysftp
from typing import List


class SftpConnector:

    def __init__(self, sftp_host: str, sftp_username: str, sftp_password: str, sftp_port: int, sftp_default_path: str):
        self.host = sftp_host
        self.username = sftp_username
        self.password = sftp_password
        self.port = sftp_port
        self.default_path = sftp_default_path
        # FIXED
        self.today = datetime.today()

    def connect(self):
        con = None
        try:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            con = pysftp.Connection(host=self.host, username=self.username, password=self.password,
                                    port=self.port, default_path=self.default_path, cnopts=cnopts)
        except pysftp.exceptions as e:
            print(e, "error")
        return con


def change_directory(connection: pysftp.Connection, path: str):
    connection.cd(path)


def mkdirs(connection: pysftp.Connection, paths: List[str]):
    for path in paths:
        try:
            connection.makedirs(path)
        except pysftp.exceptions as e:
            logging.exception(e)


def upload(connection: pysftp.Connection, put_this: str, to: str):
    try:
        connection.put(localpath=put_this, remotepath=to)
    except pysftp.exceptions as e:
        logging.exception(e)


def download(connection: pysftp.Connection, get_this: str, to: str):
    try:
        connection.get(remotepath=get_this, localpath=to)
    except pysftp.exceptions as e:
        logging.exception(e)

