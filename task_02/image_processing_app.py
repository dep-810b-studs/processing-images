import tkinter as tk
from tkinter import Button
from tkinter.filedialog import askopenfilename


class ImageProcessingApp(tk.Tk):
    def __init__(self, image_processor):
        self.__image_processor = image_processor
        tk.Tk.__init__(self)
        self.title("Hands photo processing application")
        self.geometry("500x260")
        self.resizable(False, False)

        self.__load_button = Button(self, text="Load image from file", command=self.load_from_file,
                                    width=61, height=2)
        self.__load_button.pack()

        self.__process_button = Button(self, text="Process image", command=self.process_image, state="disabled",
                                       width=61, height=2)
        self.__process_button.pack()

        self.__show_button = Button(self, text="Show processed image", command=self.show_processed_image,
                                    state="disabled", width=61, height=2)
        self.__show_button.pack()

        self.__save_button = Button(self, text="Save processed image to file", command=self.save_to_file,
                                    state="disabled", width=61, height=2)

        self.__save_button.pack()

        self.__exit_button = Button(self, text="Exit", command=self.exit, width=61, height=2)
        self.__exit_button.pack()

    def load_from_file(self):
        self.__image_processor.load_image_from_file(askopenfilename())
        self.__process_button["state"] = "normal"

    def process_image(self):
        self.__image_processor.find_points()
        self.__show_button["state"] = "normal"
        self.__save_button["state"] = "normal"

    def show_processed_image(self):
        self.__image_processor.show_processed_image()

    def save_to_file(self):
        self.__image_processor.save_image_to_file()

    def exit(self):
        self.quit()