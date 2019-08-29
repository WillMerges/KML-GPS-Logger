import GPSLogger
import GPSDevice


if __name__ == '__main__':
    GPS = GPSDevice.GPS_Device()
    logger = GPSLogger.GPS_Logger("test", GPS, 'test.txt')

    for i in range(10000):
        pass
        
    logger.kill()
