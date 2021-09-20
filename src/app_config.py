import os
import dotenv


class AppConfig:
    def __init__(self):
        dotenv.load_dotenv()
        self.ip = os.getenv("IP", default="0.0.0.0")
        self.port = os.getenv("PORT", default=8083)
