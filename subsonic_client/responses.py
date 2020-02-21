from .types import (
    Album,
    Artist,
    ArtistAlbum,
    Genres,
    IdName,
    Index,
    Indexes,
    MusicDirectory,
    MusicFolders,
    Subdirectory,
    Response,
    Track,
)


def ping(data):
    return Response(**data)


def getLicense(data):
    return Response(**data)


def getMusicFolders(data):
    obj_key = "musicFolder"
    list_key = "musicFolders"

    if type(data[list_key]) is dict:
        folders = data[list_key][obj_key]
    else:
        folders = data[list_key]
    return MusicFolders([IdName(m["id"], m["name"]) for m in folders])


def getIndexes(data):
    def to_artists(dicts):
        return [IdName(a["id"], a["name"]) for a in dicts]

    return Indexes(
        [Index(o["name"], to_artists(o["artist"])) for o in data["indexes"]["index"]]
    )


def getMusicDirectory(data):
    o = data["directory"]

    def to_child(o):
        if o["isDir"]:
            return Subdirectory(**o)
        return Track(**o)

    o["child"] = [to_child(c) for c in o["child"]]
    return MusicDirectory(**o)


def getGenres(data):
    return Genres([o["value"] for o in data["genres"]["genre"]])


def getArtists(data):
    return Indexes([
            Index(o["name"], _to_artists(o["artist"]))
            for o in data["artists"]["index"]
        ])


def getArtist(data):
    data = data["artist"]
    data["album"] = [ArtistAlbum(**a) for a in data["album"]]

    return Artist(**data)


def getAlbum(data):
    data = data["album"]
    data["song"] = [Track(**t) for t in data["song"]]
    return Album(**data)


# getAlbum
# getSong
# getVideos
# getVideoInfo
# getArtistInfo
# getArtistInfo2
# getAlbumInfo
# getAlbumInfo2
# getSimilarSongs
# getSimilarSongs2
# getTopSongs
# getAlbumList
# getAlbumList2
# getRandomSongs
# getSongsByGenre
# getNowPlaying
# getStarred
# getStarred2
# search
# search2
# search3
# getPlaylists
# getPlaylist
# createPlaylist
# updatePlaylist
# deletePlaylist
# stream
# download
# hls
# getCaptions
# getCoverArt
# getLyrics
# getAvatar
# star
# unstar
# setRating
# scrobble
# getShares
# createShare
# updateShare
# deleteShare
# getPodcasts
# getNewestPodcasts
# refreshPodcasts
# createPodcastChannel
# deletePodcastChannel
# deletePodcastEpisode
# downloadPodcastEpisode
# jukeboxControl
# getInternetRadioStations
# createInternetRadioStation
# updateInternetRadioStation
# deleteInternetRadioStation
# getChatMessages
# addChatMessage
# getUser
# getUsers
# createUser
# updateUser
# deleteUser
# changePassword
# getBookmarks
# createBookmark
# deleteBookmark
# getPlayQueue
# savePlayQueue
# getScanStatus
# startScan


def _to_artists(dicts):
    return [IdName(a["id"], a["name"]) for a in dicts]


class Ping(Response):
    def __init__(self, response):
        super().__init__(response)

    def pretty(self):
        return self.status


class GetLicense(Response):
    def __init__(self, response):
        super().__init__(response)
        self.license = response["license"]

    def pretty(self):
        return self.license


class GetMusicFolders(Response):
    _obj_key = "musicFolder"
    _list_key = "musicFolders"

    def __init__(self, response):
        super().__init__(response)
        if type(response[self._list_key]) is dict:
            folders = response[self._list_key][self._obj_key]
        else:
            folders = response[self._list_key]
        self.folders = [IdName(m["id"], m["name"]) for m in folders]

    def pretty(self):
        return "\n".join(f"{f.id}\t{f.name}" for f in self.folders)


class GetIndexes(Response):
    def __init__(self, response):
        super().__init__(response)

        self.artists = [
            Index(o["name"], self.to_artists(o["artist"]))
            for o in response["indexes"]["index"]
        ]

    def pretty(self):
        return "\n".join(
            [f"{i.name}\t{a.id}\t{a.name}" for i in self.indexes for a in i.artists]
        )


class GetAlbum(Response):
    pass


class GetSong(Response):
    pass


class GetVideos(Response):
    pass


class GetVideoInfo(Response):
    pass


class GetArtistInfo(Response):
    pass


class GetArtistInfo2(Response):
    pass


class GetAlbumInfo(Response):
    pass


class GetAlbumInfo2(Response):
    pass


class GetSimilarSongs(Response):
    pass


class GetSimilarSongs2(Response):
    pass


class GetTopSongs(Response):
    pass


class GetAlbumList(Response):
    pass


class GetAlbumList2(Response):
    pass


class GetRandomSongs(Response):
    pass


class GetSongsByGenre(Response):
    pass


class GetNowPlaying(Response):
    pass


class GetStarred(Response):
    pass


class GetStarred2(Response):
    pass


class Search(Response):
    pass


class Search2(Response):
    pass


class Search3(Response):
    pass


class GetPlaylists(Response):
    pass


class GetPlaylist(Response):
    pass


class CreatePlaylist(Response):
    pass


class UpdatePlaylist(Response):
    pass


class DeletePlaylist(Response):
    pass


class Stream(Response):
    pass


class Download(Response):
    pass


class Hls(Response):
    pass


class GetCaptions(Response):
    pass


class GetCoverArt(Response):
    pass


class GetLyrics(Response):
    pass


class GetAvatar(Response):
    pass


class Star(Response):
    pass


class Unstar(Response):
    pass


class SetRating(Response):
    pass


class Scrobble(Response):
    pass


class GetShares(Response):
    pass


class CreateShare(Response):
    pass


class UpdateShare(Response):
    pass


class DeleteShare(Response):
    pass


class GetPodcasts(Response):
    pass


class GetNewestPodcasts(Response):
    pass


class RefreshPodcasts(Response):
    pass


class CreatePodcastChannel(Response):
    pass


class DeletePodcastChannel(Response):
    pass


class DeletePodcastEpisode(Response):
    pass


class DownloadPodcastEpisode(Response):
    pass


class JukeboxControl(Response):
    pass


class GetInternetRadioStations(Response):
    pass


class CreateInternetRadioStation(Response):
    pass


class UpdateInternetRadioStation(Response):
    pass


class DeleteInternetRadioStation(Response):
    pass


class GetChatMessages(Response):
    pass


class AddChatMessage(Response):
    pass


class GetUser(Response):
    pass


class GetUsers(Response):
    pass


class CreateUser(Response):
    pass


class UpdateUser(Response):
    pass


class DeleteUser(Response):
    pass


class ChangePassword(Response):
    pass


class GetBookmarks(Response):
    pass


class CreateBookmark(Response):
    pass


class DeleteBookmark(Response):
    pass


class GetPlayQueue(Response):
    pass


class SavePlayQueue(Response):
    pass


class GetScanStatus(Response):
    pass


class StartScan(Response):
    pass


_RESPONSES = {
    "ping": Ping,
    "getLicense": GetLicense,
    "getMusicFolders": GetMusicFolders,
    "getIndexes": GetIndexes,
    "getAlbum": GetAlbum,
    "getSong": GetSong,
    "getVideos": GetVideos,
    "getVideoInfo": GetVideoInfo,
    "getArtistInfo": GetArtistInfo,
    "getArtistInfo2": GetArtistInfo2,
    "getAlbumInfo": GetAlbumInfo,
    "getAlbumInfo2": GetAlbumInfo2,
    "getSimilarSongs": GetSimilarSongs,
    "getSimilarSongs2": GetSimilarSongs2,
    "getTopSongs": GetTopSongs,
    "getAlbumList": GetAlbumList,
    "getAlbumList2": GetAlbumList2,
    "getRandomSongs": GetRandomSongs,
    "getSongsByGenre": GetSongsByGenre,
    "getNowPlaying": GetNowPlaying,
    "getStarred": GetStarred,
    "getStarred2": GetStarred2,
    "search": Search,
    "search2": Search2,
    "search3": Search3,
    "getPlaylists": GetPlaylists,
    "getPlaylist": GetPlaylist,
    "createPlaylist": CreatePlaylist,
    "updatePlaylist": UpdatePlaylist,
    "deletePlaylist": DeletePlaylist,
    "stream": Stream,
    "download": Download,
    "hls": Hls,
    "getCaptions": GetCaptions,
    "getCoverArt": GetCoverArt,
    "getLyrics": GetLyrics,
    "getAvatar": GetAvatar,
    "star": Star,
    "unstar": Unstar,
    "setRating": SetRating,
    "scrobble": Scrobble,
    "getShares": GetShares,
    "createShare": CreateShare,
    "updateShare": UpdateShare,
    "deleteShare": DeleteShare,
    "getPodcasts": GetPodcasts,
    "getNewestPodcasts": GetNewestPodcasts,
    "refreshPodcasts": RefreshPodcasts,
    "createPodcastChannel": CreatePodcastChannel,
    "deletePodcastChannel": DeletePodcastChannel,
    "deletePodcastEpisode": DeletePodcastEpisode,
    "downloadPodcastEpisode": DownloadPodcastEpisode,
    "jukeboxControl": JukeboxControl,
    "getInternetRadioStations": GetInternetRadioStations,
    "createInternetRadioStation": CreateInternetRadioStation,
    "updateInternetRadioStation": UpdateInternetRadioStation,
    "deleteInternetRadioStation": DeleteInternetRadioStation,
    "getChatMessages": GetChatMessages,
    "addChatMessage": AddChatMessage,
    "getUser": GetUser,
    "getUsers": GetUsers,
    "createUser": CreateUser,
    "updateUser": UpdateUser,
    "deleteUser": DeleteUser,
    "changePassword": ChangePassword,
    "getBookmarks": GetBookmarks,
    "createBookmark": CreateBookmark,
    "deleteBookmark": DeleteBookmark,
    "getPlayQueue": GetPlayQueue,
    "savePlayQueue": SavePlayQueue,
    "getScanStatus": GetScanStatus,
    "startScan": StartScan,
}


def get_response_class(name: str):
    return _RESPONSES.get(name)
