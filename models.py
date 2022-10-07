import tensorflow as tf
import numpy as np

class sequence_models:
    def __init__(self,):
        None
    
    def conv_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.Conv1D(16,5,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Conv1D(32,5,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model      
    
    def lstm_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.LSTM(32,activation='relu',return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.LSTM(32,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model

    def conv_lstm_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.ConvLSTM1D(16,5,activation='relu',return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.ConvLSTM1D(32,5,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model

    def rnn_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.SimpleRNN(32,activation='relu',return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.SimpleRNN(32,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model
    
    def nn_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model
    
    def gru_model(self,num_words,embedding_dims,max_len,embedding_matrix):
        model = tf.keras.Sequential([ 
            tf.keras.layers.Embedding(num_words+1, embedding_dims, input_length=max_len, weights=[embedding_matrix], trainable=False),
            tf.keras.layers.GRU(32,activation='relu',return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.GRU(32,activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(1,activation='sigmoid')])

        return model
    
    def compile(model):
        return model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 