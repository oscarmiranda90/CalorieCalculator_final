from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from formulas import male_bmr, female_bmr, weight_conversion, height_conversion
from tkinter import messagebox


# WELCOME TO CALORIE CALCULATOR MIFFLIN ST. JEOR!


# Setting the Formula Function


def formula():
    if name_input.get() != "":
        # destroy button and create another
        global calculate_btn
        global button_frame
        global root
        global style
        root.geometry("600x539")
        button_frame.destroy()
        calculate_btn.destroy()
        # New Button Frame after Click the first Button
        button_frame = LabelFrame(root, bg="#414141", borderwidth=0)
        # New Button after Clicking the first button
        calculate_btn = ttk.Button(button_frame, text="Calculate!", command=formula)
        # Button Layout
        button_frame.grid(row=4, column=0, columnspan=2, ipady=30, ipadx=50, sticky=W)
        calculate_btn.grid(row=0, column=0, ipadx=258, ipady=8, pady=10)

        # get user inputs a create variables for formula
        age = int(age_input.get())
        weight = weight_conversion(float(weight_input.get()), w.get())
        height = height_conversion(float(height_input.get()), h.get())
        activity = float(e.get())

        # calculations

        if sex.get() == 0:
            bmr = male_bmr(weight, height, age)
            calories = bmr * activity
        else:
            bmr = female_bmr(weight, height, age)
            calories = bmr * activity
        # Grams and Macros with their outputs
        protein = (calories * 0.25 / 4)
        carbs = (calories * 0.50 / 4)
        fat = (calories * 0.25 / 9)
        bmr_string = str(round(bmr)) + " Calories"
        calories_string = str(round(calories)) + " Calories"
        protein_string = str(round(protein, 2)) + " g of Protein"
        carbs_string = str(round(carbs, 2)) + " g of Carbs"
        fat_string = str(round(fat, 2)) + " g of Fat"
        bmr_output.config(text=bmr_string, font=("Arial", 11, "bold"))
        calories_output.config(text=calories_string, font=("Arial", 11, "bold"))
        protein_output.config(text=protein_string)
        carbs_output.config(text=carbs_string)
        fat_output.config(text=fat_string)

        # create a new frame for Fitness info ( Deficit and Surplus )
        training_frame = ttk.LabelFrame(root, text="Fitness info", height=83, width=50)
        training_frame.grid(row=3, column=0, columnspan=2, ipadx=276, ipady=20, sticky=W)

        # display fitness info depending on the GOAL
        if goalvar.get() == 1:
            deficit_calories = (str(round(calories) - 500))
            deficit_info = ("You need to eat " + deficit_calories + " Calories Approx. to Lose Weight")
            deficit_frame = ttk.Label(training_frame, text=deficit_info, style="Bg.TLabel")
            deficit_frame.grid(row=0, column=0, sticky=W)
            proteindef_calories = str(round((calories - 500) * 0.35 / 4))
            carbsdef_calories = str(round((calories - 500) * 0.40 / 4))
            fatdef_calories = str(round((calories - 500) * 0.25 / 9))
            proteindef_calories_info = "You need to eat " + proteindef_calories + "g. of Protein to maintain/gain Muscle " \
                                                                                  "while losing weight."
            carbsdef_calories_info = "You need to eat " + carbsdef_calories + "g. of Carbs to maximize fat burn while " \
                                                                              "having energy during training."
            fatdef_calories_info = "You need to eat " + fatdef_calories + "g. of Fat to have a healthy hormone balance " \
                                                                          "while losing weight."
            # Macros Labels
            protein_deficit_frame = ttk.Label(training_frame, text=proteindef_calories_info,
                                              font=("arial", 10), style="Bg.TLabel")
            carbs_deficit_frame = ttk.Label(training_frame, text=carbsdef_calories_info,
                                            font=("arial", 10), style="Bg.TLabel")
            fat_deficit_frame = ttk.Label(training_frame, text=fatdef_calories_info,
                                          font=("arial", 10), style="Bg.TLabel")
            # Macros Layout
            protein_deficit_frame.grid(row=1, column=0, sticky=W)
            carbs_deficit_frame.grid(row=2, column=0, sticky=W)
            fat_deficit_frame.grid(row=3, column=0, sticky=W)
        else:
            surplus_calories = (str(round(calories) + 300))
            surplus_info = ("You need to eat " + surplus_calories + " Calories Approx. to gain Weight/Muscle.")
            deficit_frame = ttk.Label(training_frame, text=surplus_info, font=("arial", 10), style="Bg.TLabel")
            deficit_frame.grid(row=0, column=0, sticky=W)
            proteinsur_calories = str(round((calories + 300) * 0.35 / 4))
            carbssur_calories = str(round((calories + 300) * 0.40 / 4))
            fatsur_calories = str(round((calories + 300) * 0.25 / 9))
            proteinsur_calories_info = "You need to eat " + proteinsur_calories + "g. of Protein to gain Muscle while " \
                                                                                  "gaining weight."
            carbssur_calories_info = "You need to eat " + carbssur_calories + "g. of Carbs to minimize fat gain while " \
                                                                              "having energy during training."
            fatsur_calories_info = "You need to eat " + fatsur_calories + "g. of Fat to have a healthy hormone balance " \
                                                                          "while gaining weight and muscle."
            extra_info = "It's important that you eat HIGH QUALITY food to maximize Muscle gain and minimize Body Fat gain!"
            # Macros Labels
            protein_deficit_frame = ttk.Label(training_frame, text=proteinsur_calories_info,
                                              font=("arial", 10), style="Bg.TLabel")
            carbs_deficit_frame = ttk.Label(training_frame, text=carbssur_calories_info,
                                            font=("arial", 10), style="Bg.TLabel")
            fat_deficit_frame = ttk.Label(training_frame, text=fatsur_calories_info,
                                          font=("arial", 10), style="Bg.TLabel")
            extra_info_frame = ttk.Label(training_frame, text=extra_info,
                                         font=("arial", 8, "bold", "italic"), style="Bg.TLabel")
            # Macros Layout
            protein_deficit_frame.grid(row=1, column=0, sticky=W)
            carbs_deficit_frame.grid(row=2, column=0, sticky=W)
            fat_deficit_frame.grid(row=3, column=0, sticky=W)
            extra_info_frame.grid(row=4, column=0, sticky=W)

        training_frame.grid_propagate(False)
    else:
        messagebox.showerror("Error", "Please input some data")


# Setting the root

root = tk.ThemedTk()
root.configure(background="#414141")
style = ttk.Style()
style.theme_use("equilux")
style.configure("Bg.TLabel", background="#414141", foreground="white")
style.configure("Gray.TRadiobutton", background="#414141")
style.configure("fix.TLabelframe", background="blue", foreground="white")
# root.get_themes()
# root.set_theme("equilux")
root.title("Mifflin St. Jeor Calorie Calculator.")
root.geometry("600x420")

# create main containers in root
main_frame_title = ttk.Label(root, text="Personal Info", style="Bg.TLabel")
main_frame = ttk.LabelFrame(root, labelwidget=main_frame_title)
activity_frame_title = ttk.Label(root, text="Activity Level", style="Bg.TLabel")
activity_frame = ttk.LabelFrame(root, labelwidget=activity_frame_title)
goal_frame_title = ttk.Label(root, text="Goal", style="Bg.TLabel")
goal_frame = ttk.LabelFrame(root, labelwidget=goal_frame_title)
output_frame_title = ttk.Label(root, text="Calorie Calculations", style="Bg.TLabel")
output_frame = ttk.LabelFrame(root, labelwidget=output_frame_title)
button_frame = LabelFrame(root, bg="#414141", borderwidth=0)

# Layout of all the containers
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

main_frame.grid(row=0, column=0, columnspan=2, ipady=60, ipadx=300, sticky=W)
activity_frame.grid(row=1, column=0, ipady=85, ipadx=150, sticky=W)
output_frame.grid(row=1, column=1, ipady=85, ipadx=150, sticky=W)
goal_frame.grid(row=2, column=0, columnspan=2, ipady=30, ipadx=300, sticky=W)
button_frame.grid(row=3, column=0, columnspan=2, ipadx=300, ipady=35, sticky=W)
main_frame.grid_propagate(False)
activity_frame.grid_propagate(False)
output_frame.grid_propagate(False)
goal_frame.grid_propagate(False)
button_frame.grid_propagate(False)

# ----------------Widgets in the main_frame---------------------
# Labels
name_label = ttk.Label(main_frame, text="Name: ", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
age_label = ttk.Label(main_frame, text="Age: ", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
weight_label = ttk.Label(main_frame, text="Weight: ", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
height_label = ttk.Label(main_frame, text="Height: ", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
sex = IntVar()
sex.set(0)
genre_label = ttk.Label(main_frame, text="Genre", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
sex_male = ttk.Radiobutton(main_frame, text="Male", variable=sex, value=0, style="Gray.TRadiobutton")
sex_female = ttk.Radiobutton(main_frame, text="Female", variable=sex, value=1, style="Gray.TRadiobutton")

# weight
w = IntVar()
weight_kilos = ttk.Radiobutton(main_frame, text="Kilos", variable=w, value=0, style="Gray.TRadiobutton")
weight_lbs = ttk.Radiobutton(main_frame, text="Lbs", variable=w, value=1, style="Gray.TRadiobutton")

# height
h = IntVar()
height_type = ttk.Radiobutton(main_frame, text="Centimeters", variable=h, value=0, style="Gray.TRadiobutton")
height_type2 = ttk.Radiobutton(main_frame, text="Feet", variable=h, value=1, style="Gray.TRadiobutton")

# Entries
name_input = ttk.Entry(main_frame, width=20)
age_input = ttk.Entry(main_frame, width=5)
age_input.insert(END, "0")
weight_input = ttk.Entry(main_frame, width=5)
weight_input.insert(END, "0")
height_input = ttk.Entry(main_frame, width=5)
height_input.insert(END, "0")
# layout of main frame widgets
name_label.grid(row=0, column=0, sticky=W)
name_input.grid(row=0, column=0, padx=60)
age_label.grid(row=1, column=0, sticky=W)
age_input.grid(row=1, column=0, sticky=W, padx=60)
weight_label.grid(row=1, column=1)
weight_input.grid(row=1, column=2)
height_label.grid(row=2, column=1)
height_input.grid(row=2, column=2)
genre_label.grid(row=0, column=1, sticky=W)
sex_male.grid(row=0, column=3, sticky=W)
sex_female.grid(row=0, column=4, sticky=W)
weight_kilos.grid(row=1, column=3, sticky=W)
weight_lbs.grid(row=1, column=4, sticky=W)
height_type.grid(row=2, column=3, sticky=W)
height_type2.grid(row=2, column=4, sticky=W)

# _______________ Widgets in the activity_frame ________________
e = StringVar()
e.set("1.2")
sedentary = ttk.Radiobutton(activity_frame, text="Sedentary - No Exercise",
                            variable=e, value=1.2, style="Gray.TRadiobutton")
light = ttk.Radiobutton(activity_frame, text="Light Activity / 1-3 times/week",
                        variable=e, value=1.375, style="Gray.TRadiobutton")
moderate = ttk.Radiobutton(activity_frame, text="Moderate Activity / 3-5 times/week",
                           variable=e, value=1.55, style="Gray.TRadiobutton")
very_active = ttk.Radiobutton(activity_frame, text="Hard Exercise / 6-7 times/week",
                              variable=e, value=1.725, style="Gray.TRadiobutton")
intense = ttk.Radiobutton(activity_frame, text="Intense Workout all days or Physical Job",
                          variable=e, value=1.9, style="Gray.TRadiobutton")

# Layout of activity_frame widgets

sedentary.grid(row=0, column=0, sticky=W)
light.grid(row=1, column=0, sticky=W)
moderate.grid(row=2, column=0, sticky=W)
very_active.grid(row=3, column=0, sticky=W)
intense.grid(row=4, column=0, sticky=W)

# ------------- widgets in Output BMR Calories Frame-----------------

# Labels for text output BMR, TOTAL CALORIES AND MACROS
bmr_label = ttk.Label(output_frame, text="BMR", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
bmr_output = ttk.Label(output_frame, style="Bg.TLabel")
total_calorie = ttk.Label(output_frame, text="Total Cal", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
calories_output = ttk.Label(output_frame, style="Bg.TLabel")
macros = ttk.Label(output_frame, text="Normal  Macros", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
protein_output = ttk.Label(output_frame, style="Bg.TLabel")
carbs_output = ttk.Label(output_frame, style="Bg.TLabel")
fat_output = ttk.Label(output_frame, style="Bg.TLabel")

# Layout for output bmr calories and macros

bmr_label.grid(row=0, column=5, sticky=W)
bmr_output.grid(row=1, column=5, sticky=W)
total_calorie.grid(row=3, column=5, sticky=W)
calories_output.grid(row=4, column=5, sticky=W)
macros.grid(row=0, column=5, padx=100)
protein_output.grid(row=1, column=5, padx=125, sticky=E)
carbs_output.grid(row=2, column=5, padx=125, sticky=E)
fat_output.grid(row=3, column=5, padx=125, sticky=E)

# ----------- GOAL widgets -------------------
goalvar = IntVar()
goalvar.set(0)
goal_label = ttk.Label(goal_frame, text="Choose: ", font=("Helvetica", 10, "bold"), style="Bg.TLabel")
goal_lose = ttk.Radiobutton(goal_frame, text="Gain Muscle", variable=goalvar, value=0, style="Gray.TRadiobutton")
goal_gain = ttk.Radiobutton(goal_frame, text="Lose Weight", variable=goalvar, value=1, style="Gray.TRadiobutton")

# Layout
goal_label.grid(row=0, column=0)
goal_lose.grid(row=0, column=1)
goal_gain.grid(row=0, column=2)

# ---------------- Button for Calculation--------------------------
# Button Creation
calculate_btn = ttk.Button(button_frame, text="Calculate!", command=formula)
# Button Layout
calculate_btn.grid(row=0, column=0, columnspan=2, ipadx=257, ipady=8, pady=10)

root.mainloop()
