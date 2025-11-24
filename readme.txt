docker compose up -d postgres redis

docker compose run --rm aerich aerich init -t app.config.TORTOISE_ORM

docker compose up -d fastapi celery celery_beat

При простом изменении кода:
docker compose restart fastapi

docker compose restart celery celery_beat

Пересборка контейнера, если изменил .env или установил новые библиотеки
docker compose up -d --build fastapi