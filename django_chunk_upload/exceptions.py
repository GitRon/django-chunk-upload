"""
Exceptions raised by django-chunk-upload.
"""


class ChunkUploadError(Exception):
    """
    Exception raised if errors in the request/process.
    """

    def __init__(self, status, **data):
        self.status_code = status
        self.data = data
