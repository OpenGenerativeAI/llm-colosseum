run:
	diambra -r ~/.diambra/roms run -l python3 script.py

demo:
	diambra -r ~/.diambra/roms run -l python3 demo.py && python3 result.py

local:
	diambra -r ~/.diambra/roms run -l python3 ollama.py

install:
	pip3 install -r requirements.txt

go:
	while true; do make run; done