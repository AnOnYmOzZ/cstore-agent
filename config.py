from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "cstore agent"
VERSION = "1.0.0"

CMD_CENTER_URL = config("CMD_CENTER_URL", cast=str)

