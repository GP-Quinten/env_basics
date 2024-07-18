"""
This is the main script where all functions are called to create pipelines
"""
import logging
from src.logger import init_logger
from src.parser import simple_parser


def main():
    # Parsing argument
    parser = simple_parser() # you can adjust the function in parser.py file in order to fit your need
    args = parser.parse_args()
    
    # init logger
    init_logger(level=args.log_level)
    logging.info("*" * 30)
    logging.info("Starting new sessions")
    logging.info("*" * 30)

    ## Your pipeline should be here
    print("Hello world")
    logging.info("***** Job completed *****")


if __name__ == '__main__':
    main()