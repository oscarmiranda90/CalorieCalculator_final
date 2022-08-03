from tkinter import *
from formulas import male_bmr, female_bmr, weight_conversion, height_conversion


#  _________________CALORIE CALCULATOR_____________________
# FORMULA: Mifflin St Jeor with an Activity coefficient


def formula():
    # destroy button and create another
    global calculate_btn
    global button_frame
    global root
    root.geometry("484x494")
    button_frame.destroy()
    calculate_btn.destroy()
    button_frame = LabelFrame(root)
    button_frame.grid(row=8, column=0, sticky=NSEW)
    calculate_btn = Button(button_frame, text="Calculate!", command=formula, height=3, pady=8)
    calculate_btn.grid(row=6, ipadx=209)

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
    training_frame = LabelFrame(root, text="Fitness info", height=83, width=50)
    training_frame.grid(row=5, column=0, ipadx=217, ipady=20, sticky=NSEW)
    # display fitness info depending of the GOAL
    if goalvar.get() == 1:
        deficit_calories = (str(round(calories) - 500))
        deficit_info = ("You need to eat " + deficit_calories + " Calories Approx. to Lose Weight")
        deficit_frame = Label(training_frame, text=deficit_info)
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
        protein_deficit_frame = Label(training_frame, text=proteindef_calories_info, font=("arial", 8))
        protein_deficit_frame.grid(row=1, column=0, sticky=W)
        carbs_deficit_frame = Label(training_frame, text=carbsdef_calories_info, font=("arial", 8))
        carbs_deficit_frame.grid(row=2, column=0, sticky=W)
        fat_deficit_frame = Label(training_frame, text=fatdef_calories_info, font=("arial", 8))
        fat_deficit_frame.grid(row=3, column=0, sticky=W)
    else:
        surplus_calories = (str(round(calories) + 500))
        surplus_info = ("You need to eat " + surplus_calories + " Calories Approx. to gain Weight/Muscle.")
        deficit_frame = Label(training_frame, text=surplus_info, font=("arial", 8))
        deficit_frame.grid(row=0, column=0, sticky=W)
        proteinsur_calories = str(round((calories + 500) * 0.35 / 4))
        carbssur_calories = str(round((calories + 500) * 0.40 / 4))
        fatsur_calories = str(round((calories + 500) * 0.25 / 9))
        proteinsur_calories_info = "You need to eat " + proteinsur_calories + "g. of Protein to gain Muscle while " \
                                                                              "gaining weight."
        carbssur_calories_info = "You need to eat " + carbssur_calories + "g. of Carbs to minimize fat gain while " \
                                                                          "having energy during training."
        fatsur_calories_info = "You need to eat " + fatsur_calories + "g. of Fat to have a healthy hormone balance " \
                                                                      "while gaining weight and muscle."
        extra_info= "It's important that you eat HIGH QUALITY food to maximize Muscle gain and minimize Body Fat gain."
        protein_deficit_frame = Label(training_frame, text=proteinsur_calories_info, font=("arial", 8))
        protein_deficit_frame.grid(row=1, column=0, sticky=W)
        carbs_deficit_frame = Label(training_frame, text=carbssur_calories_info, font=("arial", 8))
        carbs_deficit_frame.grid(row=2, column=0, sticky=W)
        fat_deficit_frame = Label(training_frame, text=fatsur_calories_info, font=("arial", 8))
        fat_deficit_frame.grid(row=3, column=0, sticky=W)
        extra_info_frame = Label(training_frame, text=extra_info, font=("arial", 8))
        extra_info_frame.grid(row=4, column=0, sticky=W)

    training_frame.grid_propagate(False)


root = Tk()
root.title("Calorie Calculator By Oscar Crescente")
root.geometry("484x370")
root.config(bg="black")

# create main frame and textbooks
main_frame = LabelFrame(root, text="Personal Info")
main_frame.grid(row=0, column=0, sticky=W, ipady=15)
name_input = Entry(main_frame, width=20)
name_input.grid(row=1, column=0, padx=60)
age_input = Entry(main_frame, width=5)
age_input.insert(END, "0")
age_input.grid(row=2, column=0, sticky=W, padx=60)
weight_input = Entry(main_frame, width=5)
weight_input.insert(END, "0")
weight_input.grid(row=1, column=3)
height_input = Entry(main_frame, width=5)
height_input.insert(END, "0")
height_input.grid(row=2, column=3)

# radio buttons for genre and frame for genre
sex = IntVar()
sex.set(0)
genre_label = Label(main_frame, text="Genre")
genre_label.grid(row=0, column=2, sticky=W)
sex_male = Radiobutton(main_frame, text="Male", variable=sex, value=0)
sex_male.grid(row=0, column=4, sticky=W)
sex_female = Radiobutton(main_frame, text="Female", variable=sex, value=1)
sex_female.grid(row=0, column=5, sticky=W)

# FRAME AND Radio buttons for ACTIVITY LEVEL
activity_frame = LabelFrame(root, text="Activity Level")
activity_frame.grid(row=1, column=0, sticky=W)
e = StringVar()
e.set(1.2)
sedentary = Radiobutton(activity_frame, text="Sedentary - No Exercise", variable=e, value=1.2)
sedentary.grid(row=6, column=0, sticky=W)
light = Radiobutton(activity_frame, text="Light Activity / 1-3 times/week", variable=e, value=1.375)
light.grid(row=7, column=0, sticky=W)
moderate = Radiobutton(activity_frame, text="Moderate Activity / 3-5 times/week", variable=e, value=1.55)
moderate.grid(row=8, column=0, sticky=W)
very_active = Radiobutton(activity_frame, text="Hard Exercise / 6-7 times/week", variable=e, value=1.725)
very_active.grid(row=9, column=0, sticky=W)
intense = Radiobutton(activity_frame, text="Intense Workout all days or Physical Job", variable=e, value=1.9)
intense.grid(row=10, column=0, sticky=W)

# frame and info for GOALS LOSING AND GAINING WEIGHT

goalvar = IntVar()
goalvar.set(0)
goal_frame = LabelFrame(root)
goal_frame.grid(row=7, column=0, sticky=NSEW)
goal_label = Label(goal_frame, text="Goal: ")
goal_label.grid(row=0, column=0)
goal_lose = Radiobutton(goal_frame, text="Gain Muscle", variable=goalvar, value=0)
goal_lose.grid(row=0, column=1)
goal_gain = Radiobutton(goal_frame, text="Lose Weight", variable=goalvar, value=1)
goal_gain.grid(row=0, column=2)

# create text box labels
title_label = Label(main_frame, text="Please input your Info!")
title_label.grid(row=0, column=0, sticky=NW)
name_label = Label(main_frame, text="Full Name")
name_label.grid(row=1, column=0, sticky=W)
age_label = Label(main_frame, text="Age")
age_label.grid(row=2, column=0, sticky=W)
weight_label = Label(main_frame, text="Weight")
weight_label.grid(row=1, column=2)
height_label = Label(main_frame, text="Height")
height_label.grid(row=2, column=2)

# Height Type and radio buttons


w = IntVar()
weight_kilos = Radiobutton(main_frame, text="Kilos", variable=w, value=0)
weight_kilos.grid(row=1, column=4, sticky=W)
weight_lbs = Radiobutton(main_frame, text="Lbs", variable=w, value=1)
weight_lbs.grid(row=1, column=5, sticky=W)

# height
h = IntVar()
height_type = Radiobutton(main_frame, text="Centimeters", variable=h, value=0)
height_type.grid(row=2, column=4, sticky=W)
height_type2 = Radiobutton(main_frame, text="Feet", variable=h, value=1)
height_type2.grid(row=2, column=5, sticky=W)

# output frame

# -------------------- OUTPUT FRAME --------------------
output_frame = LabelFrame(root, text="Calorie Calculation")
output_frame.grid(row=1, column=0,padx=241, ipadx=121, sticky=NSEW)

# Labels for text output BMR, TOTAL CALORIES AND MACROS
bmr_label = Label(output_frame, text="BMR", font=("arial", 8, "underline"))
bmr_label.grid(row=6, column=5, sticky=W)
bmr_output = Label(output_frame)
bmr_output.grid(row=7, column=5, sticky=W)

total_calorie = Label(output_frame, text="Total Cal", font=("arial", 8, "underline"))
total_calorie.grid(row=8, column=5, sticky=W)
calories_output = Label(output_frame)
calories_output.grid(row=9, column=5, sticky=W)

macros = Label(output_frame, text="Normal  Macros", font=("arial", 8, "underline"))
macros.grid(row=6, column=5, padx=100)
protein_output = Label(output_frame)
protein_output.grid(row=7, column=5, padx=125, sticky=E)
carbs_output = Label(output_frame)
carbs_output.grid(row=8, column=5, padx=125, sticky=E)
fat_output = Label(output_frame)
fat_output.grid(row=9, column=5, padx=125, sticky=E)

bmr_output = Label(output_frame)
bmr_output.grid(row=7, column=5, sticky=W)
output_frame.grid_propagate(False)

# Create Buttons and button frame
button_frame = LabelFrame(root)
button_frame.grid(row=8, column=0, sticky=NSEW)
calculate_btn = Button(button_frame, text="Calculate!", command=formula, height=3, pady=8)
calculate_btn.grid(row=8, column=5, ipadx=209)
#root.resizable(False, False)
root.mainloop()
