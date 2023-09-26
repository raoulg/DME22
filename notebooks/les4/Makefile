.PHONY: help run format lint

DEFAULT_GOAL := help

help:
	@echo "make run"
	@echo "       run the dashboard"
	@echo "make clean"
	@echo "       clean all files in data/processed except .gitkeep"

run:
	pdm run streamlit run dashboard.py

format:
	pdm run black dashboard.py

lint:
	pdm run ruff --fix dashboard.py
	pdm run mypy dashboard.py --ignore-missing-imports