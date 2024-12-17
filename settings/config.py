from pydantic import Field, AnyUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    max_login_attempts: int = Field(default=3, description="Background color of QR codes")
    
    # Server configuration
    server_base_url: AnyUrl = Field(default='http://localhost', description="Base URL of the server")
    server_download_folder: str = Field(default='downloads', description="Folder for storing downloaded files")
    
    # Security and authentication configuration
    secret_key: str = Field(default="secret-key", description="Secret key for encryption")
    algorithm: str = Field(default="HS256", description="Algorithm used for encryption")
    access_token_expire_minutes: int = Field(default=15, description="Expiration time for access tokens in minutes")
    jwt_secret_key: str = "a_very_secret_key"
    jwt_algorithm: str = "HS256"
    refresh_token_expire_minutes: int = 1440  # 24 hours for refresh token
    
    # Email settings for Mailtrap
    smtp_server: str = Field(default='smtp.mailtrap.io', description="SMTP server for sending emails")
    smtp_port: int = Field(default=2525, description="SMTP port for sending emails")
    smtp_username: str = Field(default='your-mailtrap-username', description="Username for SMTP server")
    smtp_password: str = Field(default='your-mailtrap-password', description="Password for SMTP server")
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Instantiate settings to be imported in your application
settings = Settings()
