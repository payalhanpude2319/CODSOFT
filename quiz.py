class Question:
    def __init__(self, text, choose, answer):
        self.text = text
        self.choose = choose
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        if self.question_index < len(self.questions):
            return self.questions[self.question_index]
        else:
            return None

    def display_score(self):
        print(f"Score: {self.score}/{len(self.questions)}")

    def next_question(self):
        question = self.get_question()
        if question:
            print(question.text)
            for i, choose in enumerate(question.choose, start=1):
                print(f"{i}. {choose}")

            user_answer = input("Enter the number  of your answer: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.choose):
                    if question.check_answer(user_answer):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print("Incorrect. The correct answer is: ", question.choose[question.answer - 1], "\n")
                else:
                    print("Invalid input. Please enter a valid choose.\n")
            else:
                print("Invalid input. Please enter a number.\n")

            self.question_index += 1
        else:
            print("Quiz completed sucessfully.")
            self.display_score()


# Define your questions here
questions = [
    Question("What is common between Kutty, Shankar, Laxman and Sudhir Dar? ",["Flim Direction", "Drawing Cartoons", "Instrumental Music", "Classical Dance"], 2),
    Question("Who was known as Iron man of India?", ["Govind Ballabh Pant ", "Jawaharlal Nehru ", "Subhash Chandra Bose", "Saradar Vallabhbhai Patel"], 4),
    Question("The Indian to beat the computers in mathematical Wizardry is?", ["Ramanujam", "Rina Panigrahi", "Raja Ramanna", "Shakunthala Devi"], 4),
    Question("Garampani sanctuary is located at ?",["Junafarh,Gujarat", "Diphu, Assam", "Kohima, Nagaland", "Gangtok,Sikkim"],2),
    Question("Entomology is the science that studies?", ["Behavior of human beings","Insects", "The origin and history of technical and scientific terms", "The formation of rocks"],2)         
             
]

# Create a quiz instance
quiz = Quiz(questions)

# Start the quiz
while quiz.get_question():
    quiz.next_question()

# Display the final score
quiz.display_score()
