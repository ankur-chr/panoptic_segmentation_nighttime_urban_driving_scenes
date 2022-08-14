# -*- coding: utf-8 -*-
"""day_night_conversion_training_2_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NpO0hNHYHkrT-Ad7oCHbnxedjrz4uYZ

# File used for re-training of day-to-night downloaded pre-trained model and test it to generate translated images from the domain of converted cityscapes images to the domain of mixed images of night time datasets (further filtered). 
# Approach 2 - Solution 3
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

# Helper commands for data setup (not always needed)
os.chdir('datasets/cityscapes_pretrained_to_mix2/trainB')

# Helper commands for data setup (not always needed)
#!unzip dz_night_filtered_2.zip

# Helper commands for datasetup (not always needed)
#!unzip train_filtered_2.zip

# helper commands for data setup (not always needed)
#!mv night_filtered_2/* .

# helper commands for data setup (not always needed)
#!mv train_filtered_2/* .

# helper commands for data setup (not always needed)
#!ls -dq *frame* | wc -l

# Train the CycleGAN network for day-night translation. 
# Here, CycleGAN is being trained on Cityscapes training images and a mix of night time images from different datasets (NightCity dataset, Dark Zurich dataset, Nighttime driving dataset, and Urban Night Driving dataset)
!python train.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/ --name cityscapes_pretrained_to_mix2 --model cycle_gan --preprocess crop --crop_size 256 --continue_train --epoch_count 154

# Used to convert day images to poor light/ night images
!python test.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/testA --name cityscapes_pretrained_to_mix2 --model test --no_dropout --num_test=900 --preprocess none #--use_wandb

# Used to convert day images to poor light/ night images [------ used with different pre-processing modes -----]
!python test.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/testA --name cityscapes_pretrained_to_mix2 --model test --no_dropout --num_test=20 --preprocess crop --crop_size 512 #--preprocess none #--use_wandb

# (Not to be used always)
# Used to convert day images to poor light/ night images [------for 840 train set data -------using the trained model from the 100th epoch (from the checkpoints directory)-------]
# Before running this, I set the 100th epoch trained model as the latest one to be used for conversion.
!python test.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/testA --name cityscapes_pretrained_to_mix2 --model test --no_dropout --num_test=900 --preprocess none #--use_wandb

# Not to be used always - FOR VARIOUS EPOCHS' TRAINED models (50, 60, 70, 80, 90th, 150th, etc)
# Used to convert day images to poor light/ night images [------for training set data ----- ]
!python test.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/testA --name cityscapes_pretrained_to_mix2 --model test --no_dropout --num_test=900 --preprocess none #--use_wandb

# Not to be used always - FOR VARIOUS EPOCHS' TRAINED models (using 60th epoch trained model only)
# Used to convert day images to poor light/ night images [------for Validation set data ----- ]
!python test.py --dataroot ./datasets/cityscapes_pretrained_to_mix2/testA --name cityscapes_pretrained_to_mix2 --model test --no_dropout --num_test=900 --preprocess none #--use_wandb

# For syncing to google drive
drive.flush_and_unmount()

"""# Used for processing the generated images, and putting them into the correct folders for further steps. 
######(This code is modified as per latest processing steps executed, so it may not have the full list of steps or folders used for train, val sets' post conversion steps)
"""

os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/cityscapes_pretrained_to_mix2/train_converted_100th_epoch/images/')

# remove the real images (only keep the converted ones)
#!rm *_real.png

# copy the fake (night/poor light) images to a folder
!cp *_fake.png /content/drive/MyDrive/day_night_conversion/images/train_sol_3

# copying the results of the conversion to the images folder as a backup
os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/cityscapes_pretrained_to_mix2/train_converted_100th_epoch/images/')
!cp -r images/ /content/drive/MyDrive/day_night_conversion/images/train_sol_3

os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/cityscapes_pretrained_to_mix2/train_converted_60th_epoch/images/')

# remove the real images (only keep the converted ones)
#!rm *_real.png

# copy the fake (night/poor light) images to a folder
!cp *_fake.png /content/drive/MyDrive/day_night_conversion/images/train_sol_3_60th

# copying the results of the conversion to the images folder as a backup
os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/cityscapes_pretrained_to_mix2/train_converted_60th_epoch/images/')
!cp -r images/ /content/drive/MyDrive/day_night_conversion/images/train_sol_3_60th

os.chdir('/content/drive/MyDrive/day_night_conversion/pytorch-CycleGAN-and-pix2pix/results/converted_cityscapes_to_nighttime_driving/images/')

# remove the real images (only keep the converted ones)
#!rm *_real.png

# copy the fake (night/poor light) images to a folder
!cp *_fake.png /content/drive/MyDrive/day_night_conversion/images/train_sol_1

os.chdir('/content/drive/MyDrive/day_night_conversion/images/')
!mv *_fake.png /content/drive/MyDrive/day_night_conversion/images/train_converted_app_1

os.chdir('/content/drive/MyDrive/day_night_conversion/train_sol_3')
#os.chdir('/content/drive/MyDrive/day_night_conversion/val')

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