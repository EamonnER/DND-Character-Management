import customtkinter as ctk
from PIL import Image
from json import load

class_data_json = open('data/classes/classes.json')
class_data = load(class_data_json)

race_data_json = open('data/races/races.json')
race_data = load(race_data_json)


class CharacterCreation(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.geometry("650x600")

        # Grid initialisation
        self.grid_columnconfigure(0, weight=0)
        padx = 15
        pady = 10
        padding = {"padx": (padx, padx), "pady": (pady, pady)}

        # Top section
        title_frame = ctk.CTkFrame(self, height=400, corner_radius=0)
        title_frame.pack(fill=ctk.X, expand=False, anchor="center")

        def init_title():
            logo = Image.open("img/logo.png")
            tk_logo = ctk.CTkImage(logo, size=(100, 100))

            title_container_frame = ctk.CTkFrame(title_frame, fg_color="transparent")
            title_container_frame.pack()

            title_image = ctk.CTkLabel(title_container_frame, text="", image=tk_logo)
            title_image.pack(side=ctk.LEFT)

            title = ctk.CTkLabel(title_container_frame, text="Character Creation",
                                 font=ctk.CTkFont(size=40, weight="bold"))
            title.pack(side=ctk.RIGHT)

        init_title()
        
        # Name input ---------------------------------------------------------------------------------------------------
        name_frame = ctk.CTkFrame(self)
        name_frame.pack(**padding)
        
        name_label = ctk.CTkLabel(name_frame, text="Name:", font=ctk.CTkFont(size=30))
        name_label.pack(side=ctk.LEFT, **padding)
        
        name_input = ctk.CTkEntry(name_frame, font=ctk.CTkFont(size=30), width=400)
        name_input.pack(side=ctk.RIGHT, **padding)

        # Split left and right -------------
        body_frame = ctk.CTkFrame(self)
        body_frame.pack()

        left_frame = ctk.CTkFrame(body_frame)
        left_frame.pack(side=ctk.LEFT, **padding)

        right_frame = ctk.CTkFrame(body_frame)
        right_frame.pack(side=ctk.RIGHT, **padding)

        # Class input --------------------------------------------------------------------------------------------------
        selected_classes = []

        def add_class(menu, target_frame):
            input_class = menu.get()
            if input_class in selected_classes:
                return

            selected_classes.append(input_class)
            frame = ctk.CTkFrame(target_frame)
            frame.pack(**padding, fill=ctk.X, expand=True)

            frame.grid_columnconfigure(0, weight=1)
            class_name_label = ctk.CTkLabel(frame, text=input_class, font=ctk.CTkFont(weight="bold"))
            class_name_label.grid(row=0, column=0, columnspan=2)
            """
            level_label = ctk.CTkLabel(frame, text="Level: ")
            level_label.grid(row=0, column=2)
            
            levels = list(str(n) for n in range(1, 21))
            level_menu = ctk.CTkOptionMenu(frame, values=levels, width=30)
            level_menu.grid(row=0, column=3)
            """
            def delete_class():
                selected_classes.remove(input_class)
                frame.destroy()

            bin_icon = Image.open("img/bin.png")
            bin_icon = ctk.CTkImage(bin_icon, size=(20, 20))
            delete_button = ctk.CTkButton(frame, text="", image=bin_icon, width=20, command=delete_class,
                                          fg_color="#DF310C", hover_color="#912008")
            delete_button.grid(row=0, column=2, **padding)

            level_label = ctk.CTkLabel(frame, text="Level: 1")
            level_label.grid(row=1, column=2)

            def update_level_label(val):
                level = val
                level_label.configure(text="Level: " + str(int(level)))

            level_slider = ctk.CTkSlider(frame, from_=1, to=20, number_of_steps=19, command=update_level_label)
            level_slider.set(1)
            level_slider.grid(row=1, column=0, columnspan=2, **padding)

        class_frame = ctk.CTkFrame(left_frame)
        class_frame.pack(**padding)

        # Selected class list ---------------------
        class_list_frame = ctk.CTkFrame(left_frame, width=270, height=110)
        class_list_frame.pack(**padding, expand=True, fill=ctk.X)
        # -----------------------------------------

        class_label = ctk.CTkLabel(class_frame, text="Select a class:")
        class_label.grid(row=0, column=0, **padding)

        classes = list(class_data.keys())
        classes = [Class.title() for Class in classes]
        class_input = ctk.CTkOptionMenu(class_frame, values=classes)
        class_input.grid(row=0, column=1, **padding)

        class_confirm_button = ctk.CTkButton(class_frame, text="Add Class",
                                             command=lambda: add_class(class_input, class_list_frame))
        class_confirm_button.grid(row=1, column=0, columnspan=2, pady=(0, pady))

        # Race input ---------------------------------------------------------------------------------------------------
        race_frame = ctk.CTkFrame(right_frame)
        race_frame.pack(**padding)

        race_label = ctk.CTkLabel(race_frame, text="Select a Race:")
        race_label.pack(side=ctk.TOP, **padding)

        races = list(race_data.keys())
        races = [race.title() for race in races]
        race_input = ctk.CTkOptionMenu(race_frame, values=races)
        race_input.pack(side=ctk.BOTTOM, **padding)

        # Use encumbrance ----------------------------------------------------------------------------------------------
        switch_frame = ctk.CTkFrame(right_frame)
        switch_frame.pack(**padding)

        encumbrance_switch = ctk.CTkSwitch(switch_frame, text="Ignore coin weight", state=ctk.DISABLED)
        encumbrance_switch.pack(side=ctk.BOTTOM, **padding)

        encumbrance_switch = ctk.CTkSwitch(switch_frame, text="Use encumbrance")
        encumbrance_switch.pack(side=ctk.TOP, **padding)

        # Buttons ------------------------------------------------------------------------------------------------------
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(**padding, fill=ctk.X, expand=True)

        def next_page():
            name = name_input.get().strip()
            if selected_classes != [] and name != "":
                print("yues")

        next_button = ctk.CTkButton(button_frame, text="Next", font=ctk.CTkFont(size=30, weight="bold"), command=next_page)
        next_button.pack(side=ctk.LEFT, fill=ctk.X, expand=True, **padding, ipady=10)

        def cancel():
            self.destroy()

        back_button = ctk.CTkButton(button_frame, text="Cancel", font=ctk.CTkFont(size=30), command=cancel,
                                    fg_color="#DF310C", hover_color="#912008")
        back_button.pack(side=ctk.RIGHT, **padding, ipady=10)

        self.mainloop()
