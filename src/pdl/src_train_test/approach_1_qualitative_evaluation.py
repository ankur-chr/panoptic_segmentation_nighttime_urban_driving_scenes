# -*- coding: utf-8 -*-
"""Approach_1_qualitative_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1897mF46gQFla0jr5L7GHy54WUtL2lhjF

# File used for panoptic segmentation qualitative evaluation using night images from other datasets
# Approach 1 - Qualitative Evaluation on other datasets
## Author: Ankur Chrungoo
"""

from google.colab import drive

drive.mount('/content/drive/', force_remount=True)

import os

#Used the same old datasets folder, because of google drive sync issues in zip extraction with new folders. So commenting out this code!
#os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/converted_datasets')

# To unzip prepared dataset, uncomment this code (and use when appropriate directory is selected as the current directory)
#!unzip datasets.zip

# To check directory content.
#ls -lrt cityscapes/leftImg8bit/

# Use ONLY for syncing to google drive
#drive.flush_and_unmount()

# Change directory as required
os.chdir('/content/drive/MyDrive/dissertation/dissertation')

# Use only for git commands
#!git pull
#!git status

# Change directory to panoptic-deeplab repo
os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab')

# Install requirements/dependencies
!pip install -r requirements.txt

# Use for training the panoptic-deeplab model

#!python tools/train_net.py --cfg configs/Base-Panoptic-DeepLab_converted_dataset.yaml
#!python tools/train_net.py --cfg configs/panoptic_deeplab_R50_os32_cityscapes.yaml

# Use only for syncing to google drive
#drive.flush_and_unmount()

# Install scripts for cityscapes data preparation, evaluation, etc.
!pip install git+https://github.com/mcordts/cityscapesScripts.git

# use for testing the panoptic-deeplab model

#!python tools/test.py --cfg configs/Base-Panoptic-DeepLab.yaml
#!python tools/test.py --cfg configs/Base-Panoptic-DeepLab_converted_dataset.yaml

"""**DEMO - Evaluation** - Without Merge"""

# Use for qualitative evaluation purposes  - With Merge  
#!python tools/demo.py --cfg configs/Base-Panoptic-DeepLab_converted_dataset.yaml \
#    --input-files demo_input_converted \
#    --output-dir output/ps_converted_data_R50_bs_1_90K_lr_00005/demo_output_converted \
#    --merge-image \
#    TEST.MODEL_FILE output/ps_converted_data_R50_bs_1_90K_lr_00005/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# ----- Cityscapes converted validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_cs_val_converted \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_cs_val_conv_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ----- Cityscapes converted validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_cs_val_converted \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_cs_val_conv_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# ----- Cityscapes test set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_cs_test_set \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_cs_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ----- Cityscapes test set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_cs_test_set \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_cs_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# ----- BDD test set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_bdd100k_test \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_bdd_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ----- BDD data set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_bdd100k_test \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_bdd_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# -----UNDD data set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_undd \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_undd_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ----- UNDD data set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_undd \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_undd_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

"""## Other datasets - More difficult as not trained!"""

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# -----Dark Zurich validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_dark_zurich_val \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_dark_zurich_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# ------Night City validation set (some images)------

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_nightcity_val \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_night_city_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# -----Dark Zurich validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_dark_zurich_val \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_dark_zurich_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ------Night City validation set (some images)------

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_nightcity_val \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_night_city_no_merge \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

"""**DEMO - EVALUATION** - With Merge option"""

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# -----Dark Zurich validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_dark_zurich_val \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_dark_zurich_merge \
    --merge-image \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For ORIGINAL MODEL ----------
# ------Night City validation set (some images)------

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_original_model.yaml \
    --input-files demo_input_nightcity_val \
    --output-dir output/approach_1_qual_eval_original_model/demo_output_night_city_merge \
    --merge-image \
    TEST.MODEL_FILE output/approach_1_qual_eval_original_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# -----Dark Zurich validation set (some images)----- 

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_dark_zurich_val \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_dark_zurich_merge \
    --merge-image \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth

# Use for qualitative evaluation purposes (without merge) 
# --------For RETRAINED MODEL ----------
# ------Night City validation set (some images)------

!python tools/demo.py --cfg configs/Approach_1_qual_evaluation_retrained_model.yaml \
    --input-files demo_input_nightcity_val \
    --output-dir output/approach_1_qual_eval_retrained_model/demo_output_night_city_merge \
    --merge-image \
    TEST.MODEL_FILE output/approach_1_qual_eval_retrained_model/final_state.pth