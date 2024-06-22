import tkinter as tk
import GUI_settings as setting

root = tk.Tk()

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
window_left = int((window_width - setting.width) / 2)
window_top = int((window_height - setting.height) / 2)

root.resizable(False,False)
root.configure(background = "")
root.title("Email Helper")
root.geometry(f'{setting.width}x{setting.height}+{window_left}+{window_top}')

#login session

login_success = False
account = tk.StringVar()
password = tk.StringVar()
account.set('')
password.set('')

def check_accont_valid(account, password):
    valid = True
    if(valid):
        print(account,password)
        global login_success
        login_success = True

login_sign = tk.Label(root,
                    text = "Please Login your Gmail!",
                    font = (setting.font, 24),
                    bg = "#FFFFFF"
                    ).pack(pady = 60)

account_input = tk.Entry(root,
                        font = (setting.font, 20),
                        bd = 2,
                        width = 25,
                        textvariable = account
                        ).pack(pady = 10)

password_input = tk.Entry(root,
                        font = (setting.font, 20),
                        bd = 2,
                        width = 25,
                        textvariable = password,
                        show = '*'
                        ).pack(pady = 10)

login_button = tk.Button(root,
                        font = (setting.font, 20),
                        text = "Login",
                        command = check_accont_valid(account.get(), password.get()),
                        pady = 5
                        ).pack()

if(login_success):
    test_label = tk.Label(root, textvariable = account).pack()
    test_label2 = tk.Label(root, textvariable = password).pack()


root.mainloop()