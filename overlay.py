import cv2
import numpy as np
import pygetwindow as gw
import win32gui
import win32ui
import win32con
from ultralytics import YOLO
from collections import deque

# Carregar o modelo treinado
model = YOLO(f"runs/detect/train4/weights/best.pt")

# Função para capturar a janela selecionada
def capture_window(window_title):
    # Encontra a janela pelo título
    window = gw.getWindowsWithTitle(window_title)
    if not window:
        print(f"Janela '{window_title}' não encontrada.")
        return None
    
    hwnd = window[0]._hWnd  # Identificador da janela

    # Obtém as dimensões da janela
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bot - top

    # Captura o conteúdo da janela
    hwin = win32gui.GetDesktopWindow()
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    # Converte para uma imagem OpenCV
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)  # BGRA

    # Limpa os objetos do Windows
    memdc.DeleteDC()
    win32gui.DeleteObject(bmp.GetHandle())

    # Converte de BGRA para BGR, descartando o canal alfa
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    return img

window_title = "Friends.MKV" 

# Iniciar loop de captura de janela e detecção
running = True

while running:
    # Captura o conteúdo da janela
    frame = capture_window(window_title)
    if frame is None:
        break

    # Realizar a detecção com o modelo YOLO
    results = model(frame, stream=True)

    # Plotar as caixas de detecção no frame
    for result in results:
        for box in result.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            x1, y1, x2, y2 = map(int, box[:4])
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Exibir o frame com as boxes
    cv2.imshow("Detection", frame)

    # Capturar tecla pressionada
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # 'q' ou 'ESC'
        running = False

# Libere as janelas
cv2.destroyAllWindows()
