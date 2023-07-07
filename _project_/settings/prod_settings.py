import environs
from _project_.settings import BASE_DIR

env = environs.Env()
env.read_env(BASE_DIR / "_project_/settings/env/.env.prod")

SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# Database
DATABASES = {
    "default": {
        "ENGINE": env.str("POSTGRES_ENGINE"),
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
    }
}



