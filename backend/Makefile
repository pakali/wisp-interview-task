CURRENT_PATH=$(shell pwd)
CURRENT_DATE=$(shell date)

test:  
	PYTHONPATH=. pytest -o log_cli=true

build:
	docker build -t wisp . 
	
run:
	docker run -p 80:80 wisp