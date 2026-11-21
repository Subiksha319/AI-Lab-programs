#IoT Sensor Data Analysis using NumPy
import numpy as np
sensor_data = np.array([24.5, 25.1 ,26.3,27.0,28.2,29.1,27.8,26.5,25.7,30.2])
print("Sensor Data:", sensor_data)
print("Mean    :" ,round(np.mean(sensor_data), 2))
print("Median  :" ,round(np.median(sensor_data), 2))
print("Minimum :" ,round(np.min(sensor_data), 2))
print("Maximum :" ,round(np.max(sensor_data), 2))
print("Std. Dev. :" ,round(np.std(sensor_data), 2))

threshold = 28.0
high_values = sensor_data[sensor_data > threshold]
print("values_above", threshold, ":" , high_values)