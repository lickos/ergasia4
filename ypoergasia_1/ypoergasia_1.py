import pickle
import codecs

def centralize_first_part(name):
    spaces = int((9 - len(name)) / 2)
    formated_string = ' ' * spaces + name + ' ' * spaces
    return formated_string

def load(filename):
    try:
        with open(filename, 'rb') as my_file:
            pickled_file = pickle.load(my_file)
            return pickled_file
    except IOError:
        print('An error occured while openning the file')
        return []
    
def save(filename, reservation_list):
    reservation_list.sort(key=lambda a: a[1])
    try: 
        with codecs.open(filename, 'a', 'utf-8') as file:
            title1 = centralize_first_part('Δωμάτιο')
            title2 ="Πελάτης"
            file.write(title1 + title2 + '\n')
            for x in my_file:
                file.write(centralize_first_part(str(x[1])) + x[2] + ' ' + x[3] + '\n')
    except IOError:
        print('An error occured while saving the file')

my_file = load('./../my_reservations_20240407')

save('my_reservations_20240407.txt', my_file)
