import numpy as np


times_agoras = [56.7, 73.53, 62.55, 55.01, 57.55, 75.89, 80, 91.7, 86.69,
81, 71.93, 58.8, 60.37, 60.37, 67, 73.43, 78.71, 79.04, 100.03, 83.43, 77.31, 51.47, 60.37, 67.08]

posotita_energeias = [12, 30,
15,67,56, 43, 32, 15, 46, 48,96, 123, 12, 7, 69, 3, 60, 213, 34, 56, 78, 22, 56, 78]

energy_prices = np.array(times_agoras)
quantity = np.array(posotita_energeias)

energy_by_six = energy_prices.reshape(4,6)

print(energy_by_six)

print(np.sum(energy_prices * quantity))

print(np.sum(posotita_energeias))

for row in energy_by_six:
    print('%.2f' % np.min(row))

for row in energy_by_six:
    print('%.2f' % np.mean(row))


energy_prices_sorted = np.sort(energy_prices)

print(energy_prices_sorted)