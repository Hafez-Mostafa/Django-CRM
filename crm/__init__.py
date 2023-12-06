__all__ = [
    "__version__",
]

PACKAGE_NAME = "django-bootstrap-v5"

try:
    from importlib.metadata import metadata
except ImportError:
    from importlib_metadata import metadata

__version__ = metadata(PACKAGE_NAME)["Version"]
