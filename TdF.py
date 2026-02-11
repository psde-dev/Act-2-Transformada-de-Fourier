import numpy as npy
import matplotlib.pyplot as plot

#linespace
#(inicio,fin,cantidad) - Se crea un arreglo de números espaciados igualmente entre dos calores.

fs = 1000  # Frecuencia de muestreo (Hz)
t = npy.linspace(0, 1, 500)

#Señales

# Señal senoidal
f = 5 
# señal original
seno = npy.sin(2 * npy.pi * f * t)

#señal desplazada 0.5 s 
seno_desplazada = npy.sin(2*npy.pi*5*(t-0.1))

# Pulso rectangular
pulso = npy.where((t >= 0.3) & (t <= 0.6), 1, 0)

# Función escalón
escalon = npy.where(t >= 0.5, 1, 0)

#Transformada de Fourier
def calcular_fft(signal):
  N = len(signal)
  fft = npy.fft.fft(signal)
  frec = npy.fft.fftfreq(N, 1/fs)
  return frec, npy.abs(fft)

#FFT
f_seno, fft_seno = calcular_fft(seno)
fft_seno_desplazada = npy.fft.fft(seno_desplazada)
f_pulso, fft_pulso = calcular_fft(pulso)
f_escalon, fft_escalon = calcular_fft(escalon)
fft_seno = npy.fft.fft(seno)


#Propiedad de linealidad 
suma = seno + pulso 

#FFT de la suma 
f_suma, fft_suma = calcular_fft(suma)

#Las gráficas de la información obtenida previamente
plot.figure(figsize=(12,8))
plot.figure(figsize=(10,6))
plot.subplot(3,2,1)
plot.plot(t, seno)
plot.title("Senoidal - Tiempo")

plot.subplot(3,2,1)
plot.plot(t, seno_desplazada)
plot.title("Magnitud de la Transformada de Fourier- Señal Senoidal Desplazada")
plot.subplot(3,2,2)
plot.plot(f_seno, fft_seno)
plot.title("Senoidal - Frecuencia")

plot.subplot(3,2,3)
plot.plot(t, pulso)
plot.title("Pulso Rectangular - Tiempo")

plot.subplot(3,2,4)
plot.plot(f_pulso, fft_pulso)
plot.title("Pulso Rectangular - Frecuencia")

plot.subplot(3,2,5)
plot.plot(t, escalon)
plot.title("Escalón - Tiempo")

plot.subplot(3,2,6)
plot.plot(f_escalon, fft_escalon)
plot.title("Escalón - Frecuencia")


#Suma
plot.figure()

plot.subplot(2,1,1)
plot.plot(t, suma)
plot.title("Suma de señales - Tiempo")

plot.subplot(2,1,2)
plot.plot(f_suma, fft_suma)
plot.title("Suma de señales - Frecuencia")

# Graficar
plot.figure(figsize=(10,6))


#Frecuencia Comprimida vs Expandida vs Frecuencia
señal_comprimido = npy.sin(2*npy.pi*f*(t*0.5))
seno_expandida = npy.sin(2*npy.pi*f*(t*2))


#Señal comprimida
plot.subplot(3,1,2)
plot.plot(t, señal_comprimido)
plot.title("Señal expandida")


#Señal expandida
plot.subplot(3,1,3)
plot.plot(t, seno_expandida)
plot.title("Señal comprimida")


plot.tight_layout()

plot.show()
