import json
import time
from datetime import datetime
import RPi.GPIO as GPIO
  
class FlowMeter():
    ''' Class representing the flow meter sensor which handles input pulses
        and calculates current flow rate (L/min) measurement
    '''
    
    def __init__(self):
        self.flow_rate = 0.0
        self.last_time = datetime.now()
  
    def pulseCallback(self, p):
        ''' Callback that is executed with each pulse 
            received from the sensor 
        '''
       
        # Calculate the time difference since last pulse recieved
        current_time = datetime.now()
        diff = (current_time - self.last_time).total_seconds()
       
        # Calculate current flow rate
        hertz = 1. / diff
        self.flow_rate = hertz / 7.5
       
        # Reset time of last pulse
        self.last_time = current_time
    
    def getFlowRate(self):
        ''' Return the current flow rate measurement. 
            If a pulse has not been received in more than one second, 
            assume that flow has stopped and set flow rate to 0.0
        '''
       
        if (datetime.now() - self.last_time).total_seconds() > 1:
            self.flow_rate = 0.0
        
        return self.flow_rate
  
def main():
    ''' Main function for repeatedly collecting flow rate measurements
        and sending them to the SORACOM API
    '''
   
    # Configure GPIO pins
    INPUT_PIN = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   
    # Init FlowMeter instance and pulse callback
    flow_meter = FlowMeter()
    GPIO.add_event_detect(INPUT_PIN,
                          GPIO.RISING,
                          callback=flow_meter.pulseCallback,
                          bouncetime=20)
   
    # Begin infinite loop
    while True:
  
        # Get current timestamp and flow meter reading
        timestamp = str(datetime.now())
        flow_rate = flow_meter.getFlowRate()
        print('Timestamp: %s' % timestamp)
        print('Flow rate: %f' % flow_rate)
       
        # Delay
        time.sleep(5)
  
if __name__ == '__main__':
   main()
