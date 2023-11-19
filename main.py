import cv2
import numpy as np

# Carregando a imagem em escala de cinza
buildingBW = cv2.imread('C:\\Users\\rianb\\Downloads\\walt-disney-center-1629173_1920.jpg', 0)

# Redimensionando a imagem para a metade do tamanho original
height, width = buildingBW.shape[:2]
buildingBW_resized = cv2.resize(buildingBW, (width // 2, height // 2))

# Detectando cantos usando Shi-Tomasi na imagem redimensionada
corners = cv2.goodFeaturesToTrack(buildingBW_resized, maxCorners=50000, qualityLevel=0.01, minDistance=10)

# Convertendo as coordenadas para inteiros
corners = np.int0(corners)

# Criando uma imagem colorida para sobrepor os cantos
building_colored = cv2.cvtColor(buildingBW_resized, cv2.COLOR_GRAY2BGR)

# Desenhando círculos nos cantos detectados
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(building_colored, (x, y), 3, [0, 255, 0], -1)

# Exibindo a imagem redimensionada com os cantos destacados
cv2.imshow('Cantos Detectados (Redimensionado)', building_colored)
cv2.imwrite('building_colored.jpg', building_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()
