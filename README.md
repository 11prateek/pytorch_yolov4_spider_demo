# PyTorch YOLOv4 Object Detection Demo on Spiders

This is a quick, little experiment I did for fun where I trained YOLOv4 on images of spiders from the [Arthropod Taxonomy Orders Object Detection Dataset](https://www.kaggle.com/mistag/arthropod-taxonomy-orders-object-detection-dataset).

I used the [PyTorch implementation of YOLOv4 by TianXiaomo](https://github.com/Tianxiaomo/pytorch-YOLOv4).

The image set was split roughly into 76:12:12 for train:val:test. For simplicity's sake, I removed images which had more than 5 spiders.
Preliminary test results:

```
Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.366
Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.467
Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.442
Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.658
Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.745
Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.776
```

## Fun with GIFs

##### *A scene from Spider-Man (2002 film):*

![](GIFs/1.gif)

##### *A GIF from [GIPHY](https://media.giphy.com/media/rAbKGNGM99DBC/giphy.gif):*

![](GIFs/2.gif)

##### *A spider just outside where I live:*

![](GIFs/3.gif)


## References:
- https://github.com/Tianxiaomo/pytorch-YOLOv4
- https://www.kaggle.com/mistag/arthropod-taxonomy-orders-object-detection-dataset
