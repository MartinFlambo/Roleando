import cv2

# Usa una cadena cruda para evitar problemas con las secuencias de escape
img_path = 'images/imagen.png'

# Lee la imagen
img = cv2.imread(img_path)
cv2.imshow('foto', img)
cv2.waitKey(0)
# Verifica si la imagen se cargó correctamente
