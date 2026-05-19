from ultralytics import YOLO

# Cargamos el modelo YOLO
model = YOLO("yolo11n.pt")

# Especificar la imagen o su URL (Asegúrate de tener solo 3 o agrega la 4ta si quieres)
source = ["./Detection_task/Inputs/001_image.jpg", "./Detection_task/Inputs/002_image.jpg", "./Detection_task/Inputs/003_image.jpg"]

# Realizamos la inferencia de YOLO
results = model(source)

# Visualizar los resultados
results[0].show()

for result in results:
    print("-----")
    print(result)
    print(result.boxes)
    result.show()