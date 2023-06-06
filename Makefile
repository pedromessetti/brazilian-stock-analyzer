.SILENT:
# Color variables
RED = \033[1;31m
GREEN = \033[1;32m
WHITE = \033[1;37m
RESET = \033[0m

all: 
	python3 writer.py
	echo "$(GREEN)[OK]$(WHITE)tabela.csv$(RESET)"
	echo "$(GREEN)Analyzer starting..$(WHITE)"
	python3 analyzer.py	
	echo "$(RED)Killed"