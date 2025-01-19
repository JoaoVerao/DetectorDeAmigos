import cv2
import numpy as np
import torch 
from ultralytics import YOLO

# Carregar o modelo YOLO treinado
model = YOLO('runs/detect/train3/weights/best.pt')

# Iniciar a captura da webcam
cap = cv2.VideoCapture(0)

def cor(cls):
    if cls==0:
        return (0, 255, 0)
    else:
        return (0, 0, 255)

while True:
    # Captura um frame da webcam
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar imagem")
        break
    
    # Realizar a detecção com o modelo YOLO
    results = model(frame)
    
    for result in results:
        for box in result.boxes.data.tolist():
            x, y, x2, y2, conf, cls = box
            x, y, x2, y2 = map(int, box[:4])
            if conf > 0.6:  # Ajustar o limiar de confiança
                # Desenhar a caixa delimitadora ao redor do rosto detectado
                label = f"{model.names[int(cls)]} {conf:.2f}"
                cv2.rectangle(frame, (int(x), int(y)),
                            (int(x2), int(y2)), cor(cls), 2)
                cv2.putText(frame, label, (int(x), int(y) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor(cls), 2)
    
    
    # Exibir o frame com as detecções
    cv2.imshow('Detecção de Rosto', frame)

    # Interromper com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura da webcam e fechar a janela
cap.release()
cv2.destroyAllWindows()
