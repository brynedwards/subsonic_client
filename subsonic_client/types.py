from collections import abc, namedtuple


class _Type:
    fields = tuple()

    def __init__(self, **kwargs):
        for f in self.fields:
            if type(f) is str:
                setattr(self, f, kwargs.get(f, None))
            elif type(f) is tuple:
                setattr(self, f[1], kwargs.get(f[0], None))


class Response(_Type):
    fields = ("status", "version")

    def __init__(self, data, **kwargs):
        self.data = data

        for f in self.fields:
            setattr(self, f, kwargs.get(f, None))

    def pretty(self):
        return self.status


class MusicFolders(list):
    def pretty(self):
        print("\n".join([f"{e.id}\t{e.name}" for e in self]))


class Album(_Type):
    fields = (
        "id",
        "name",
        "artist",
        "artistId",
        "coverArt",
        "created",
        "duration",
        "songCount",
        ("song", "tracks"),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        s = f"""Name: {self.name}
ID: {self.id}

Tracks
"""
        return s + "\n".join([t.pretty() for t in self.tracks])


class Artist(_Type):
    fields = ("id", "name", ("album", "albums"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        s = f"""Name: {self.name}
ID: {self.id}

Albums
"""
        return s + "\n".join([a.pretty() for a in self.albums])


class ArtistAlbum(_Type):
    fields = (
        "id",
        "name",
        "artist",
        "artistId",
        "coverArt",
        "created",
        "duration",
        "songCount",
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        return f"{self.id}\t{self.name}\t{self.artist}\t{self.created}"


class Genres(list):
    def pretty(self):
        return "\n".join(self)


class Indexes(list):
    def pretty(self):
        return "\n".join(
            [f"{i.name}\t{a.id}\t{a.name}" for i in self for a in i.artists]
        )


class MusicDirectory(_Type):
    fields = ("id", "name", "parent", ("child", "children"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        s = f"""Name: {self.name}
ID: {self.id}
Parent ID: {self.parent}

Contents
"""

        return s + "\n".join([c.pretty() for c in self.children])


class Child(_Type):
    fields = ("id", "title", "parent", "isDir", "isVideo", "album", "artist", "created")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Subdirectory(Child):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        return f"Subdir\t{self.id}\t{self.title}\t{self.parent}\t{self.album}\t{self.artist}\t{self.created}"


class Track(Child):
    fields = (
        "album",
        "albumId",
        "artist",
        "artistId",
        "bitRate",
        "contentType",
        "coverArt",
        "created",
        "discNumber",
        "duration",
        "genre",
        "id",
        "isDir",
        "isVideo",
        "parent",
        "path",
        "size",
        "suffix",
        "title",
        "track",
        "type",
        "year",
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pretty(self):
        return f"Track\t{self.id}\t{self.title}\t{self.parent}\t{self.album}\t{self.artist}\t{self.created}"


IdName = namedtuple("IdName", ("id", "name"))
Index = namedtuple("Index", ("name", "artists"))
