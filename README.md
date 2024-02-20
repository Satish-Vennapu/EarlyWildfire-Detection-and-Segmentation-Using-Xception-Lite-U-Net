# Early  Wildfire Detection and Segmentation Using Xception Lite and U-Net





### Dataset
* The FLAME dataset is uploaded on Google Drive You can find the dataset [here] (https://drive.google.com/drive/folders/1es3KGvb8fAa5P2GJ-zyt-BDJ2RkuehvM?usp=drive_link) 

* This table below shows all available data for the dataset.
* This project uses items 7, 8, 9, and 10 from the dataset. Items 7 and 8 are being used for the "Fire_vs_NoFire" image classification. Items 9 and 10 are for the fire segmentation. 
* If you clone this repository on your local drive, please download item [7](https://drive.google.com/drive/folders/1es3KGvb8fAa5P2GJ-zyt-BDJ2RkuehvM?usp=drive_link) 
 from the dataset and unzip in the directory /frames/Training/... for the Training phase of the "Fire_vs_NoFire" image classification. The directory looks like this:
```bash
Repository/frames/Training
                    ├── Fire/*.jpg
                    ├── No_Fire/*.jpg
```
* For testing your trained model, please use item [8](https://drive.google.com/drive/folders/1b9RLhxoLlFeKWFXumwEsSWGw1ySRoodC?usp=sharing) and unzip it in directory/frame/Test/... . The directory looks like this:
```bash
Repository/frames/Test
                    ├── Fire/*.jpg
                    ├── No_Fire/*.jpg
```
* Items [9](https://drive.google.com/drive/folders/1TjiHFUqimGuerpznDXmXUlKrVwplWY0G?usp=drive_link) and [10](https://drive.google.com/drive/folders/1TjiHFUqimGuerpznDXmXUlKrVwplWY0G?usp=drive_link) should be unzipped in these directories frames/Segmentation/Data/Image/... and frames/Segmentation/Data/Masks/... accordingly. The directory looks like this:
```bash
Repository/frames/Segmentation/Data
                                ├── Images/*.jpg
                                ├── Masks/*.png
```



### Model
* The binary fire classification model of this project is based on the Xception Network:

![Alt text](/frames/xception-lite.jpeg)
<br/>
<br/>

* The fire segmentation model of this project is based on the U-NET:

![Alt text](/frames/segmentation_architecture.jpeg)


## Requirements
* os
* re
* cv2
* copy
* tqdm
* scipy
* pickle
* NumPy
* random
* itertools
* Keras 2.4.0
* scikit-image
* Tensorflow 2.3.0
* matplotlib.pyplot

## Code
This code is run and tested on Python 3.9.7 on Linux (Ubuntu 18.04) machine with no issues. There is a config.py file in this directory that shows all the configuration parameters such as **Mode**, **image target size**, **Epochs**, **batch size**, **train_validation ratio**, etc. All dependency files are available in the root directory of this repository.
* To run the training phase for the "Fire_vs_NoFire" image classification, change the **mode** value to 'Training' in the config.py file. 
```
Mode = 'Training'
```
Make sure that you have copied and unzipped the data in the correct directory.

* To run the test phase for the "Fire_vs_NoFire" image classification, change the **mode** value to 'Classification' in the config.py file. 
```
Mode = 'Classification'
```
Make sure that you have copied and unzipped the data in the correct directory.

* To run the test phase for the Fire segmentation, change the **mode** value to 'Classification' in the config.py file. 
```
Mode = 'Segmentation'
```

* To train with  Xception-lite, change the **mode** value to 'Classification' in the config.py file. 
```
Mode = 'Myxception'
```
* To train with  Xception, change the **mode** value to 'Classification' in the config.py file. 
```
Mode = 'xception'
```

Make sure that you have copied and unzipped the data in the correct directory.

Then after setting your parameters, just run the main.py file.
```
python main.py
```

## Results

![Alt text](/frames/segmentation_results.png)

* Comparison between generated masks and ground truth masks:

![Alt text](/frames/segmentation_img.png)




