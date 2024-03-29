# **Improving Panoptic Segmentation for Nighttime or Low-Illumination Urban Driving Scenes**
This repository contains the source code and related files for the research project titled above, and linked here (https://arxiv.org/abs/2306.13725 Citation: arXiv:2306.13725 [cs.CV] ). The research is based on existing deep-learning architectures and utilizes the Domain Adaptation technique to improve Panoptic segmentation for nighttime or low-illumination urban driving scenes by making use of various existing nighttime driving datasets.

# Training/Testing - source code 
- Python files & Jupyter notebooks
    - All the source code files for training and evaluation are present under the folder **"/src/pdl/src_train_test"** 
        - NOTE: There is no single executable file, as it is not an application development project. There are several files which are used for training and evaluation of deep-learning models. They have been included in the said folder.
        - A description for all the files is provided in
            - **ReadMe.MD** file under the **"/src/pdl/src_train_test"** directory.
            - One can also check or download the descriptions via **"Files.xlsx"** in the same folder
        - The folder contains training and evaluation files for:
            -  Panoptic Segmentation
            -  Domain Adaptation (CycleGAN)
        - Corresponding Jupyter Notebooks are also available with output logs, etc. These are added under the sub-folder **"/jupyter"**
        - For using the training/testing code, one needs the source code for Panoptic-DeepLab and/or CycleGAN. Any adaptations to that code are listed below.
            
# Panoptic-DeepLab model architecture base source code:
- Source code for Panoptic segmentation model is present under the folder: **"/src/pdl/panoptic-deeplab"**
- The source code for Panoptic-DeepLab was **used and slightly adapted** from a public re-implementation of the paper: "Panoptic-DeepLab: A Simple, Strong,and Fast Baseline for Bottom-Up Panoptic Segmentation", available via https://github.com/bowenc0221/panoptic-deeplab  
    - bibtex entry:
        - @inproceedings{cheng2020panoptic,
          title={Panoptic-DeepLab: A Simple, Strong, and Fast Baseline for Bottom-Up Panoptic Segmentation},
          author={Cheng, Bowen and Collins, Maxwell D and Zhu, Yukun and Liu, Ting and Huang, Thomas S and Adam, Hartwig and Chen, Liang-Chieh},
          booktitle={CVPR},
          year={2020}
        }
- The adapted code that was used is included in this folder. 
- A new parameter TRAIN.REFINE was introduced which allows for model refinement with a fresh learning rate, when training is resumed from a given iteration using the RESUME flag. This can be configured like other settings via the configuration yaml files.
- Config files: All the config files used during the training and evaluation are included as part of the **/configs** folder.
- Important base scripts are present in the **/tools** directory, and are described as follows:
    - train_net.py is the base script for training the model.
    - test.py is the base script for testing the model quantitatively.
    - demo.py can be used to test a trained model qualitatively using some input images.

# CycleGAN base source code:
- The base code for CycleGAN mmodel architecture was sourced from the public github repository : https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
- It is part of the published paper "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks" :
    - @inproceedings{CycleGAN2017,
      title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks},
      author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
      booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
      year={2017}
    }
    - @inproceedings{isola2017image,
      title={Image-to-Image Translation with Conditional Adversarial Networks},
      author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
      booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
      year={2017}
    }
- The code can be downloaded using the following git command:
    - !git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
 
- The primary scripts that are important are:
    - train.py : used for training a CycleGAN model
    - test.py : testing a trained CycleGAN model 
- Usage instructions are present in the link: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

# Datasets used:
The following publicly available datasets have been used in this project:
- Cityscapes: https://www.cityscapes-dataset.com/
- Dark Zurich: https://www.trace.ethz.ch/publications/2019/GCMA_UIoU/
- NightCity: https://dmcv.sjtu.edu.cn/people/phd/tanxin/NightCity/index.html
- BDD100K: https://www.bdd100k.com/
- Urban Night Driving Dataset (UNDD): 
    -  https://github.com/sauradip/night_image_semantic_segmentation
    -  https://drive.google.com/drive/folders/1KBn3LIoD5rvNFDe2aZCH-4mNo6iXSuGX
- Nighttime driving dataset: http://people.ee.ethz.ch/~daid/NightDriving/#

# IMPORTANT: DATA SETUP for Cityscapes dataset
- Before training of the panoptic-deeplab model, the data preparation scripts need to be run for the Cityscapes dataset, as described in https://github.com/bowenc0221/panoptic-deeplab/blob/master/datasets/README.md
- This should be done after downloading the required Cityscapes dataset from the dataset link provided below.

# Running the training / evaluation code
- NOTE that the executable code works on the "Google Drive" environment (has been implemented and tested via Google Colaboratory).
- **Panoptic Segmentation**
    - Please download and setup the Cityscapes panoptic segmentation training dataset and prepare it using the instructions and the dataset link(s) provided above.
    - After setting up the data for the Cityscapes dataset, the python file for baseline panoptic segmentation model can be run. Or the other python files can be run as per need.
    - In some files, demo code is also available as described in the readme file in the **"/src_train_test"** directory. The demo related commands in the python files take a trained model, and some input images and use the model to make the panoptic predictions.
        - You will need to setup the data in the required input directory, and have the trained model path ready before using this.
    - The python files also contain commands to execute 'test.py' which evaluate a trained panoptic segmentation model on the configured validation set.
    - The panoptic-deeplab folder contains configuration yaml files under the "configs" directory which can be configured to use different datasets, model settings, trained model path, number of iterations, resume/refine model, number of GPUs, batch size, crop size, loss parameters, and various other settings.
- **CycleGAN**:
    - One can download the required repository from the link provided above.
    - The python files provided under the **"/src_train_test"** directory can be used as per need to train or refine a CycleGAN model.
    - For detailed instructions, please refer: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix and related documentation.
    - The Pytorch-based implementation has been used in the respective code files that are provided.
    - In order to train CycleGAN, source and target datasets need to be set up as per the instructions provided in the repository linked above.
    - If the training gets stuck mid-way, it can be resumed using the --continue_train --epoch_count <epoch number> arguments to the training command. Such examples can be found in the training execution python files in the **"/src_train_test"** directory.

# Trained Models
- The 3 main trained models for panoptic segmentation, and 1 main CycleGAN model can be found here: https://drive.google.com/drive/folders/1--u0QI1YJQsbKRJTA55MDEga7X6OzS3c?usp=sharing
- Many other models were trained and tested for Panoptic Segmentation and CycleGAN under various settings and with different datasets. Those can be shared on request as the list is big!

# Additional data/logs
- Some additional training and evaluation logs are added in the folder **/src/pdl/additional_output** as artifacts for trainings (and evaluation) conducted under various settings, such as:
    - different ResNet backbone variants i.e., ResNet-34 or ResNet-50
    - different learning rates, crop sizes, batch sizes, dilation enabled/disabled, etc.
    - refining or training from scratch
      
# References
- CycleGAN and pix2pix in PyTorch
  https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
  - @inproceedings{CycleGAN2017,
      title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks},
      author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
      booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
      year={2017}
    }
  - @inproceedings{isola2017image,
      title={Image-to-Image Translation with Conditional Adversarial Networks},
      author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
      booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
      year={2017}
    }    
- Panoptic-DeepLab: A Simple, Strong,and Fast Baseline for Bottom-Up Panoptic Segmentation
  https://github.com/bowenc0221/panoptic-deeplab  
    - bibtex entry:
        - @inproceedings{cheng2020panoptic,
          title={Panoptic-DeepLab: A Simple, Strong, and Fast Baseline for Bottom-Up Panoptic Segmentation},
          author={Cheng, Bowen and Collins, Maxwell D and Zhu, Yukun and Liu, Ting and Huang, Thomas S and Adam, Hartwig and Chen, Liang-Chieh},
          booktitle={CVPR},
          year={2020}
        }
