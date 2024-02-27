import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

match os.getenv('APP_ENV'):
    case 'local':
        env_location: str = f'{os.getcwd()}/.env.local'
    case 'prod':
        env_location: str = f'{os.getcwd()}/.env'

load_dotenv(env_location, override=True)


class DatabaseSettings(BaseSettings):
    host: str = os.environ.get('MYSQL_HOST', '127.0.0.1')
    port: str = os.environ.get('MYSQL_PORT', '3306')
    name: Optional[str] = os.environ.get('MYSQL_DATABASE')
    user: Optional[str] = os.environ.get('MYSQL_USER')
    password: Optional[str] = os.environ.get('MYSQL_PASSWORD')


class ApplicationSettings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()

    PROJECT_NAME: str = "devgyurak.log"
    PROJECT_DESCRIPTION: str = "devgyurak.log Backend"


settings: ApplicationSettings = ApplicationSettings()
