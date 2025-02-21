import matplotlib.pyplot as plt
import numpy as np

# Data Results with the following sample amount:
    # samples_by_size = 15

# 100.000 - 1.000.000
# data = [
#     [100000, 1404.0708541870117, 86.95125579833984, 0.0, 201.8451690673828],
#     [200000, 3226.8285751342773, 580.6684494018555, 493.47877502441406, 404.8347473144531],
#     [300000, 4084.920883178711, 808.9542388916016, 783.0381393432617, 892.6630020141602],
#     [400000, 6168.389320373535, 1211.2617492675781, 1186.966896057129, 1482.4628829956055],
#     [500000, 7299.78084564209, 1591.324806213379, 1399.1117477416992, 1518.9170837402344],
#     [600000, 8910.560607910156, 1793.980598449707, 1689.291000366211, 1789.9513244628906],
#     [700000, 10756.850242614746, 2199.2921829223633, 2200.4127502441406, 2181.220054626465],
#     [800000, 12396.073341369629, 2487.4210357666016, 2577.543258666992, 2503.323554992676],
#     [900000, 14169.502258300781, 3039.0262603759766, 2808.6423873901367, 2780.294418334961],
#     [1000000, 15824.675559997559, 3318.667411804199, 3183.3887100219727, 3185.4867935180664]
# ]

# 100 - 1000
# data = [
#     [100, 0.0, 0.0, 0.0, 0.0],
#     [200, 0.0, 0.0, 0.0, 0.0],
#     [300, 0.0, 0.0, 0.0, 0.0],
#     [400, 0.0, 0.0, 0.0, 0.0],
#     [500, 0.0, 0.0, 0.0, 0.0],
#     [600, 0.0, 0.0, 0.0, 0.0],
#     [700, 0.0, 0.0, 0.0, 0.0],
#     [800, 0.0, 0.0, 0.0, 0.0],
#     [900, 0.0, 0.0, 0.0, 0.0],
#     [1000, 0.0, 0.0, 0.0, 0.0]
# ]

# 1.000.000 - 10.000.000
data = [
    [1000000, 16693.25828552246, 3184.5808029174805, 3179.8362731933594, 3174.5195388793945],
    [2000000, 35866.16516113281, 6645.1311111450195, 6758.999824523926, 6876.802444458008],
    [3000000, 55269.86122131348, 10732.507705688477, 10448.288917541504, 10485.982894897461],
    [4000000, 77121.75846099854, 14258.837699890137, 15766.477584838867, 13772.392272949219],
    [5000000, 94636.05880737305, 17566.03717803955, 17387.080192565918, 17363.309860229492],
    [6000000, 114192.62886047363, 21381.711959838867, 20804.142951965332, 21287.894248962402],
    [7000000, 137366.29486083984, 25069.546699523926, 24837.303161621094, 25627.970695495605],
    [8000000, 153713.2978439331, 35598.087310791016, 29566.264152526855, 29433.465003967285],
    [9000000, 217803.4782409668, 63152.170181274414, 33752.9182434082, 33548.16436767578],
    [10000000, 370921.8978881836, 176120.7103729248, 192096.1618423462, 167450.76179504395]
]

sizes = [row[0] for row in data]
alg1 = [row[1] for row in data]  
alg2 = [row[2] for row in data]  
alg3 = [row[3] for row in data]  
alg4 = [row[4] for row in data]  

bar_width = 0.2
index = np.arange(len(sizes))

# Crear las barras para cada algoritmo
plt.bar(index, alg1, bar_width, label="Linear Search", color='blue')
plt.bar(index + bar_width, alg2, bar_width, label="Jump Search", color='green')
plt.bar(index + 2 * bar_width, alg3, bar_width, label="Binary Search", color='red')
plt.bar(index + 3 * bar_width, alg4, bar_width, label="Ternary Search", color='purple')

# Etiquetas y título
plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo (segundos)')
plt.title('Tiempos de ejecución de algoritmos de búsqueda')

# Configurar los ticks y la leyenda
plt.xticks(index + 1.5 * bar_width, sizes, rotation=45)
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
