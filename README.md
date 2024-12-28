conda create -n yolov10 python=3.9 (or: python -m venv yolov10)

conda activate yolov10 (or cd ./yolov10/Scripts/activate.bat)

pip install -r requirements.txt

pip install -e .

python app.py

visit http://127.0.0.1:7860
