# -*- coding: utf-8 -*-
"""Approach_2_ps_test_for_sol_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wA7SFJX8HEcTO6oWQD3zMRvdVEfbL2U6

# File used for panoptic segmentation training and evaluation using the converted dataset
# Used for quantitative testing for Approach 2 on solution 2 converted validation set
## Author: Ankur Chrungoo
"""

from google.colab import drive

drive.mount('/content/drive/', force_remount=True)

import os

# Change directory as required
os.chdir('/content/drive/MyDrive/dissertation/dissertation')

# Change directory to panoptic-deeplab repo
os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab')

# Install requirements/dependencies
!pip install -r requirements.txt

# Install scripts used for cityscapes data preparation, evaluation, etc. 
!pip install git+https://github.com/mcordts/cityscapesScripts.git

os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val/images')
!rm *_real.png
!mv *.png /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val/

os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val')
!sudo apt-get install mmv

#Remove '_fake' from the file names.
!mmv '*_fake*' '#1#2'

## Used for the 'validation' images only

# Move the images into corresponding city folder 
!mkdir frankfurt
!mv frankfurt_* frankfurt/

!mkdir lindau
!mv lindau_* lindau/
  
!mkdir munster
!mv munster_* munster/

# Change directory to panoptic-deeplab repo
os.chdir('/content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab')

# use for testing the panoptic-deeplab model (solution 2 testing)

#!python tools/test.py --cfg configs/Base-Panoptic-DeepLab.yaml
!python tools/test.py --cfg configs/Approach_2_solution_2_test_on_approach_1_refined.yaml