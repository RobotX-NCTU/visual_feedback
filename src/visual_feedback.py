#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO

from std_msgs.msg import Bool,Int32

class VisualFeedback(object):
    def __init__(self):
        self.node_name = "visual_feedback"

        self.output_pins = [4, 17, 27, 22] # red, yellow, green, nothing

        # Initial gpio and attach SIGINT event. 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_no, GPIO.OUT)
        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        rospy.sleep(1)
        self.turnOnAll()
        self.clearAll()
        rospy.sleep(1)

        rospy.Timer(rospy.Duration(0.5), self.detectEmergency)

        # Subscribers
        self.sub_red = rospy.Subscriber("~visual_fb_red", Bool, self.cbRed, queue_size=1)
        self.sub_yellow = rospy.Subscriber("~visual_fb_yellow", Bool, self.cbYellow, queue_size=1)
        self.sub_green = rospy.Subscriber("~visual_fb_green", Bool, self.cbGreen, queue_size=1)
        self.sub_mode = rospy.Subscriber("~mode", Int32, self.cbMode, queue_size=1)

    def detectEmergency(self, event):
        if (GPIO.input(21) == 1):
            self.setLed(self.output_pins[0], True)
        else:
            self.setLed(self.output_pins[0], False)

    def cbMode(self, msg):
        if (msg.mode == 0): # Joystick => Yellow
            self.setLed(self.output_pins[2], False)
            self.setLed(self.output_pins[1], True)
        elif (msg.mode == 1): # Autonomous => Green
            self.setLed(self.output_pins[1], False)
            self.setLed(self.output_pins[2], True)

    def turnOnAll(self):
        for pin in self.output_pins:
            GPIO.output(pin, 1)

    def clearAll(self):
        for pin in self.output_pins:
            GPIO.output(pin, 0)

    def setLed(self, pin, on): 
        data = 0 if on==True else 1
        GPIO.output(pin, data)

    def cbRed(self, msg):
        self.setLed(self.output_pins[0], msg.data)
    
    def cbYellow(self, msg):
        self.setLed(self.output_pins[1], msg.data)

    def cbGreen(self, msg):
        self.setLed(self.output_pins[2], msg.data)

    def onShutdown(self):
        self.clearAll()
        GPIO.cleanup()
        rospy.loginfo("[Visual Feedback] Shutdown.")


if __name__ == '__main__':
    rospy.init_node('visual_feedback', anonymous=False)
    visual_feedback_node = VisualFeedback()
    rospy.on_shutdown(visual_feedback_node.onShutdown)
    rospy.spin()
