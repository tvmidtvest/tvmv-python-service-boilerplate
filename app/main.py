import os

import config

# Put this in all files that use the logger
logger = config.get_logger(__name__)


def example_function(my_var: str) -> None:
    """ Example function."""

    logger.info(f"Example function called: {my_var}")


def main() -> None:
    """ Main function."""

    # Get an environment variable
    my_var = os.environ.get("MY_VAR")

    example_function(my_var)


if __name__ == '__main__':
    main()
