import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL modules

class QuizApp:

    score = 0

    def start_quiz(self):
    # Hide the welcome message label and start the quiz
        self.welcome_label.pack_forget()
        self.next_question()

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        root.attributes("-fullscreen", True)
        
        self.welcome_label = tk.Label(root, text="Welcome to the epic quiz!!!!", font=("Helvetica", 38))
        self.welcome_label.pack(pady=20)
        



        # Initialize question and answer data
        self.questions = [
            {
                'question': "What php stands for?",
                'choices': ["Powerfull Helpfull Programing", "prehipertexprograms", "elephpant", "homepage person"],
                'correct': "elephpant"
            },
            {
                'question': "wich is bestester?",
                'choices': ["javecrypt", "piton", "see", "ccastation stylechets"],
                'correct': "see"
            },
            {
                'question': "best sistem of operationer?",
                'choices': ["wendows", "mag oz", "tempale oes", "linkus"],
                'correct': "tempale oes"
            },
            {
                'question': "what is the bestest?",
                'choices': ["php", "php", "php", "php"],
                'correct': "php"
            },
            {
                'question': "sql helowrold how>?",
                'choices': ["SELECT Say Hello, World!", "SELECT こんにちは、ワールド!", "@@^*& &i*Ud 3943i4I**& &jkIuy;!!$%", "As an AI language model developed by OpenAI, I am programmed to follow ethical guidelines and legal principles. I cannot provide assistance, information, or engage in discussions related to harmful, illegal, or unethical activities, including any form of violence or harm to individuals, governments, or property. If you have questions or need information on other topics that do not involve harm or illegal activities, please feel free to ask, and I'll be happy to provide assistance to the best of my abilities."],
                'correct': "SELECT こんにちは、ワールド!"
            },
            {
                'question': "fastest best lagua",
                'choices': ["hotmol", "subscirbe to my yotuube chanel", "skibiditoiletorcreeper.nl", "c++++++++++++++++++++"],
                'correct': "c++++++++++++++++++++"
            },
            {
                'question': "how to make dives in html?",
                'choices': ["<div> </div>", "<div> <\div>", "[divaes////][diveer]", "<div> </diiavev>"],	
                'correct': "<div> </div>"
            },
            {
                "question": "best c version",
                'choices' : ["c#++#+###", "seeing", "c++", "c"],
                'correct': "c"
            },
            {
                'question': "most smartest progarmer",
                'choices': ["me", "terry davis", "Rasmus Lerdorf", "albert einsin"],
                'correct': "terry davis"
            },
            {
                'question': "what is minceraft programes in??",
                'choices': ["javascript", "csharps", "php", "c=="],
                'correct': "javascript"
            }
                
            
        ]

        self.current_question = 0

        self.label = tk.Label(root, padx=20, pady=10)
        self.label.pack()

        self.image_label = tk.Label(root)  # Label to display the image
        self.image_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.start_button = tk.Button(root, text="Next", command=self.start_quiz)
        self.start_button.pack()

        


    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text = question_data['question']
            choices = question_data['choices']

            self.label.config(text=question_text)

        
            # Clear previous answer choice buttons
            for widget in self.button_frame.winfo_children():
                widget.destroy()

            # Create buttons for answer choices
            for choice in choices:
                choice_button = tk.Button(self.button_frame, text=choice, command=lambda c=choice: self.check_answer(c, question_data['correct']))
                choice_button.pack()

            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Finished", "You have completed the quiz! Your score is " + str(self.score) + " out of " + str(len(self.questions)) + ".")
            exit(0)

    def check_answer(self, selected_answer, correct_answer):
        if selected_answer == correct_answer:
            messagebox.showinfo("Correct", "Your answer is correct!")
            self.score += 1
            self.start_quiz()
            
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect!")
            self.start_quiz()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
