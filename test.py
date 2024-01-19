from keras.models import load_model
import scipy.io as sio
import numpy as np
import sys
argc = len(sys.argv)

lengths = sys.argc
name = lengths[1]
output_name = lengths[2]
file = sio.loadmat('test.csv')

test_matrix = file['test_matrix'][:].ravel()
reads_number = 10000 # set as your own query sequences file 
size2 = file['size2'][:].ravel()

test_matrix = np.reshape(test_matrix,(int(reads_number),int(size2)))
test_matrix = np.array(test_matrix)

result = list()

model1 = load_model('model.h5')

for i in range(int(reads_number)):
    result_pre = list()
    number = 0
    for j in range(int(size2)):
        
        model = model1
        preds = model.predict(np.reshape(test, (1, 9000, 20)))
        k = 9000
        number = number + 9000  
             
    result_pre.append(k*preds)
    result1 = np.sum(np.array(result_pre) / number)
    result.append(result1)
np.savetxt('result.csv',result)
