#example 1
from keras.models import Sequential
from keras.layers import Merge, Activation, Dense
from keras.layers.recurrent import LSTM

n, m = 10, 3
input_dim = 10
output_dim = 20

first_model = Sequential()
first_model.add(LSTM(output_dim, input_shape=(m, input_dim)))

second_model = Sequential()
second_model.add(LSTM(output_dim, input_shape=(n-m, input_dim)))

model = Sequential()
model.add(Merge([first_model, second_model], mode='concat'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(optimizer='RMSprop', loss='binary_crossentropy')
model.fit([X[:,:m,:], X[:,m:,:]], y)







#example 2

embedding_layer_1 = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=50,
                            trainable=False)

embedding_layer_2 = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=50,
                            trainable=False)


s1rnn = Sequential()
s1rnn.add(embedding_layer_1)
s1rnn.add(LSTM(128, input_shape=(100, 1)))
s1rnn.add(Dense(1))

s2rnn = Sequential()
s2rnn.add(embedding_layer_2)
s2rnn.add(LSTM(128, input_shape=(100, 1)))
s2rnn.add(Dense(1))