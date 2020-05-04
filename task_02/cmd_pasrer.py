import argparse


class ImageProcessorArgs:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Program to find points - ends of fingers on hands photos")

        parser.add_argument("-i", "--input-file-name", type=str,
                            help="String that contain input image filename to load", dest="input_file_name")
        parser.add_argument("-o", "--output-file-name", type=str,
                            help="String that contain processed image filename to save", dest="output_file_name")
        parser.add_argument("-c", "--coefficient", type=float,
                            help="Approximation Poly DP Coefficient", dest="coefficient")
        parser.add_argument("-s", "--show", type=bool,
                            help="Is show final picture needed or now", dest="show_needed")

        args = parser.parse_args()

        self.__input_file_name = args.input_file_name
        self.__output_file_name = args.output_file_name
        self.__approx_poly_dp_coefficient = args.coefficient
        self.__show_needed = False if args.show_needed is None else args.show_needed

    @property
    def input_file_name(self):
        return self.__input_file_name

    @property
    def output_file_name(self):
        return self.__output_file_name

    @property
    def approx_poly_dp_coefficient(self):
        return self.__approx_poly_dp_coefficient

    @property
    def is_showing_picture_needed(self):
        return self.__show_needed
