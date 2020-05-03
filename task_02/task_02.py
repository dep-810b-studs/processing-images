from tkinter.filedialog import askopenfilename
from image_processor import ImageProcessor
from cmd_pasrer import  ImageProcessorArgs

if __name__ == "__main__":
    image_processor_args = ImageProcessorArgs()

    if image_processor_args.input_file_name is None:
        image_processor = ImageProcessor(askopenfilename())
        show_needed = True
    else:
        input_file_name, output_file_name, approx_poly_dp_coefficient = image_processor_args.input_file_name, \
                                                                        image_processor_args.output_file_name, \
                                                                        image_processor_args.approx_poly_dp_coefficient
        image_processor = ImageProcessor(input_file_name, output_file_name, approx_poly_dp_coefficient)
        show_needed = image_processor_args.is_showing_picture_needed

    image_processor.load_image_from_file()
    image_processor.find_points()
    image_processor.save_image_to_file()
    if show_needed:
        image_processor.show_processed_image()