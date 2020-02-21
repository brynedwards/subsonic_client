import codecs
import logging

import requests

from subsonic_client.exceptions import ErrorResponse
from subsonic_client import responses

logger = logging.getLogger(__name__)


class Client:
    def __init__(self, base_url, username, password, client_name, format="json"):
        if base_url is None:
            raise Exception("Base URL not set")
        if username is None:
            raise Exception("Username not set")
        if password is None:
            raise Exception("Password not set")
        if client_name is None:
            raise Exception("Client name not set")
        self.base_url = base_url
        self.session = requests.Session()

        if format not in ["xml", "json", "jsonp"]:
            logger.warn(f"Non-standard format '{format}' specified.")

        p = codecs.encode(password.encode("ascii"), "hex").decode("ascii")
        self.params = (
            ("u", username),
            ("p", f"enc:{p}"),
            ("v", "1.9.0"),
            ("c", client_name),
            ("f", "json"),
        )
        # TODO ping() to check version

    def _get(self, endpoint, params=None):
        params = self.params + (params or tuple())
        response = self.session.get(f"{self.base_url}/{endpoint}.view", params=params)
        if response.status_code != 200:
            body = response.json()["subsonic-response"]["error"]
            raise ErrorResponse(response.status_code, body["code"], body["message"])
        return response.json()["subsonic-response"]


    def _to_response(self, method, params=None):
        return getattr(responses, method)(self._get(method, params))

    def ping(self, params=None):
        return self._to_response("ping")

    def getLicense(self, params=None):
        return self._to_response("getLicense")

    def getMusicFolders(self, params=None):
        return self._to_response("getMusicFolders")

    def getIndexes(self, params=None):
        return self._to_response("getIndexes", params)

    def getMusicDirectory(self, params=None):
        return self._to_response("getMusicDirectory", params)

    def getGenres(self, params=None):
        return self._to_response("getGenres", params)

    def getArtists(self, params=None):
        return self._to_response("getArtists", params)

    def getArtist(self, params=None):
        return self._to_response("getArtist", params)

    def getAlbum(self, params=None):
        return self._to_response("getAlbum", params)
