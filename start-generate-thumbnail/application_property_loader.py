import sys
from typing import Dict

import yaml

from logger import logger

profile: str = sys.argv[1]


class ApplicationProperty:
    host: str
    port: int

    def __init__(self, root_key: str, conf: Dict) -> None:
        for key, value in conf.get(root_key).items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f'ApplicationProperty(host= {self.host}, port= {self.port})'


def load_application_property() -> ApplicationProperty:
    with open(f'application_property_{profile}.yaml', 'r', encoding='UTF8') as yaml_file:
        configuration = yaml.safe_load(yaml_file)
        application_property: ApplicationProperty = ApplicationProperty("app", configuration)

        logger.info(f'application_property= {application_property}')
        return application_property
