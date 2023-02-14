step 1 => remove all other previous data and environment 

step 2 => create new environment and install required dependency. 


Step 3 => after unzip you will get 3 directory
		  1. data
		  2. geojson
		  3. yolov7

step 4 => put your .tif file and their corresponding .tfw file in data folder.
		  so data folder will be look like:
		  	-> NamarDaharat2_Orthomosaic_export_TueAug23092831065915.tif
		  	-> NamarDaharat2_Orthomosaic_export_TueAug23092831065915.tfw


step 5 => put your .geojson file in geojson folder.
		  geojson folder will be look like:
		  	-> Bounding-boxed-samples-fixed-geom-v3.geojson


step 6 => go to yolov7 directory and run 'training_pipeline.ipynb'.


NOTE: if you get any error during training data then remove all previous directory, delete all generated data and then go to yolov7 directory and install other pip dependecy using:
	pip install -r requirements.txt.
then try again and repeat all steps.
