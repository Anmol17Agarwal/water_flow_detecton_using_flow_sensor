# water_flow_detecton_using_flow_sensor

In industries there will be many big pipelines carrying various types of liquids, including the flammable liquids and corrosive
liquids. It is necessary to control the flow rate of the liquid for enhancing the processes and to prevent the accidents. The paper
proposes a methodology to monitor and control the liquid flow in the pipeline of industries through web server. There are many
systems to do the same, but this is about to monitor and control the flow of liquid using Internet with the help of Raspberry pi and
Arduino. The flow rate of the liquid is measured by Hall Effect sensor based flow meter. Arduino, a microcontroller development
board reads the pulses from the flow meter and sends it to Raspberry pi, a microcomputer to control the electro valve which is
connected to the pipeline. Server was setup by means of Raspberry pi..


## Content
- Water flow sensor
- Flow calculation
- Water flow detection
- Tech News

## Requirement
- Raspberry Pi
- installed OS memory card
- flow sensor
- 5V/2Amp power supply

## Water Flow Sensor

YFS201 Hall Effect Water Flow Sensor 
This sensor sits in line with the water line and contains a pinwheel sensor to measure how much water has moved through it. There is an integrated magnetic Hall-Effect sensor that outputs an electrical pulse with every revolution.

![alt text](https://github.com/Anmol17Agarwal/water_flow_detecton_using_flow_sensor/blob/main/download.jfif)

## Flow Calculation

The basis relationship for determining the liquid’s flow rate in such cases is Q=VxA, 
Q - flow rate/total flow of water through the pipe
V - average velocity of the flow and A is the cross-sectional area of the pipe
 
 Pulse frequency (Hz) = 7.5Q, Q is flow rate in Litres/minute – in Minute
Flow Rate (Litres/hour) = (Pulse frequency x 60 min) / 7.5Q – Q in hour

Pulses=7.5×Q
Q=Pulses/7.5 (This is flow rate in Litres/min)
Q=Pulses/(7.5×60) (This is flow rate in Litres/hour)

![alt text](https://github.com/Anmol17Agarwal/water_flow_detecton_using_flow_sensor/blob/main/connection.png)

## Water Flow Detection
Snapshot of the water flow setup is shown in figure .According to flow meter sensor’s data sheet 5600 pulses = 1 litres. The program is written to send the data every second.First of all, a small tank with low pressure was used. The data was like this (The liquid used here is water) 258L/hour,321 L/hour,278 L/hour,345 L/hour etc. The water flow was very slow. But even when the water is turned OFF there were some reading like 20L/hour, 31L/hour, etc.indicating zero error. All the components were checked carefully, It was found to be loose connection between the interrupt pins in arduino, sending blank pulses to the serial port and has been rectified. Now the connections are checked again and the water flow is switched ON. Now there is no error and the data it shows is perfect when the water is switched OFF it correctly shows 0 L/hour.

![alt text](https://github.com/Anmol17Agarwal/water_flow_detecton_using_flow_sensor/blob/main/Untitled.png)

## TECH News

**New type of atomic clock keeps time even more precisely!**

The design, which uses entangled atoms, could help scientists detect dark matter and study gravity's effect on time. A newly-designed atomic clock uses entangled atoms to keep time even more precisely than its state-of-the-art counterparts. The design could help scientists detect dark matter and study gravity's effect on time.



"Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less!" - Marie Curie
