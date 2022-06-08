import cv2
import numpy as np
import tkinter as tk


def bridge(order):
    junction = []
    for index, element in enumerate(order):
        count = 0
        for x in range(index + 1, 5):
            if order[x] < element:
                count += 1
        for x in range(0, index):
            if order[x] > element:
                count += 1
        junction.append(count)

    max_junction = max(junction)
    max_junction_index = junction.index(max_junction)

    while max_junction > 0:
        junction[max_junction_index] = -1

        for x in range(max_junction_index + 1, 5):
            if order[x] < order[max_junction_index] and junction[x] != -1:
                junction[order.index(order[x])] -= 1

        for x in range(0, max_junction_index):
            if order[x] > order[max_junction_index] and junction[x] != -1:
                junction[order.index(order[x])] -= 1

        max_junction = max(junction)
        max_junction_index = junction.index(max_junction)

    result = []
    for index, x in enumerate(junction):
        if x == 0:
            result.append(order[index])

    return result


def Show_Graph(order):
    background = np.zeros((320, 480, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX

    circle_center = [80, 70]
    text_center = [70, 80]
    for i in range(5):
        cv2.circle(background, tuple(circle_center), 20, (86, 255, 34), -1)
        cv2.putText(background, str(i + 1), tuple(text_center), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        text_center[0] += 80
        circle_center[0] += 80

    circle_center = [80, 230]
    text_center = [70, 240]
    for element in order:
        cv2.circle(background, tuple(circle_center), 20, (86, 255, 34), -1)
        cv2.putText(background, str(element), tuple(text_center), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        text_center[0] += 80
        circle_center[0] += 80

    for element in bridge(order):
        first_circle = (80 * element, 90)
        i = order.index(element)
        second_circle = (80 + 80 * i, 210)
        cv2.line(background, first_circle, second_circle, (160, 160, 160), 2)

    cv2.imshow('Result', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_input_text():
    entry = input_text.get("1.0", "end")
    entry = [int(i) for i in entry.split('\n')[0]]
    if len(entry) != 5 or set(entry) != {1, 2, 3, 4, 5}:
        error = tk.Tk()
        error.title('Error')
        error.geometry("150x50")
        l = tk.Label(error, text="Wrong Entry! Try Again", border=5)
        l.pack()
    else:
        Show_Graph(entry)


first_page = tk.Tk()
first_page.title("Order")
first_page.geometry("180x150")

label = tk.Label(first_page, text="Enter Your Order", border=5)
label.pack()

input_text = tk.Text(first_page, height=1, width=10, border=5)
input_text.pack()

Start_Button = tk.Button(first_page, height=1, width=10, text="Ok", command=get_input_text)
Quit_Button = tk.Button(first_page, height=1, width=10, text="Cancel", command=first_page.destroy)

Start_Button.pack()
Quit_Button.pack()

first_page.mainloop()
