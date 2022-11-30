import logging

import requests as requests
from requests import Response


# token = ''
class LineNotify:
    def __init__(self, msg: str, token: str = ''
                 , sticker_package_id: str = '6370', sticker_id: str = '11088035'):
        self.payload = {
            'message': msg,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id
        }
        self.token = token

    def notify(self) -> Response:
        try:
            return requests.post('https://notify-api.line.me/api/notify'
                                 , headers={'Authorization': 'Bearer {}'.format(self.token)}
                                 , params=self.payload
                                 )
        except Exception as e:
            logging.exception(e)
