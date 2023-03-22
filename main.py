import tkinter
import customtkinter as ctk
from PIL import Image
from character_creation import CharacterCreation

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class SelectCharacter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x550")

        # Top section
        title_frame = ctk.CTkFrame(self, height=500, corner_radius=0)
        title_frame.pack(fill=ctk.X, expand=False, anchor="center")

        def init_title():
            logo = Image.open("img/logo.png")
            tk_logo = ctk.CTkImage(logo, size=(200, 200))

            title_container_frame = ctk.CTkFrame(title_frame, fg_color="transparent")
            title_container_frame.pack()

            title_image = ctk.CTkLabel(title_container_frame, text="", image=tk_logo)
            title_image.pack(side=ctk.LEFT)

            title = ctk.CTkLabel(title_container_frame, text="D&D", font=ctk.CTkFont(size=60, weight="bold"))
            title.pack(side=ctk.RIGHT)

        init_title()

        # Tab section
        tab_frame = ctk.CTkTabview(self, width=350, corner_radius=30)
        tab_frame.pack(pady=(15, 20))

        def init_tabs():
            tab_frame.add("Created Characters")
            tab_frame.add("Sample Characters")

        init_tabs()

        # Button section
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack()

        def create_new_character():
            CharacterCreation()

        def quit_app():
            self.destroy()

        def init_buttons():
            new_character_button = ctk.CTkButton(button_frame, text="Create New Character!", command=create_new_character,
                                                 font=ctk.CTkFont(size=20, weight="bold"))
            new_character_button.pack(side=ctk.LEFT, padx=5)

            quit_button = ctk.CTkButton(button_frame, text="Quit", fg_color="#DF310C", hover_color="#912008",
                                        width=100, command=quit_app, font=ctk.CTkFont(size=20))
            quit_button.pack(side=ctk.RIGHT, padx=5)

        init_buttons()

        self.mainloop()


if __name__ == "__main__":
    SelectCharacter()
