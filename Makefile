run:
	diambra -r ~/.diambra/roms run -l python3 script.py

demo:
	diambra -r ~/.diambra/roms run -l python3 mistral.py && python3 result.py

qwen:
	diambra -r ~/.diambra/roms run -l python3 qwen.py

install:
	pip3 install -r requirements.txt

go:
	while true; do make run; done