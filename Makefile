coverage:
	pytest --cov=open_budgie_ii --migrations
fcov:
	@echo "Running fast coverage check"
	@pytest --cov=open_budgie_ii -n 4 --dist loadfile -q
