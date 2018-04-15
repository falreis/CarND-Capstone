from styx_msgs.msg import TrafficLight
import random
import rospy
import time

class TLClassifier(object):
    def __init__(self):
        self.current_light = TrafficLight.UNKNOWN
        self.last_time = rospy.get_time()
        rospy.logerr('Traffic Light UNKNOWN')
        #TODO load classifier

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        '''
        Traffic light simulator just to test the behavior of the vehicle
        '''
        if self.current_light == TrafficLight.RED:
            if (rospy.get_time() - self.last_time) > 10:
                self.current_light = TrafficLight.GREEN
                rospy.logerr('Traffic Light GREEN')
        else:
            self.last_time = rospy.get_time()
            randvalue = random.randint(0,10000)
            
            if randvalue < 2:
                self.current_light = TrafficLight.RED
                rospy.logerr('Traffic Light RED')
            elif randvalue > 999:
                self.current_light = TrafficLight.UNKNOWN
            else:
                self.current_light = TrafficLight.GREEN

        return self.current_light
