# ----------------------------
# DOCKER SHORTCUTS
# ----------------------------

init:
	@docker compose up -d postgres redis
	@docker compose run --rm aerich aerich init -t app.config.TORTOISE_ORM
	@docker compose up -d fastapi celery celery_beat

restart:
	docker compose restart fastapi

restart-celery:
	docker compose restart celery

restart-celery-beat:
	docker compose restart celery_beat

re-build:
	docker compose up -d --build fastapi

re-build-celery:
	docker compose up -d --build celery

re-build-celery-beat:
	docker compose up -d --build celery_beat

migrate-up:
	docker compose run --rm aerich aerich migrate && \
	docker compose run --rm aerich aerich upgrade
