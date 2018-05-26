import tkinter as tk


class Application(tk.Frame):
    def __init__(self, send_communicate):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.pack()
        self.send = send_communicate

    def create_labels(self, facilities_collection):
        for facility_index in range(0, len(facilities_collection)):
            tk.Label(self, text=facilities_collection[facility_index].description, height=2) \
                .grid(row=facility_index, column=0)
            self.generate_button("ON", facility_index,facilities_collection[facility_index])
            self.generate_button("OFF", facility_index,facilities_collection[facility_index])

        tk.Button(self, text="QUIT", fg="red",
                  command=self.root.destroy) \
            .grid(row=len(facilities_collection))

    def generate_button(self, label, facility_index,facility_element):
        if label == 'ON':
            tk.Button(self, text="ON", width=1, height=1,
                      command=lambda: self.button_handler("ON",facility_element.name))\
                .grid(row=facility_index, column=1)
        else:
            tk.Button(self, text="OFF", width=1, height=1,
                      command=lambda: self.button_handler("OFF",facility_element.name))\
                .grid(row=facility_index, column=2)

    def button_handler(self, button_type, facility_code):
        self.send(button_type + ' ' + facility_code)
