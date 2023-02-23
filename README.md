# Yolo Exploration
## Get started
1. Clone `yolov7` repo
`git clone https://github.com/WongKinYiu/yolov7.git`
2. Download `yolov7` trained weights from here and put it in yolov7 directory. 
`wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt`
2. Install all necessary dependency using `pip install requirements.txt`. You need Cuda to install talk to your GPU. 
3. Put `training_pipeline.ipynb, custom_scripts, model_prediction_custom.ipynb, visulization_pipeline.ipynb` in `yolov7` directory

## Train the model
1. `training_pipeline.ipynb` contains `data_preprocess` and model training module.
2. `tif` file and `geojson` file is required to run script.
3. The data will preprocess in first phase and stored images and their label in `txt` format on given path.
4. After data preprocess if the `aug` flag is TRUE then data augmentation will start and after augmentation data will be divided in train and validation set. If `aug` flag is FALSE then data will directly divide into train and validation dataset (ratio is training = 80, validation = 20).
5. After the creation of the `validation_set` and `training_set` model the training will start. You can change the parameter in yolo class for training.
6. The trained model is saved in the given path. The results are acceptable without changing the default anchors because the images are cropped according to the size and area of the object (ratio object to crop). For example, if the detectable object  is too small in geotiff image, then the image crop size was small during preprocessing part, and if the dump is big, then the image crop size is big, So I cropped the image in such a way that the object size was is consisten, without changing the default anchors values of the yolo model.
7. In the weights directory `best.pt` is best model. But you can save it on different location.

### Notes 
- `data_augmentation.py` file is required for data augmentation. 
- default `cropping_size = 2500`. This means the image will be croped from main `tif` file with height, width = 2500. set cropping size according to your needs.
- **For a better model accuracy keep `crop_size` same for model training as well as model prediction.**

## Prediction
1. `model_prediction_custom.ipynb` will accept (`tif` file and  `model_weights`) and save predicted images in given directory. The model `.pt` file is required for model prediction. The standard script was customised to save static path to a dynamic path saving static path. 

## Visualization
1. `visualization_pipeline.ipynb` will accept `tif` file and `geojson` file as input and visualize bounding box. You can use this script to verify input/predicted data.

## Party !
