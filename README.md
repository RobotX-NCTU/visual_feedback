# visual_feedback
Led Array for robotx competition. There are red, yellow, green, and buzzer on the visual feedback.

## How to setup
``` 
cd ~/robotx/catkin_ws/src
git clone https://github.com/RobotX-NCTU/visual_feedback.git
```

## catkin_make

```
source /opt/ros/kinetic/setup.bash
cd ~/robotx/catkin_ws
catkin_make
```

## How to run

```
cd ~/robotx
source /opt/ros/kinetic/setup.bash
source ~/robotx/catkin_ws/devel/setup.bash
roslaunch visual_feedback visual_feedback_node.launch

rostopic pub /visual_feedback_node/visual_fb_[red] std_msgs/Bool "data: true"
[] could be "red", "green", "yellow", "bz"
```

## Error List


 
