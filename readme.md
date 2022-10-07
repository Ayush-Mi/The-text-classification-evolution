# The text classification evolution

## Description

One of the basic problem statement in language models is clasifying text data, this repo analyzes five different deep learning algorithms for their efficiency
on [Twitter Sentiment](https://www.kaggle.com/datasets/kazanova/sentiment140). All the trainings were performed on mac M1 pro with 32gb memory.

## Dependencies

## Methods

## Models

 Simple NN Model | RNN Model | GRU Model | LSTM Model | CNN Model 
 :---: | :---: | :---: | :---: | :---: |
 ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/nn_model.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/rnn_model.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/gru_model.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/lstm_model.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/conv_model.png) |

## Results

| | Model Size | No. of Parameters | No. of Trainable Parameters | Training time per epoch | Train Accuracy | Val Accuarcy |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Simple NN Model | 121.5 MB | 26 M | 2.1 M | 135s | 78.62 | 77.9 |
| RNN Model | 95.9 MB | 23.95 M | 7.4 K | 2287s | 80.66 | 80.77 |
| GRU Model | 96.1 MB | 23.96 M | 20.2 K | 36788s | 82.13 | 82.36 |
| LSTM Model | 96.1 MB | 23.96 M | 26.4 K | 4646s | 82.06 | 82.44 |
| Convolution Model | 100 MB | 24.28 M | 344 K | 282s | 79.84 | 80.31 |

NN Model
Accuracy Plot | Loss Plot
:---: | :---: |
![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/NN_accuracy.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/NN_loss.png) |

RNN Model
Accuracy Plot | Loss Plot
:---: | :---: |
![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/rnn_accuracy.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/rnn_loss.png) |

GRU Model
Accuracy Plot | Loss Plot
:---: | :---: |
![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/GRU_accuracy.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/GRU_loss.png) |

LSTM Model
Accuracy Plot | Loss Plot
:---: | :---: |
![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/LSTM_accuracy.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/LSTM_loss.png) |

CNN Model
Accuracy Plot | Loss Plot
:---: | :---: |
![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/CNN_accuracy.png) | ![](https://github.com/Ayush-Mi/The-text-classification-evolution/blob/main/images/CNN_loss.png) |

## Recommendations

