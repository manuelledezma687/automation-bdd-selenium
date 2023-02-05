from typing import Dict
from pathlib import Path
from prettyconf import Configuration
from prettyconf.loaders import IniFile


class Properties:

    @classmethod
    def get_config(cls, args: Dict) -> Configuration:

        return Configuration(
            loaders=[
                IniFile(filename=str(
                    Path(__file__).parents[1] / f"properties/environments/{args.get('env')}.ini")),
                IniFile(filename=str(
                    Path(__file__).parents[1] / f"properties/defaults.ini"))
            ]
        )
