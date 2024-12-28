from conf.config import Config
from core.cli import GradBuilderCLI

if __name__ == "__main__":
    config = Config(lang="en")
    cli = GradBuilderCLI(config)
    cli.run()