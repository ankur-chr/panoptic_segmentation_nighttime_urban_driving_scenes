# ------------------------------------------------------------------------------
# Builds model.
# Updated by Ankur Chrungoo
# ------------------------------------------------------------------------------

import torch

from .backbone import resnet
from .meta_arch import PanopticDeepLab
from .loss import RegularCE, OhemCE, DeepLabCE, L1Loss, MSELoss, CrossEntropyLoss


def build_segmentation_model_from_cfg(config):
    """Builds segmentation model with specific configuration.
    Args:
        config: the configuration.

    Returns:
        A nn.Module segmentation model.
    """
    model_map = {
        'panoptic_deeplab': PanopticDeepLab,
    }

    model_cfg = {
        'panoptic_deeplab': dict(
            replace_stride_with_dilation=config.MODEL.BACKBONE.DILATION,
            in_channels=config.MODEL.DECODER.IN_CHANNELS,
            feature_key=config.MODEL.DECODER.FEATURE_KEY,
            low_level_channels=config.MODEL.PANOPTIC_DEEPLAB.LOW_LEVEL_CHANNELS,
            low_level_key=config.MODEL.PANOPTIC_DEEPLAB.LOW_LEVEL_KEY,
            low_level_channels_project=config.MODEL.PANOPTIC_DEEPLAB.LOW_LEVEL_CHANNELS_PROJECT,
            decoder_channels=config.MODEL.DECODER.DECODER_CHANNELS,
            atrous_rates=config.MODEL.DECODER.ATROUS_RATES,
            num_classes=config.DATASET.NUM_CLASSES,
            has_instance=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.ENABLE,
            instance_low_level_channels_project=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.LOW_LEVEL_CHANNELS_PROJECT,
            instance_decoder_channels=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.DECODER_CHANNELS,
            instance_head_channels=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.HEAD_CHANNELS,
            instance_aspp_channels=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.ASPP_CHANNELS,
            instance_num_classes=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.NUM_CLASSES,
            instance_class_key=config.MODEL.PANOPTIC_DEEPLAB.INSTANCE.CLASS_KEY,
            semantic_loss=build_loss_from_cfg(config.LOSS.SEMANTIC),
            semantic_loss_weight=config.LOSS.SEMANTIC.WEIGHT,
            center_loss=build_loss_from_cfg(config.LOSS.CENTER),
            center_loss_weight=config.LOSS.CENTER.WEIGHT,
            offset_loss=build_loss_from_cfg(config.LOSS.OFFSET),
            offset_loss_weight=config.LOSS.OFFSET.WEIGHT,
        )
    }

    if config.MODEL.BACKBONE.META == 'resnet':
        backbone = resnet.__dict__[config.MODEL.BACKBONE.NAME](
            pretrained=config.MODEL.BACKBONE.PRETRAINED,
            replace_stride_with_dilation=model_cfg[config.MODEL.META_ARCHITECTURE]['replace_stride_with_dilation']
        )
    else:
        raise ValueError('Unknown meta backbone {}, please first implement it.'.format(config.MODEL.BACKBONE.META))

    model = model_map[config.MODEL.META_ARCHITECTURE](
        backbone,
        **model_cfg[config.MODEL.META_ARCHITECTURE]
    )
    # set batchnorm momentum
    for module in model.modules():
        if isinstance(module, torch.nn.BatchNorm2d):
            module.momentum = config.MODEL.BN_MOMENTUM
    return model


def build_loss_from_cfg(config):
    """Builds loss function with specific configuration.
    Args:
        config: the configuration.

    Returns:
        A nn.Module loss.
    """
    if config.NAME == 'cross_entropy':
        # return CrossEntropyLoss(ignore_index=config.IGNORE, reduction='mean')
        return RegularCE(ignore_label=config.IGNORE)
    elif config.NAME == 'ohem':
        return OhemCE(ignore_label=config.IGNORE, threshold=config.THRESHOLD, min_kept=config.MIN_KEPT)
    elif config.NAME == 'hard_pixel_mining':
        return DeepLabCE(ignore_label=config.IGNORE, top_k_percent_pixels=config.TOP_K_PERCENT)
    elif config.NAME == 'mse':
        return MSELoss(reduction=config.REDUCTION)
    elif config.NAME == 'l1':
        return L1Loss(reduction=config.REDUCTION)
    else:
        raise ValueError('Unknown loss type: {}'.format(config.NAME))
