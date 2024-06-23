import dearpygui.dearpygui as dpg
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
    global title,sender,context
    title = dpg.add_text(test.data[1][0], tag = "title", parent = "Email helper")
    sender = dpg.add_text(test.data[1][1], tag = "sender", parent = "Email helper")
    context = dpg.add_text(test.data[1][2], tag = "context", parent = "Email helper", wrap = 2000)


dpg.create_context()

width, height, channels, data = dpg.load_image('Gmail_icon.png') # 0: width, 1: height, 2: channels, 3: data
with dpg.texture_registry():
    dpg.add_static_texture(width, height, data, tag="gmail_icon")

with dpg.window(tag = "Email helper"):
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
    dpg.draw_image("gmail_icon", (1100, 20), (1180, 80), uv_min=(0, 0), uv_max=(1, 1))




dpg.create_viewport(title='Email helper', width=1280, height=800,resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Email helper", True)
dpg.start_dearpygui()

dpg.destroy_context()