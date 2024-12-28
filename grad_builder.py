from conf.config import Config
from gui.app import GradBuilderApp

if __name__ == "__main__":
    config = Config(lang="en")
    app = GradBuilderApp(config)
    app.run()