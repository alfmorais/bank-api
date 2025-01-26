format:
	@ruff check . --fix && ruff format .

start:
	@docker compose build --no-cache  && docker compose up