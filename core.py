import sys
import controller
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug('Run core')
    controller.run()
    
