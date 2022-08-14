# -*- coding: utf-8 -*-
"""ps_for_converted_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ZwI22egYUQ7fUFbNwkv4w6_fHE0A586

# File used for panoptic segmentation training and evaluation using the converted dataset
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
drive.flush_and_unmount()

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

# Refinement done on approach 1 trained model, using approach 2 solution 2 based data
!python tools/train_net.py --cfg configs/Approach_2_solution_2_refine_on_approach_1.yaml

# Train for approach 2 solution 2 based data from scratch
!python tools/train_net.py --cfg configs/Approach_2_solution_2_train_from_scratch.yaml

# Use only for syncing to google drive
#drive.flush_and_unmount()

# Not needed
#!git config --global user.email ankur.chrungoo@gmail.com

#!git commit -m "updated"

# Install scripts used for cityscapes data preparation, evaluation, etc. 
!pip install git+https://github.com/mcordts/cityscapesScripts.git

# use for testing the panoptic-deeplab model (solution 2a testing)

#!python tools/test.py --cfg configs/Base-Panoptic-DeepLab.yaml
!python tools/test.py --cfg configs/Approach_2_solution_2_refine_on_approach_1.yaml

"""**DEMO - Evaluation**"""

# Use for qualitative evaluation purposes
!python tools/demo.py --cfg configs/Base-Panoptic-DeepLab_converted_dataset.yaml \
    --input-files demo_input_converted \
    --output-dir output/ps_converted_data_R50_bs_1_90K_lr_00005/demo_output_converted \
    --merge-image \
    TEST.MODEL_FILE output/ps_converted_data_R50_bs_1_90K_lr_00005/final_state.pth

# Use for qualitative evaluation purposes (without merge)
!python tools/demo.py --cfg configs/Base-Panoptic-DeepLab_converted_dataset.yaml \
    --input-files demo_input_converted \
    --output-dir output/ps_converted_data_R50_bs_1_90K_lr_00005/demo_output_converted_no_merge \
    TEST.MODEL_FILE output/ps_converted_data_R50_bs_1_90K_lr_00005/final_state.pth