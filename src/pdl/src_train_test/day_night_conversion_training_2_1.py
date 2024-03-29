# -*- coding: utf-8 -*-
"""day_night_conversion_training_2_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15kCKY2ta3Y_h8gIitUlsmD8Xdppq58-0

# File used for fresh training of day-to-night conversion model using CycleGAN and test it to generate translated images from the domain of converted cityscapes images to the domain of Nighttime Driving dataset images. Also, test it to generate translated images from normal domain to Nighttime driving dataset domain.
# Approach 2 - Solution 1
## Author: Ankur Chrungoo
"""

# Mount google drive
from google.colab import drive
drive.mount('/content/drive/', force_remount=True)
import os

# Switch directory
os.chdir('/content/drive/MyDrive/day_night_conversion')

"""# Install"""

!git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

os.chdir('pytorch-CycleGAN-and-pix2pix/')

# Install dependencies
!pip install -r requirements.txt

# Helper command to setup the converted cityscapes training data
#!cp -r /content/drive/MyDrive/day_night_conversion/train /content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/datasets/cityscapes_to_nighttime_driving/trainA

# Train the CycleGAN network for day-night translation. Keeping the dataset path same, but using a different name for the model being trained.
# Here, CycleGAN is being trained on converted Cityscapes nighttime images (taken from Approach 1), and Nighttime Driving Dataset images (publicly available night images)
!python train.py --dataroot ./datasets/cityscapes_to_nighttime_driving/ --name converted_cityscapes_to_nighttime_driving --model cycle_gan --preprocess crop --crop_size 256

# Used to convert day images to poor light/ night images [From converted cityscapes nighttime images (from approach 1) to Nighttime driving dataset domain]
!python test.py --dataroot ./datasets/cityscapes_to_nighttime_driving/ --name converted_cityscapes_to_nighttime_driving --model test --no_dropout --preprocess none --num_test=900 #--use_wandb

# Used to convert day images to poor light/ night images (from cityscapes normal 840 images to Nighttime driving dataset domain)
!python test.py --dataroot ./datasets/cityscapes_to_nighttime_driving/testA --name converted_cityscapes_to_nighttime_driving --model test --no_dropout --preprocess none --num_test=900 #--use_wandb 

# STOPPED this particular test in the middle of it, as the results were not promising!

# For syncing to google drive
#drive.flush_and_unmount()

"""# Used for processing the generated images, and putting them into the correct folders for further steps. 
######(This code is modified as per latest processing steps executed, so it may not have the full list of steps or folders used for train, val sets' post conversion steps)
"""

os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/daynight_cyclegan_pretrained/test_latest/images')

# remove the real images (only keep the converted ones)
!rm *_real.png

# copy the fake (night/poor light) images to the 'val' folder
!cp *_fake.png /content/drive/MyDrive/day_night_conversion/val

# copying the results of the conversion to the images folder as a backup
os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/daynight_cyclegan_pretrained/test_latest/')
!cp -r images/ /content/drive/MyDrive/day_night_conversion/images/val

#os.chdir('/content/drive/MyDrive/day_night_conversion/train')
os.chdir('/content/drive/MyDrive/day_night_conversion/val')

!sudo apt-get install mmv

#Remove '_fake' from the file names.
!mmv '*_fake*' '#1#2'

## Used for the 'training' images only

# Move the images into corresponding city folder 
!mkdir aachen
!mv aachen_* aachen/

!mkdir bochum
!mv bochum_* bochum/

!mkdir bremen
!mv bremen_* bremen/

!mkdir cologne
!mv cologne_* cologne/

!mkdir darmstadt
!mv darmstadt_* darmstadt/

!mkdir dusseldorf
!mv dusseldorf_* dusseldorf/

!mkdir erfurt
!mv erfurt_* erfurt/

!mkdir hamburg
!mv hamburg_* hamburg/

!mkdir hanover
!mv hanover_* hanover/

!mkdir jena
!mv jena_* jena/

!mkdir krefeld
!mv krefeld_* krefeld/

!mkdir monchengladbach
!mv monchengladbach_* monchengladbach/

!mkdir strasbourg
!mv strasbourg_* strasbourg/

!mkdir stuttgart
!mv stuttgart_* stuttgart/

!mkdir tubingen
!mv tubingen_* tubingen/

!mkdir ulm
!mv ulm_* ulm/

!mkdir weimar
!mv weimar_* weimar/

!mkdir zurich
!mv zurich_* zurich/

## Used for the 'training' images only

#Copy files into the actual dataset
os.chdir('/content/drive/MyDrive/day_night_conversion/train')

!cp aachen/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/aachen/
!cp bochum/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/bochum/
!cp bremen/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/bremen/
!cp cologne/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/cologne/
!cp darmstadt/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/darmstadt/
!cp dusseldorf/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/dusseldorf/
!cp erfurt/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/erfurt/
!cp hamburg/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/hamburg/
!cp hanover/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/hanover/
!cp jena/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/jena/
!cp krefeld/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/krefeld/
!cp monchengladbach/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/monchengladbach/
!cp strasbourg/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/strasbourg/
!cp stuttgart/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/stuttgart/
!cp tubingen/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/tubingen/
!cp ulm/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/ulm/
!cp weimar/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/weimar/
!cp zurich/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/train/zurich/

## Used for the 'validation' images only

# Move the images into corresponding city folder 
!mkdir frankfurt
!mv frankfurt_* frankfurt/

!mkdir lindau
!mv lindau_* lindau/
  
!mkdir munster
!mv munster_* munster/

## Used for the 'validation' images only

#Copy files into the actual dataset
os.chdir('/content/drive/MyDrive/day_night_conversion/val')

!cp frankfurt/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val/frankfurt/
!cp lindau/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val/lindau/
!cp munster/* /content/drive/MyDrive/dissertation/dissertation/src/pdl/panoptic-deeplab/datasets/cityscapes/leftImg8bit/val/munster/