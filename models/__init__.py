#!/usr/bin/python3
"""Models init package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
