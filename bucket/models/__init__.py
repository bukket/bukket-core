# Sadly this ordering matters. Base must come first :(
from bucket.models.base import Base  # noqa: F401
from bucket.models.core import Factoid, Items, Vars, Values  # noqa: F401
