from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # Чтение изображения
    image_data = await file.read()
    
    # TODO: Обработайте изображение с помощью YOLO
    # Например, вызвать вашу модель YOLO для анализа
    result = "This is a dummy YOLO response. Replace with your YOLO output."

    return {"result": result}

if name == "main":
    uvicorn.run(app, host="127.0.0.1", port=8001)  # YOLO-контроллер работает на порту 8001 5788077