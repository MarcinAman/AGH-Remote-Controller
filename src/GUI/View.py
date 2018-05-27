import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, send_communicate, activate_voice):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.pack()
        self.send = send_communicate
        self.activate_voice = activate_voice

    def create_labels(self, facilities_collection):
        """
        Filling window with button and labels
        :param facilities_collection: list of facilites. Function uses fields like name and description
        """
        for facility_index in range(0, len(facilities_collection)):
            tk.Label(self, text=facilities_collection[facility_index].description, height=2) \
                .grid(row=facility_index, column=0)
            self.generate_button("ON", facility_index, facilities_collection[facility_index])
            self.generate_button("OFF", facility_index, facilities_collection[facility_index])

        tk.Button(self, text="Uzyj glosu", command=lambda: self.activate_voice()).grid(row=len(facilities_collection))

        tk.Button(self, text="QUIT", fg="red",
                  command=self.root.destroy) \
            .grid(row=len(facilities_collection)+1)

    def generate_button(self, label, facility_index, facility_element):
        """
        Higher level interface to easily create buttons and attach them to frame
        :param label: Button name. Can be either ON or OFF
        :param facility_index: index of button's row
        :param facility_element: associated facility name passed to onClick action
        """
        if label == 'ON':
            tk.Button(self, text="ON", width=1, height=1,
                      command=lambda: self.button_handler("ON", facility_element.name)) \
                .grid(row=facility_index, column=1)
        else:
            tk.Button(self, text="OFF", width=1, height=1,
                      command=lambda: self.button_handler("OFF", facility_element.name)) \
                .grid(row=facility_index, column=2)

    def button_handler(self, button_type, facility_code):
        self.send(button_type + ' ' + facility_code)

    def render_error_popup(self,title,message):
        """
        Method primarily used with voice recognition to handle situations where it is impossible to recognise
        :param title: box's title
        :param message: content of a message label
        """
        messagebox.showinfo(title=title,message=message)
