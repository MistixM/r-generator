import customtkinter
import time
import os
import logging

from generate_accounts import start
from favorite_bot import favorite

from threading import Thread

logging.basicConfig(filename='debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# GLOBAl VARIABLES
account_generated = 0

info_messages = None
auto_generation = False
is_configurator_open = False
auto_generation_delay = 0
auto_account_limit = 0
account_info = None

def main():
    global info_messages, account_info

    WIDTH, HEIGHT = 740, 400
    MIN_WIDTH, MIN_HEIGHT = 640, 337

    app = customtkinter.CTk()
    app.geometry(f"{MIN_WIDTH}x{MIN_HEIGHT}")
    app.resizable(True,True)
    app.title("R-Generator")
    app.minsize(MIN_WIDTH, MIN_HEIGHT)
    app.maxsize(WIDTH, HEIGHT)

    app.protocol('WM_DELETE_WINDOW', lambda: os._exit(125))

    # Configure grid columns and rows
    for index in range(5):
        app.grid_columnconfigure(index, weight=1)
        app.grid_rowconfigure(index, weight=1)

    # Fonts
    h1_font = customtkinter.CTkFont("assets/fonts/roboto-regular.ttf", 21)
    h2_font = customtkinter.CTkFont("assets/fonts/roboto-regular.ttf", 18)
    p_font = customtkinter.CTkFont("assets/fonts/roboto-light.ttf", 13)

    title = customtkinter.CTkLabel(app, 
                                   text="R-Generator",
                                   font=h1_font)
    
    title.grid(row=0, columnspan=5, pady=30, padx=0)

    info_messages = customtkinter.CTkLabel(app,
                                           text="",
                                           font=p_font)
    info_messages.grid(row=5, columnspan=5, pady=10)

    selector_frame = customtkinter.CTkFrame(app, width=150)
    selector_frame.grid(row=1, column=0, padx=10, pady=0, sticky="nw")
    selector_frame.grid_columnconfigure(0, weight=1)

    content_frame = customtkinter.CTkFrame(app, width=430, height=215)
    content_frame.grid(row=1, column=1, columnspan=4, padx=0, pady=0, sticky="nw")
    for index in range(5):
        content_frame.grid_columnconfigure(index, weight=1)


    account_generator_btn = customtkinter.CTkButton(selector_frame, 
                                                    width=100, 
                                                    text="Account Generator", 
                                                    fg_color="transparent", 
                                                    hover_color="#383838", 
                                                    anchor='w',
                                                    command=lambda: open_account_generator(content_frame, h2_font),
                                                    font=p_font)
    
    account_generator_btn.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

    favorite_bot_btn = customtkinter.CTkButton(selector_frame, 
                                               width=100, 
                                               text="Favorite Bot", 
                                               fg_color="transparent", 
                                               hover_color="#383838", 
                                               anchor='w',
                                               command=lambda: open_favorite_bot(content_frame, h2_font),
                                               font=p_font)
    
    favorite_bot_btn.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

    account_info = customtkinter.CTkLabel(selector_frame, text=f"Accounts: {check_accounts_count()}")
    account_info.grid(rowspan=5, column=0, pady=10, padx=10, sticky="ew")

    app.mainloop()


def open_account_generator(frame, font):
    clear_frame(frame)
    
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    title = customtkinter.CTkLabel(frame, 
                                   text="Account Generator", 
                                   font=font,
                                   anchor="center")
    
    title.grid(row=0, column=0, columnspan=2, pady=15, padx=55, sticky="ew")

    configurator_generation_btn = customtkinter.CTkButton(frame, width=100, text="Configurator", command=lambda: open_delay_configurator(configurator_generation_btn))
    configurator_generation_btn.grid(row=1, column=1, pady=5, padx=(5, 35), sticky="ew")

    generate_btn = customtkinter.CTkButton(frame, width=100, text="Generate", command=lambda: generate_account(frame, generate_btn))
    generate_btn.grid(row=1, column=0, pady=5, padx=(35, 5), sticky="ew")

    frame = customtkinter.CTkScrollableFrame(frame, width=430, height=80)
    frame._scrollbar.configure(height=0, width=12)
    frame._scrollbar._button_color = "#919191"
    frame._scrollbar._button_hover_color = "#737373"

    for index in range(5):
        frame.grid_columnconfigure(index, weight=1)

    frame.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="nswe")

    id_index = customtkinter.CTkLabel(frame, text="ID")
    id_index.grid(row=0, column=0, pady=5, padx=0)

    cookie = customtkinter.CTkLabel(frame, text="Cookie")
    cookie.grid(row=0, column=1, pady=5, padx=5)


def open_favorite_bot(frame, font):
    clear_frame(frame)

    title = customtkinter.CTkLabel(frame, 
                                text="Favorite Bot", 
                                font=font,
                                anchor='w')
    
    title.grid(row=0, column=0, pady=10, padx=25, sticky="w")

    cloth_input = customtkinter.CTkEntry(frame, width=135, placeholder_text="Enter your cloth ID")
    cloth_input.grid(row=1, column=0, pady=10, padx=25, sticky='w')

    cloth_acc_input = customtkinter.CTkEntry(frame, width=135, placeholder_text="Account limit")
    cloth_acc_input.grid(row=1, column=1, pady=10, padx=25, sticky='w')

    cloth_request_delay = customtkinter.CTkEntry(frame, width=135, placeholder_text="Request delay")
    cloth_request_delay.grid(row=2, column=0, pady=10, padx=25, sticky='w')

    def check_cloth_delay_input():
        try:
            cloth_request_delay_int = int(cloth_request_delay.get())
        except Exception as e:
            cloth_request_delay_int = 0
        
        return cloth_request_delay_int
    cloth_button = customtkinter.CTkButton(frame, width=135, text="Start", command=lambda: fav_clothes(cloth_input, cloth_acc_input, cloth_button, check_cloth_delay_input()))
    cloth_button.grid(row=2, column=1, padx=25, pady=15)

def fav_clothes(cloth_input, cloth_acc, button, delay):
    global info_messages

    cloth_id = cloth_input.get()
    cloth_acc_count = cloth_acc.get()

    if cloth_id == "" or " " in cloth_id or cloth_id.isalpha():
        info_messages.configure(text="Please enter a valid ID")
        return
    
    if cloth_acc_count == "" or " " in cloth_acc_count or cloth_acc_count.isalpha():
        info_messages.configure(text="Please enter a valid limit")
        return
    
    button.configure(state="disabled")
    info_messages.configure(text="Liking..")
    
    fav_thread = Thread(target=favorite, args=(cloth_id, cloth_acc_count, info_messages, button, delay))
    fav_thread.daemon = True
    fav_thread.start()

def generate_account(frame, clicked_button):
    global account_generated, info_messages, auto_account_limit, auto_generation_delay, account_info

    info_messages.configure(text="Generating..")

    def run_scraper():
        if auto_generation:
            clicked_button.configure(state='disabled')

            current_account = 0
            while auto_generation:
                if current_account == auto_account_limit:
                    current_account = 0
                    info_messages.configure(text=f"Cooldown: {auto_generation_delay} seconds")

                    time.sleep(auto_generation_delay)

                cookies = start(info_messages)
                update_ui_with_cookies(cookies)
                current_account += 1

            clicked_button.configure(state='normal')

        else:
            clicked_button.configure(state='disabled')
            cookies = start(info_messages)
            update_ui_with_cookies(cookies)

    # Run the scraping in a separate thread
    scraper_thread = Thread(target=run_scraper)
    scraper_thread.daemon = True
    scraper_thread.start()

    def update_ui_with_cookies(cookies):
        global account_generated

        account_generated += 1
        cookie_str = str(cookies)[:45]  # Limit string length for display

        id_label = customtkinter.CTkLabel(frame, text=account_generated)
        id_label.grid(row=account_generated, column=0, pady=5, padx=0)

        cookie_label = customtkinter.CTkLabel(frame, text=cookie_str, anchor='w')
        cookie_label.grid(row=account_generated, column=1, pady=5, padx=5)

        info_messages.configure(text=f"Account was generated!")
        account_info.configure(text=f"Accounts: {check_accounts_count()}")

        if not auto_generation:
            clicked_button.configure(state='normal')

def open_delay_configurator(delay_btn):
    global is_configurator_open, auto_generation, auto_generation_delay, auto_account_limit

    if not is_configurator_open:
        is_configurator_open = True

        configurator = customtkinter.CTkToplevel()

        configurator.geometry("450x150")
        configurator.title("Delay Configurator")
        configurator.resizable(False, False)

        # Configure rows and columns
        for index in range(4):
            configurator.grid_columnconfigure(index, weight=1)
            configurator.grid_rowconfigure(index, weight=1)

        # Create and place the checkbox and entry widget
        auto_checkbox = customtkinter.CTkCheckBox(configurator, 
                                                checkbox_width=20, 
                                                checkbox_height=20, 
                                                text="Auto Generation",
                                                command=lambda: on_toggle())

        if auto_generation:
            auto_checkbox.select()

        auto_checkbox.grid(row=0, column=0, columnspan=2, sticky='ew', padx=(20, 5), pady=15)

        auto_delay = customtkinter.CTkEntry(configurator, placeholder_text="Delay")
        auto_delay.grid(row=0, column=2, sticky='ew', padx=(20, 5), pady=15)
        
        if auto_generation_delay > 0:
            auto_delay.insert(0, auto_generation_delay)

        auto_account_limit_input = customtkinter.CTkEntry(configurator, placeholder_text="Limit")
        auto_account_limit_input.grid(row=1, column=2, sticky='ew', padx=(20, 5), pady=0)

        if auto_account_limit > 0:
            auto_account_limit_input.insert(0, auto_account_limit)

        info_log = customtkinter.CTkLabel(configurator, text="")
        info_log.grid(row=2, column=0, columnspan=3, pady=5, padx=30, sticky='ew')

        # Disable the button when the configurator is open
        delay_btn.configure(state='disabled')
        
        # Handle the window close event
        configurator.protocol("WM_DELETE_WINDOW", lambda: on_configurator_closed())
        
        def on_configurator_closed():
            global is_configurator_open, auto_generation_delay, auto_account_limit

            delay_btn.configure(state='normal')
            try:
                auto_generation_delay = int(auto_delay.get())
            except Exception as e:
                pass
            
            try:
                auto_account_limit = int(auto_account_limit_input.get())
            except Exception as e:
                pass

            is_configurator_open = False
            configurator.destroy()
        
        def on_toggle():
            global auto_generation

            if not auto_checkbox.get():
                auto_generation = False
                info_log.configure(text="Auto generation was disabled")

            else:
                info_log.configure(text="Auto generation was enabled")
                auto_generation = True
    else:
        delay_btn.configure(state='disabled')

def check_accounts_count():
    return len(os.listdir("accounts/"))

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    main()