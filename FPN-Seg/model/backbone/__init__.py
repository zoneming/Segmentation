from model.backbone import resnet

def build_backbone(back_bone):
    if back_bone == "resnet101":
        return resnet.ResNet101(pretrained=True)
    elif back_bone == "resnet50":
        return resent.ResNet50(pretrained=True)
    elif back_bone == "resnet34":
        return resent.ResNet34(pretrained=True)
