#!/usr/bin/env python
import rospy
import wiringpi

from std_msgs.msg import Bool

class VisualFeedbackNode(object):
  def __init__(self):
    self.node_name = "Visual_Feedback"
    wiringpi.wiringPiSetupSys()

    self.pins = [4, 17, 27, 22]
    for pin in self.pins:
      wiringpi.pinMode(pin,1)
      wiringpi.digitalWrite(pin,1)

    # Subscribers
    self.sub_red = rospy.Subscriber("visual_feedback_red", Bool, self.cbRed, queue_size=1)
    self.sub_yellow = rospy.Subscriber("visual_feedback_yellow", Bool, self.cbYellow, queue_size=1)
    self.sub_green = rospy.Subscriber("visual_feedback_green", Bool, self.cbGreen, queue_size=1)
    self.sub_bz = rospy.Subscriber("visual_feedback_bz", Bool, self.cbBz, queue_size=1)

  def cbRed(self, msg):
    #data = msg.data==True ? 0 : 1
    data = 0 if msg.data==True else 1
    wiringpi.digitalWrite(self.pins[0],data)
  def cbYellow(self, msg):
    data = 0 if msg.data==True else 1
    wiringpi.digitalWrite(self.pins[1],data)

  def cbGreen(self, msg):
    data = 0 if msg.data==True else 1
    wiringpi.digitalWrite(self.pins[2],data)

  def cbBz(self, msg):
    data = 0 if msg.data==True else 1
    wiringpi.digitalWrite(self.pins[3],data)

  def onShutdown(self):
    rospy.loginfo('[VisualFeedbackNode Shutdown.')

if __name__ == '__main__':
  rospy.init_node('visual_feedback', anonymous=False)
  visual_feedback_node = VisualFeedbackNode()
  rospy.on_shutdown(visual_feedback_node.onShutdown)
  rospy.spin()
