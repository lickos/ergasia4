import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ημερήσια κλιματικά δεδομένα
climate_data = {
    'Πόλη': ['Αλεξανδρούπολη', 'Φέρες', 'Σουφλί', 'Διδυμότειχο', 'Ορεστιάδα'],
    'Θερμοκρασία': [21, 20, 17, 19, 20],
    'Υγρασία': [89, 78, 80, 86, 90],
    'Υετός': [56.7, 64.3, 59.1, 48.9, 47.6]
}

# Α. Δημιουργία DataFrame
# Δημιουργήστε ένα pandas DataFrame για τον χειρισμό των ημερήσιων κλιματικών δεδομένων

pd_dataframe = pd.DataFrame(climate_data)



# Β1. Συνάρτηση προβολής κλιματικών δεδομένων
def display_climate_info():
    # Υλοποίηση της συνάρτησης προβολής κλιματικών δεδομένων
    print(pd_dataframe)

# Β2. Συνάρτηση υπολογισμού περιγραφικών στατιστικών (descriptive statistics)
def calculate_descriptive_statistics():
    # Υλοποίηση της συνάρτησης υπολογισμού περιγραφικών στατιστικών (descriptive statistics)
    print(pd_dataframe.describe())

# Β3. Συνάρτηση υπολογισμού μέσης θερμοκρασίας
def calculate_average_temp():
    # Υλοποίηση της συνάρτησης υπολογισμού μέσης θερμοκρασίας
    print(pd_dataframe['Θερμοκρασία'].mean())

# Β4. Συνάρτηση εκτύπωσης ραβδογράμματος (bar plot) υγρασίας
def plot_humidity():
    # Υλοποίηση της συνάρτησης εκτύπωσης ραβδογράμματος (bar plot) υγρασίας
    fig, ax = plt.subplots()
    poleis = pd_dataframe['Πόλη']
    humitidy = pd_dataframe['Υγρασία']
    ax.bar(poleis, humitidy)
    ax.set_ylabel('Υγρασία (%)')
    ax.set_title('Ραβδόγραμμα Υγρασίας')
    plt.show()

# Γ. Κύρια συνάρτηση
def main():
    # Υλοποίηση μενού επιλογών με βάση τις συναρτήσεις που έχετε δημιουργήσει
    display_climate_info()
    calculate_descriptive_statistics()
    calculate_average_temp()
    plot_humidity()

if __name__ == "__main__":
    main()
