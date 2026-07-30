"""
Utility for loading configuration values from environment variables
with type coercion and default fallbacks.
"""

import os
from typing import Any, Type


def get_config_value(key: str, default: Any = None, cast: Type = str) -> Any:
    """
    Retrieve a configuration value from the environment.

    Args:
        key: The environment variable name.
        default: The default value if the variable is not set.
        cast: The type to cast the value to.

    Returns:
        The configuration value, cast to the specified type.
    """
    raw_value = os.environ.get(key)
    if raw_value is None:
        return default

    try:
        return cast(raw_value)
    except (TypeError, ValueError):
        return default


if __name__ == "__main__":
    print(get_config_value("PORT", default=8080, cast=int))
