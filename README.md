# Project: Emotion Recognize
This project has 4 part
### Part 1: steps to create data
- Data will be taken from my feelings, using computer webcam to collect.
- Data includes 5 types of emotions: happy, sad, suprise, angry, normal. Each emotion has 3000 pictures

### Part 2 data processing steps on jupyter notebook
- Read images, resize to 128, 128
- Normalization and one-hot encoding
- Split train - valid data
- Save to .npy file to upload to Google Collab for training

### Part 3: Train Model
- The model I created is based on the idea of VGG16, which is to use nested convolution layers, then use maxpooling to pool images, and again use nested convolution layers, finally a fully connected network.
- The network includes 4 convolution layers, 2 maxpooling layers, FC includes 2 dense layers and 1 output layer.
- After the network is done training, the checkpoint will be saved and modeled again
- Predictable network Final Loss: 0.5006, Final Accuracy: 0.2077
- The reason is because the resource is in stock, so only train epochs = 10

### Part 4: Test on real data taken from webcam
- Like part 1, instead of the image being saved to a folder, it will be projected straight and predicted based on the model.
- Because the accuracy is still poor, it still needs a lot of improvement.
  
***This project is for reference only***
