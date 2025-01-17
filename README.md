# DetecctorDeAmigos: Detecção de Personagens de *Friends* com Visão Computacional

## Descrição

Este repositório contém um projeto de visão computacional para detectar personagens da famosa série *Friends* em vídeos e imagens utilizando um modelo treinado. O modelo foi desenvolvido e treinado com um dataset manualmente curado, com o objetivo de identificar personagens como Ross, Rachel, Monica, Chandler, Phoebe e Joey.

## Objetivo

O objetivo principal deste projeto é demonstrar o uso de redes neurais para a detecção de personagens em um ambiente real. O modelo foi treinado de forma modesta, utilizando uma máquina local e um dataset de tamanho pequeno, mas com precisão otimizada para a tarefa.

## Passo a Passo

### 1. **Coleta de Dados**

O dataset foi coletado na plataforma [Kaggle](https://www.kaggle.com/datasets/amiralikalbasi/images-of-friends-character-for-face-recognition), com imagens dos atores da série *Friends* e criado as etiquetas com auxilio da plataforma [CVAT](cvat.com). As bounding box foram criadas uma a uma, imagem a imagem.

### 2. **Treinamento do Modelo**

Utilizei o modelo YOLO (You Only Look Once) para a tarefa de detecção de objetos. A escolha do YOLO se deu pela sua alta performance em tempo real. O treinamento foi realizado utilizando a biblioteca [Ultralytics YOLO](https://github.com/ultralytics/yolov5).

As configurações e código de treinamento estão no repositório.

### 3. **Ajustes e Testes**

Durante o treinamento, houve a necessidade de ajustes para melhorar a precisão do modelo. Diversos testes em tempo real foram realizados para validar a eficácia da detecção. O código de inferência está configurado para capturar imagens de uma janela ou tela, permitindo a detecção de personagens enquanto um vídeo é reproduzido.

### 4. **Captura de Vídeo**

Utilizei o OpenCV para capturar frames de vídeos e realizar a inferência em tempo real, desenhando caixas delimitadoras ao redor dos personagens detectados.

### 5. **Resultado Final**

Os resultados foram satisfatórios, com boa precisão na detecção dos personagens. Um vídeo demonstrativo foi gerado para ilustrar o funcionamento do modelo em tempo real.

### 6. **Vídeo de Demonstração**

O vídeo demonstrativo pode ser acessado no seguinte [link do Google Drive]([#](https://drive.google.com/drive/folders/1nPlf9R_vJX-BI7qtqRxB8XXpi56cQQEs?usp=sharing)), onde você pode ver o modelo realizando a detecção em tempo real.

## Tecnologias Usadas

- **Python**
- **OpenCV**
- **YOLO (Ultralytics YOLO)**
- **Google Drive (para compartilhamento do vídeo)**

## Como Rodar o Código

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/DetecctorDeAmigos.git

   pip install -r requirements.txt
   
   python overlay.py

2. Alterar a variavel window_title caso queira testar em outros videos:
    ```bash
    window_title="insira o nome do arquivo de video"
