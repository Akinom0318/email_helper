import dearpygui.dearpygui as dpg
import pyperclip as pc
import test

def check_valid():
    global login_success
    user_account_input = dpg.get_value(account)
    user_password_input = dpg.get_value(password)
    print(user_account_input,user_password_input)
    login_success = True
    clear_login_page()
    email_session()

def clear_login_page():
    dpg.delete_item("account")
    dpg.delete_item("password")
    dpg.delete_item("login_button")
    dpg.delete_item("welcome_message")
    dpg.delete_item("gmail_icon")

def email_session():
    global title,sender,context,GPT
    title = dpg.add_text(test.data[1][0], tag = "title", parent = "main")
    sender = dpg.add_text(test.data[1][1], tag = "sender", parent = "main")
    context = dpg.add_text(test.data[1][2], tag = "context", parent = "main", wrap = 2000)
    GPT = dpg.add_text("text reply~~~~~~~~~it has been attched to your clip board!",wrap = 600,
                            tag = "GPT_reply",
                            parent = "GPT",)
    pc.copy(dpg.get_value("GPT_reply"))

dpg.create_context()

with dpg.window(tag = "main", label = "Email", width = 640, height = 800,no_resize=True,no_close=True,no_move=True):
    with dpg.font_registry():
        with dpg.font(r"kaiu.ttf", 16, tag="custom font"):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(dpg.last_container())
    #login session
    login_success = False
    dpg.add_text("Welcome to Gmail helper!", tag = "welcome_message")
    account = dpg.add_input_text(tag = "account", label = "account")
    password = dpg.add_input_text(tag = "password",
                                  label = "password",
                                  password = True)
    login_button = dpg.add_button(label = "Login",
                                    tag = "login_button",
                                    callback=(check_valid))
    
with dpg.window(tag = "GPT", label = "GPT's action", width = 625, height = 800, pos = (640,0), no_resize=True, no_close=True,no_move=True):
    pass

dpg.create_viewport(title='Email Helper', width=1280, height=800,resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()