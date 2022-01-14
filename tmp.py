import tkinter as tk
import tkinter.ttk as ttk
import time
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x100")
        

        self.str_date = tk.StringVar()
        self.str_time = tk.StringVar()
        self.str_date.set("*** Current Date ***")
        self.str_time.set("*** Current Time ***")


        self.label = tk.Label(self, textvariable=self.str_date,font=("Arial",24))
        self.label.pack()
        
        self.label2 = tk.Label(self, textvariable=self.str_time,font=("Arial",24))
        self.label2.pack()
        self.update_time()

        self.quit_button = tk.Button(self, text="Quit", command=self.quit,font=("Arial",24))
        self.quit_button.pack()


    def update_time(self):
        time_now = time.strftime("%H:%M:%S")
        date_now = time.strftime("%d %B, %Y")
        
        self.str_time.set(time_now)
        self.str_date.set(date_now)
        self.after(1, self.update_time)
       

        
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()
