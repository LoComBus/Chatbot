import tkinter

main_window = tkinter.Tk()

# profile image
image = tkinter.PhotoImage(file="/Users/columbus/Desktop/Anna_bot2.png")
image = image.subsample(2,2)

label = tkinter.Label(main_window, image=image)

label.pack()

tkinter.mainloop()