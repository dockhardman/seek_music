from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl

from seek_music.types.kkbox.album import Album


class Track(BaseModel):
    id: str
    name: str
    duration: int
    isrc: str
    url: HttpUrl
    track_number: int
    explicitness: bool
    available_territories: List[str]
    album: Optional[Album] = Field(None)
