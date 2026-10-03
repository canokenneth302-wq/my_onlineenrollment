"""Read-only inventory for the public Rabbit Software vector prefix."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional
from urllib.parse import quote
from urllib.request import Request, urlopen
from xml.etree import ElementTree

DEFAULT_BUCKET = "amzn-s3-rabbit-software"
DEFAULT_PREFIX = "vectors/"
S3_XML_NAMESPACE = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}


@dataclass(frozen=True)
class PublicVectorIndexStatus:
    bucket: str
    prefix: str
    reachable: bool
    object_count: int = 0
    error: Optional[str] = None

    def to_dict(self) -> dict:
        status = {
            "bucket": self.bucket,
            "prefix": self.prefix,
            "reachable": self.reachable,
            "object_count": self.object_count,
            "access": "public-read",
        }
        if self.error:
            status["error"] = self.error
        return status


class PublicVectorIndex:
    """Lists public vector objects without uploading research or identity data."""

    def __init__(self, bucket: Optional[str] = None, prefix: Optional[str] = None):
        self.bucket = bucket or os.getenv("RABBIT_VECTOR_BUCKET", DEFAULT_BUCKET)
        configured_prefix = prefix or os.getenv("RABBIT_VECTOR_PREFIX", DEFAULT_PREFIX)
        self.prefix = configured_prefix.rstrip("/") + "/"

    def list_keys(self, timeout: int = 10) -> list[str]:
        query = quote(self.prefix, safe="/")
        url = f"https://{self.bucket}.s3.amazonaws.com/?list-type=2&prefix={query}"
        request = Request(url, headers={"User-Agent": "Hello-World/1.0"})
        with urlopen(request, timeout=timeout) as response:
            root = ElementTree.fromstring(response.read())

        return [
            node.text
            for node in root.findall("s3:Contents/s3:Key", S3_XML_NAMESPACE)
            if node.text and node.text != self.prefix
        ]

    def status(self, timeout: int = 10) -> PublicVectorIndexStatus:
        try:
            return PublicVectorIndexStatus(
                bucket=self.bucket,
                prefix=self.prefix,
                reachable=True,
                object_count=len(self.list_keys(timeout)),
            )
        except (ElementTree.ParseError, OSError, ValueError) as exc:
            return PublicVectorIndexStatus(
                bucket=self.bucket,
                prefix=self.prefix,
                reachable=False,
                error=str(exc),
            )


if __name__ == "__main__":
    print(PublicVectorIndex().status().to_dict())
