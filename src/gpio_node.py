#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO

from std_msgs.msg import Bool



class GPIONode(object):
  def __init__(self):
    self.node_name = "GPIO"

    self.pins = [4, 17, 27, 22, 20]    
    self.gpio_no = self.pins #gpio_no

    # Subscribers
    self.sub_red = rospy.Subscriber("~visual_fb_red", Bool, self.cbRed, queue_size=1)
    self.sub_yellow = rospy.Subscriber("~visual_fb_yellow", Bool, self.cbYellow, queue_size=1)
    self.sub_green = rospy.Subscriber("~visual_fb_green", Bool, self.cbGreen, queue_size=1)
    self.sub_bz = rospy.Subscriber("~visual_fb_bz", Bool, self.cbBz, queue_size=1)

    # Initial gpio and attach SIGINT event. 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.gpio_no, GPIO.OUT)
    #signal.signal(signal.SIGINT, self.dtor)

    GPIO.output(20, 0)

  def cbRed(self, msg):
    data = 0 if msg.data==True else 1
    GPIO.output(self.pins[4], data)
    
  def cbYellow(self, msg):
    data = 0 if msg.data==True else 1
    GPIO.output(self.pins[1], data)

  def cbGreen(self, msg):
    data = 0 if msg.data==True else 1
    GPIO.output(self.pins[2], data)

  def cbBz(self, msg):
    data = 0 if msg.data==True else 1
    GPIO.output(self.pins[3], data)

  def onShutdown(self):
    GPIO.cleanup()
    rospy.loginfo("[GPIONode] Shutdown.")


if __name__ == '__main__':
  rospy.init_node('GPIO', anonymous=False)
  gpio_node = GPIONode()
  rospy.on_shutdown(gpio_node.onShutdown)
  rospy.spin()
