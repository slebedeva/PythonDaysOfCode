.DEFAULT_GOAL := test

test:
	pytest

day1:
	python day1_swap_variables.py #-c 'from taxifare.interface.main import preprocess; preprocess()'


