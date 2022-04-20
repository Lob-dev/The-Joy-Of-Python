from dataclasses import dataclass


@dataclass(frozen=True)
class ThumbnailRequest:
    filename: str
    file_store_path: str
    thumbnail_name: str
    thumbnail_store_path: str
