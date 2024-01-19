from keras.models import load_model
import scipy.io as sio
import numpy as np
import sys
argc = len(sys.argv)

lengths = sys.argc
name = lengths[1]
output_name = lengths[2]
file = sio.loadmat('temp_file/'+name)

test_matrix = file['test_matrix'][:].ravel()
reads_number = file['current_reads_number'][:].ravel()
size2 = file['size2'][:].ravel()

test_matrix = np.reshape(test_matrix,(int(reads_number),int(size2)))
test_matrix = np.array(test_matrix)

result = list()

model1 = load_model('model_1.h5')
model2 = load_model('model_2.h5')
model3 = load_model('model_3.h5')
model4 = load_model('model_4.h5')
model5 = load_model('model_5.h5')

for i in range(int(reads_number)):
    result_pre = list()
    number = 0
    for j in range(int(size2)):
        test = test_matrix[i][j]
        
        if len(test)<=300:
            model = model1
            preds = model.predict(np.reshape(test,(1,300,20)))
            k = 300
            number = number+300
        elif (300<len(test)) and (len(test)<=500):
            model = model2
            preds = model.predict(np.reshape(test, (1, 500, 20)))
            k = 500
            number = number + 500
        elif (500<len(test)) and (len(test)<=1000):
            model = model3
            preds = model.predict(np.reshape(test, (1, 1000, 20)))
            k = 1000
            number = number + 1000
        elif (1000<len(test)) and (len(test)<=2000):
            model = model4
            preds = model.predict(np.reshape(test, (1, 2000, 20)))
            k = 2000
            number = number + 2000
         else:
            model = model4
            preds = model.predict(np.reshape(test, (1, 9000, 20)))
            k = 9000
            number = number + 9000
             
        result_pre.append(k*preds)

    result1 = np.sum(np.array(result_pre) / number)
    result.append(result1)
np.savetxt('result.csv',result)
