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
4. After the data preprocess and if the `aug` flag is TRUE then data augmentation will start. After the augmentation the data will be divided in traiingn and validation sets. If `aug` flag is FALSE then data will directly be split into the two sets (ratio is training = 80, validation = 20).
5. After the creation of the `validation_set` and `training_set` model the training will start. You can change the parameter in yolo class for training.
6. All paramters (epochs) can be changed in `config.py`.
6. The trained model is saved in the given path, as `best.pt` 
7. In the weights directory `best.pt` is best model. But you can save it on different location.

### Notes 
- `data_augmentation.py` file is required for data augmentation. 
- default `cropping_size = 2500`. This means the image will be croped from main `tif` file with height, width = 2500. set cropping size according to your needs.
- **For a better model accuracy keep `crop_size` same for model training as well as model prediction.**

## Prediction
1. `prediction_with_geojson.ipynb` will accept (`tif` file and  `model_weights`) and save predicted images in given directory. The model `.pt` file is required for the model prediction and the path for model weights needs updating to the location of `best.pt`.
2. The prediction process script will generate crops from the `tif` file and predict and store the output in the destination folder. If the object is detected a bounding box is drawn on the image. 
3. The script will create a `geojson` file with the realworld coordinates of the the detected objects. 

## Visualization
1. `visualization_pipeline.ipynb` will accept `tif` file and `geojson` file as input and visualize bounding box. You can use this script to verify input/predicted data.


## Party !!!





