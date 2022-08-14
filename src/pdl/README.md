# Training and Testing execution source code
All the Training and Testing execution related source code files are present under the folder **"/src_train_test"**
- A description for all the files is provided in **"Files.xlsx"**. Please refer this file to understand which file does what.
- The corresponding jupyter notebooks are added to a sub-folder **"/jupyter"**
        

# IMPORTANT: DATA SETUP for Cityscapes dataset
- Before training of the panoptic-deeplab model, the data preparation scripts need to be run for the Cityscapes dataset, as described in https://github.com/bowenc0221/panoptic-deeplab/blob/master/datasets/README.md

# Panoptic-DeepLab model architecture source code:
- Source code for Panoptic segmentation model is present under the folder: **"/panoptic-deeplab"**
    - Config files: All the config files used during the training and evaluation are included as part of this folder.
    - All the adapted code used in the project is also present under this folder.    
- Note: The source code for Panoptic-DeepLab was **ADAPTED** from the public github repository: https://github.com/bowenc0221/panoptic-deeplab which has a re-implementation from the original paper : "Panoptic-DeepLab: A Simple, Strong,and Fast Baseline for Bottom-Up Panoptic Segmentation" 
    - bibtex entry:
        - @inproceedings{cheng2020panoptic,
          title={Panoptic-DeepLab: A Simple, Strong, and Fast Baseline for Bottom-Up Panoptic Segmentation},
          author={Cheng, Bowen and Collins, Maxwell D and Zhu, Yukun and Liu, Ting and Huang, Thomas S and Adam, Hartwig and Chen, Liang-Chieh},
          booktitle={CVPR},
          year={2020}
        }

# CycleGAN main source code:
- The code was referenced from the public github repository : https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
- The code can be downloaded using the following git command:
    - !git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
