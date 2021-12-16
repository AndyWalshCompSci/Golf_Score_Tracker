'''
Andy Walsh
Golf Score Tracker
3rd. of December 2021
'''

from tkinter import *
#setting stroke count for "stroke" button
stroke_counter =0
#Creating board
root = Tk()

#Setting board geometry)
root.geometry("600x500")
root.configure(bg='forest green')

#text entry (Score Goal)
string_var = StringVar()
string_var2 = StringVar()
sum_ = StringVar()
stroke_sum = StringVar()
sum_score = StringVar()
#variable for score
my_text = ""

#calculating the amount of strokes left to reach your goal
def strokes_remaining():
    course_par = string_var.get()
    score_goal= string_var2.get()

    global my_text

    try:
        int_course_par = int(course_par)
        int_score_goal = int(score_goal)
        sum_ = int_score_goal - int_course_par
        print(course_par)
        print(score_goal)
        print(sum_)
        box_4_label.config(text=sum_)
    #in case of invalid integer
    except ValueError:
        print("Please enter a valid integer")

#This is the function for the "stroke" button
#it takes your initial score goal and subracts by 1
#it then continues to subtract by that number all the way down to 0
def stroke():
    global stroke_counter
    #mess_3 = string_var.get()
    mess_2 = string_var2.get()

    global my_text
    stroke_counter = stroke_counter + 1

    try:
        int_mess_2 = int(mess_2)
        stroke_sum = int_mess_2 - 1
        stroke_sum = int_mess_2 - stroke_counter
        print(mess_2)
        print(stroke_sum)
        total_stroke_label.config(text=int(stroke_sum))
    except ValueError:
        print("Please enter a valid integer")


#function to continue to subtract numbers from score
'''
def subtract_score():
    global stroke_counter
    total_stroke_label= string_var.get()

    global my_text
    stroke_counter = stroke_counter + 1
    try:
        total_stroke = int(total_stroke_label)
        sum_score = total_stroke - stroke_counter
        print(total_stroke)
        print(sum_score)
        total_stroke_label.config(text=sum_score)



    # in case of invalid integer
    except ValueError:
        print("Please enter a valid integer")

'''


#name
box_1_label = Label(root, text='Golf Score Tracker:', font=('calibre', 25,'bold'))
box_1_label.grid(row=0, column=0)

#Course par label
box_2_label = Label(root, text='Golf Course Par:', font=('calibre', 20,'bold'))
box_2_label.grid(row=20, column=0)

#box_4_input = Entry(root, textvariable=string_var)

#Golf Course Par text entry:
entry_box_3 = Entry(root, font=('calibre', 15, 'normal'),textvariable=string_var)
entry_box_3.grid(row=20, column=1)

#Score Goal label
box_3_label = Label(root, text='Score Goal:', font=('calibre', 20,'bold'))
box_3_label.grid(row=25, column=0)

#text entry (Shots till goal)

#box_4_input = Entry(root, textvariable=string_var)
#Score goal text entry:
entry_box_4 = Entry(root, font=('calibre', 15, 'normal'),textvariable=string_var2)
entry_box_4.grid(row=25, column=1)

#Shots till goal
box_4_label = Label(root, text='Shots -par remaining to reach goal:', font=('calibre', 20,'bold'))
box_4_label.grid(row=30, column=0)

#subtract scores (button)
pop_up_btn = Button(root, text='Find Stroke Limit',command=strokes_remaining)
pop_up_btn.grid(row=35, column=0)

#Shots remaining
box_4_label = Label(root, text= "                 ", font=('calibre', 20,'bold'))
box_4_label.grid(row=30, column=1)

#take a shot (button)
pop_up_btn = Button(root, text='Stroke',command=stroke)
pop_up_btn.grid(row=35, column=1)

#Strokes remaining + stroke button
total_stroke_label = Label(root, text= "                    ", font=('calibre', 20, 'bold'))
total_stroke_label.grid(row=40, column=0)

root.mainloop()