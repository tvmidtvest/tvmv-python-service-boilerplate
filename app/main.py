import config

# Put this in all files that use the logger
logger = config.get_logger(__name__)


def example_function() -> None:
    """ Example function."""

    logger.info("Example function called")


def main() -> None:
    """ Main function."""

    example_function()


if __name__ == '__main__':
    main()
