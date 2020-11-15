# Robust Neural Network Output Enhancement for Active Lane Detection (RONELD)

Python implementation for "RONELD: Robust Neural Network Output Enhancement for Active Lane Detection"

<br>

## Paper
Zhe Ming Chng, Joseph Mun Hung Lew, Jimmy Addison Lee, "RONELD: Robust Neural Network Output Enhancement for Active Lane Detection", to be presented at International Conference on Pattern Recognition (ICPR) 2020. 

Link on arXiv: https://arxiv.org/abs/2010.09548

<br>

## Introduction

<img src="process_workflow.jpg" />

RONELD is intended as a turnkey solution for use on probability map outputs from deep learning lane detection models such as SCNN and ENet-SAD to detect and optimize active lane detection. RONELD searches for the two lane markings that demarcate the active lane which is the single road space that the vehicle is currently travelling on.

<br>

## Using RONELD

This code has been tested on Python 3.6 and should work on later versions as well.

 - lane_detection_functions.py
 - evaluate.py

Code for the module is stored in the lane_detection_functions module, with roneld_lane_detection being the main method to run

roneld_lane_detection takes in the probability maps from the deep learning models as numpy arrays, along with other information that keeps track of preceding frame data. The camera's extrinsic parameters are also required to determine where the center of the lane is, as well as the height of the horizon, which are center_ratio and lane_ratio respectively. (For experiments, center_ratio was set at 0.5 to reflect the horizontal center of the image, while the lane_ratio was set at 0.6 for TuSimple and 0 for CULane, as CULane did not extend the lane to the horizon)

### Setup

Clone this repo and run setup.py to install the required packages:

```
  python setup.py install
```

### Before starting

Run the images on the SCNN or ENet-SAD model (https://github.com/cardwing/Codes-for-Lane-Detection) first to obtain the probability map outputs before using the RONELD method.

### Testing the method

In test.py, change dataset_file_path to the file path of the directory containing the images and probability map outputs. The naming of the probability map outputs should follow that of the above SCNN and ENet-SAD implementation (4 lanes each labelled {original image name}\_{0-3}\_avg.png)

Then, run test.py:
```
  python test.py
```

Some sample images from the CULane dataset (https://xingangpan.github.io/projects/CULane.html) with lane outputs from the SCNN model have been included included to showcase the method.

<br>

## Citing RONELD
If you find RONELD helpful to your research, please cite it:
```
@misc{chng2020roneld,
      title={RONELD: Robust Neural Network Output Enhancement for Active Lane Detection}, 
      author={Zhe Ming Chng and Joseph Mun Hung Lew and Jimmy Addison Lee},
      year={2020},
      eprint={2010.09548},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

<br>

## To-do list

- [x] Add lane_detection_functions
- [ ] Add test code that can be run from the command line
- [ ] Add evaluation code

<br>

## Contact

Facing any errors or difficulties? Any comments, feedback, or suggestions? Just want to get in touch? Raise an issue or email me at zchng3@gatech.edu or chngzm@gmail.com
