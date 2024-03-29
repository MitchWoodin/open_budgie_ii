coverage:
	pytest --cov=open_budgie_ii --migrations -n 2 --dist loadfile
fcov:
	@echo "Running fast coverage check"
	@pytest --cov=features -n 4 --dist loadfile -q
