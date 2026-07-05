from importlib import import_module
from os import getenv


class Config:
    ARCHIVE_LIMIT = 0
    AS_DOCUMENT = False
    AUTHORIZED_CHATS = ""
    AUTHOR_NAME = "HEARTXBOTS"
    AUTHOR_URL = "https://t.me/HEARTXBOTS"
    BASE_URL = ""
    BASE_URL_PORT = 80
    BOT_MAX_TASKS = 0
    BOT_PM = False
    BOT_TOKEN = ""
    BUZZHEAVIER_API = ""
    CLEAN_LOG_MSG = False
    CLONE_LIMIT = 0
    CMD_SUFFIX = ""
    DATABASE_URL = ""
    DEFAULT_LANG = "en"
    DEFAULT_UPLOAD = "rc"
    DEBRID_LINK_API = ""
    DELETE_LINKS = False
    DIRECT_LIMIT = 0
    DISABLE_BULK = False
    DISABLE_FF_MODE = False
    DISABLE_LEECH = False
    DISABLE_MULTI = False
    DISABLE_SEED = False
    DISABLE_TORRENTS = False
    EQUAL_SPLITS = False
    EXCLUDED_EXTENSIONS = ""
    EXTRACT_LIMIT = 0
    FFMPEG_CMDS = {}
    FILELION_API = ""
    FORCE_SUB_IDS = ""
    GD_DESP = "Uploaded with HEARTXBOTS"
    GD_DL_LIMIT = 0
    GDRIVE_ID = ""
    GOFILE_API = ""
    GOFILE_FOLDER_ID = ""
    HELPER_TOKENS = ""
    HYBRID_LEECH = True
    HYDRA_API_KEY = ""
    HYDRA_IP = ""
    HYPER_THREADS = 0
    IMDB_TEMPLATE = ""
    INCOMPLETE_TASK_NOTIFIER = False
    INDEX_URL = ""
    INSTADL_API = ""
    IS_TEAM_DRIVE = False
    JD_EMAIL = ""
    JD_LIMIT = 0
    JD_PASS = ""
    LEECH_CAPTION = ""
    LEECH_DUMP_CHAT = ""
    LEECH_FONT = ""
    LEECH_LIMIT = 0
    LEECH_PREFIX = ""
    LEECH_SPLIT_SIZE = 2097152000
    LEECH_SUFFIX = ""
    LINKS_LOG_ID = ""
    LOGIN_PASS = ""
    MEDIA_GROUP = False
    MEDIA_STORE = True
    MEGA_EMAIL = ""
    MEGA_LIMIT = 0
    MEGA_PASSWORD = ""
    MIRROR_LOG_ID = ""
    NAME_SWAP = ""
    NZB_LIMIT = 0
    OWNER_ID = 0
    PIXELDRAIN_KEY = ""
    PLAYLIST_LIMIT = 0
    PROTECTED_API = ""
    QUEUE_ALL = 0
    QUEUE_DOWNLOAD = 0
    QUEUE_UPLOAD = 0
    RC_DL_LIMIT = 0
    RCLONE_FLAGS = ""
    RCLONE_PATH = ""
    RCLONE_SERVE_PASS = ""
    RCLONE_SERVE_PORT = 8080
    RCLONE_SERVE_URL = ""
    RCLONE_SERVE_USER = ""
    RSS_CHAT = ""
    RSS_DELAY = 600
    RSS_SIZE_LIMIT = 0
    SEARCH_API_LINK = ""
    SEARCH_LIMIT = 0
    SEARCH_PLUGINS = []
    SET_COMMANDS = True
    SHOW_CLOUD_LINK = True
    STATUS_LIMIT = 10
    STATUS_UPDATE_INTERVAL = 15
    STOP_DUPLICATE = False
    STORAGE_LIMIT = 0
    STREAMWISH_API = ""
    SUDO_USERS = ""
    TELEGRAM_API = 0
    TELEGRAM_HASH = ""
    TG_PROXY = None
    THUMBNAIL_LAYOUT = ""
    TIMEZONE = "Asia/Kolkata"
    TORRENT_LIMIT = 0
    TORRENT_TIMEOUT = 0
    UPDATE_PKGS = True
    UPLOAD_PATHS = {}
    UPSTREAM_BRANCH = "master"
    UPSTREAM_REPO = ""
    USENET_SERVERS = []
    USER_MAX_TASKS = 0
    USER_SESSION_STRING = ""
    USER_TIME_INTERVAL = 0
    USER_TRANSMISSION = True
    USE_SERVICE_ACCOUNTS = False
    VERIFY_TIMEOUT = 0
    WEB_PINCODE = True
    YT_CATEGORY_ID = 22
    YT_DESP = "Uploaded with HEARTXBOTS bot"
    YT_DLP_OPTIONS = {}
    YT_PRIVACY_STATUS = "unlisted"
    YT_TAGS = ["telegram", "bot", "youtube"]

    @classmethod
    def get(cls, key):
        return getattr(cls, key) if hasattr(cls, key) else None

    @classmethod
    def set(cls, key, value):
        if hasattr(cls, key):
            value = cls._convert_env_type(key, value)
            setattr(cls, key, value)
        else:
            raise KeyError(f"{key} is not a valid configuration key.")

    @classmethod
    def get_all(cls):
        return {
            key: getattr(cls, key)
            for key in cls.__dict__.keys()
            if not key.startswith("__") and not callable(getattr(cls, key))
        }

    @classmethod
    def load(cls):
        cls.load_config()
        cls.load_env()

    @classmethod
    def load_config(cls):
        try:
            settings = import_module("config")
        except ModuleNotFoundError:
            return
        for attr in dir(settings):
            if hasattr(cls, attr):
                value = getattr(settings, attr)
                if not value:
                    continue
                if isinstance(value, str):
                    value = value.strip()
                if attr == "DEFAULT_UPLOAD" and value != "gd":
                    value = "rc"
                elif attr in [
                    "BASE_URL",
                    "RCLONE_SERVE_URL",
                    "INDEX_URL",
                    "SEARCH_API_LINK",
                ]:
                    if value:
                        value = value.strip("/")
                elif attr == "USENET_SERVERS":
                    try:
                        if not value[0].get("host"):
                            continue
                    except Exception:
                        continue
                setattr(cls, attr, value)
        for key in ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]:
            value = getattr(cls, key)
            if isinstance(value, str):
                value = value.strip()
            if not value:
                raise ValueError(f"{key} variable is missing!")

    @classmethod
    def load_env(cls):
        config_vars = cls.get_all()
        for key in config_vars:
            env_value = getenv(key)
            if env_value is not None:
                converted_value = cls._convert_env_type(key, env_value)
                cls.set(key, converted_value)

    @classmethod
    def _convert_env_type(cls, key, value):
        original_value = getattr(cls, key, None)
        if original_value is None:
            return value
        elif isinstance(original_value, bool):
            if isinstance(value, bool):
                return value
            return str(value).lower() in ("true", "1", "yes")
        elif isinstance(original_value, int):
            if isinstance(value, int):
                return value
            try:
                return int(value)
            except (ValueError, TypeError):
                return original_value
        elif isinstance(original_value, float):
            if isinstance(value, float):
                return value
            try:
                return float(value)
            except (ValueError, TypeError):
                return original_value
        return value

    @classmethod
    def load_dict(cls, config_dict):
        for key, value in config_dict.items():
            if hasattr(cls, key):
                if key == "DEFAULT_UPLOAD" and value != "gd":
                    value = "rc"
                elif key in [
                    "BASE_URL",
                    "RCLONE_SERVE_URL",
                    "INDEX_URL",
                    "SEARCH_API_LINK",
                ]:
                    if value:
                        value = value.strip("/")
                elif key == "USENET_SERVERS":
                    try:
                        if not value[0].get("host"):
                            value = []
                    except Exception:
                        value = []
                value = cls._convert_env_type(key, value)
                setattr(cls, key, value)
        for key in ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]:
            value = getattr(cls, key)
            if isinstance(value, str):
                value = value.strip()
            if not value:
                raise ValueError(f"{key} variable is missing!")


class BinConfig:
    ARIA2_NAME = "heartaria"
    QBIT_NAME = "heartbit"
    FFMPEG_NAME = "heartforge"
    RCLONE_NAME = "heartclone"
    SABNZBD_NAME = "heartsab"
