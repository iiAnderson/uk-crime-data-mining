
Data Mining UK Crime Data - Part of University Course into Data Mining

As the dataset was often missing records, there was multiple cleaning steps. Furthermore, to ensure we tested all dimensions of the data, many of the scripts in the `processing` directory are to remove and add certain aspects to the dataset. These allowed us to run the models efficiently on limited compute power.

The models directory contains the models we ran, utlising jupyter notebooks to easily iterate on solutions. The main comparison we used was the AlwayASBOClassifier,which predicted each crime was of type ASBO - which was the most common type of crime. We then tested different models against this classifier to attempt to find a better method of predicting crime type.

More information can be found in the Data_Mining_Report.pdf