import sys
import asyncio

from bot.main import main


if __name__ == "__main__":
    # Check python version
    if sys.version_info < (3, 9):
        print("Python 3.9 or higher is required.")
        sys.exit(1)

    # Run the bot
    asyncio.run(main())
