
from .main import main
from .config import config

options = config["DEFAULT"]



if __name__=="__main__":
    options = {}
    options["webdriver"] = config["DEFAULT"].get('webdriver')
    options["url"] = config["DEFAULT"].get('url')
    options["username"] = config["DEFAULT"].get('username')
    options["password"] = config["DEFAULT"].get('password')
    options["domain"] = config["DEFAULT"].get('domain')

    options["fullscreen"] = config["DEFAULT"].getboolean("fullscreen", False)
    options["auto_close_browser"] = config["DEFAULT"].getboolean("auto_close_browser", True)

    main(**options)
