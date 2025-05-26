from ultralytics import YOLO
import cv2

# Cargar el modelo entrenado
model = YOLO("runs/detect/train/weights/best.pt")

# Iniciar la cámara (0 = cámara integrada principal)
cap = cv2.VideoCapture(0)

# Verificar si se abrió la cámara correctamente
if not cap.isOpened():
    print("❌ No se pudo acceder a la cámara.")
    exit()

print("✅ Cámara encendida. Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer el frame de la cámara.")
        break

    # Hacer inferencia con YOLO
    results = model(frame)

    # Dibujar predicciones sobre la imagen
    annotated_frame = results[0].plot()

    # Mostrar la imagen en ventana
    cv2.imshow("Detección en vivo - YOLOv8", annotated_frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()