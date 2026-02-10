from pydantic import BaseSettings


class Config(BaseSettings):
    # DB
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "main"

    # 👇 שם ה־service של ה־DB ב־docker-compose
    MYSQL_HOST: str = "user-db"

    # 👇 בתוך Docker תמיד 3306
    MYSQL_PORT: str = "3306"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )

    # 👇 תקשורת פנימית בין containers
    POLL_SERVICE_BASE_URL: str = "http://poll-service:8081"

    class Config:
        env_file = ".env"
