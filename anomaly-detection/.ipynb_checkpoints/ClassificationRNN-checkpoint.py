import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class Data:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.numeric_data = self.data.drop(columns=['timestamp', 'source', 'destination'])
        self.X = self.numeric_data.drop(columns=['protocol']).values
        self.Y = self.numeric_data['protocol'].values
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)

    def TrainTestSplit(self, trainTestSplitRatio=0.6):
        numeric_data = self.data.drop(columns=['timestamp', 'source', 'destination'])
        numeric_data['protocol'] = pd.Categorical(numeric_data['protocol']).codes
        self.X = numeric_data.drop(columns=['protocol']).values
        self.Y = numeric_data['protocol'].values
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)
        self.Y_encoded = to_categorical(self.Y)
        self.n_train = int(round(len(self.data) * trainTestSplitRatio, 0))
        self.trainX, self.testX = self.X_scaled[:self.n_train, :], self.X_scaled[self.n_train:, :]
        self.trainY, self.testY = self.Y_encoded[:self.n_train], self.Y_encoded[self.n_train:]
        self.trainY = np.argmax(self.trainY, axis=1)
        self.testY = np.argmax(self.testY, axis=1)
        return (self.trainX, self.trainY, self.testX, self.testY)

data_path = "~/Network-Monitoring-Security/anomaly-detection/TrainTest.csv"
data = Data(data_path)
trainX, trainY, testX, testY = data.TrainTestSplit()
input_dimensions = (trainX.shape[1], 1)
if len(trainY.shape) == 1:
    trainY_encoded = to_categorical(trainY)
    testY_encoded = to_categorical(testY)
else:
    trainY_encoded, testY_encoded = trainY, testY

model = Sequential([
    LSTM(64, activation='relu', input_shape=input_dimensions, return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dropout(0.2),
    Dense(4, activation='softmax')  
])

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
history = model.fit(trainX, trainY_encoded, epochs=50, batch_size=32, validation_data=(testX, testY_encoded))
loss, accuracy = model.evaluate(testX, testY_encoded)
print(f'Loss: {loss}, Accuracy: {accuracy}')

predicted_probs = model.predict(testX)
predicted_labels = np.argmax(predicted_probs, axis=1)
n_train = data.n_train
true_labels = data.Y[n_train:]

accuracy = accuracy_score(true_labels, predicted_labels)
print(f'Accuracy: {accuracy:.4f}')

precision = precision_score(true_labels, predicted_labels, average='macro')
recall = recall_score(true_labels, predicted_labels, average='macro')
f1 = f1_score(true_labels, predicted_labels, average='macro')

print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1:.4f}')

cm = confusion_matrix(true_labels, predicted_labels)
print('Confusion Matrix:')
print(cm)