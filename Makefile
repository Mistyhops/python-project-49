install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	python -V
	uv tool install dist/*.whl
