from time import sleep
class TrafficLight:
    __color = 'Черный'

    def running(self):
        while True:
             print('TrafficLight is red now')
             sleep(7)
             print('TrafficLight is yellow now')
             sleep(2)
             print('TrafficLight is green now')
             sleep(7)
             print('TrafficLight is yellow now')
             sleep(2)
trafficlight = TrafficLight()
trafficlight.running
print(trafficlight)