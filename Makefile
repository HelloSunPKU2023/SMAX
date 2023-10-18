TESTS_DIR = 'tests'
TESTS = $(shell find $(TESTS_DIR) -name 'test_*.py')

test:
	@echo "Running tests..."
	@for test in $(TESTS); do \
		echo $$test; \
		python -m unittest $$test; \
	done

init:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt