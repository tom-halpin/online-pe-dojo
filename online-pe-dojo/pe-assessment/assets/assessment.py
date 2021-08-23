#!/usr/bin/python3

# import system from os
from os import system

module_welcome = "welcome"
module_introduction = "introduction"
module_designthinking = "design thinking"
module_gettingstarted = "getting started"

class Question:
     def __init__(self, prompt, answer, module):
          self.prompt = prompt
          self.answer = answer
          self.module = module

# Question bank
question_prompts = [
     "Q1. Who was appointed as the coach and mentor for the adaption of Product Engineering in the Universal Imports Group?\n\n(a) Charlie\n\n(b) Paulo\n\n(c) Miyagi\n\n(d) Adriana\n\n(e) Brenda\n\n",
     "Q2. In the Product Engineering Manifesto, which of the following is valued ?\n\n(a) Theory over Practice\n\n(b) Standards over Guidelines\n\n(c) Culture over Tooling\n\n",
     "Q3. What is the name given to a squad member empowered and willing to lead the Introduction of Production Engineering in their squad?\n\n(a) Champion\n\n(b) Mentor\n\n(c) Product Owner\n\n",
     "Q4. What is the first phase of the Product Engineering Lifecycle being adapted by the Universal Imports Group?\n\n(a) Architecture and Prototyping\n\n(b) Product Delivery\n\n(c) Ideation and Conceptualization\n\n ",
     "Q5. What is the first phase in the Stanford Design Thinking model?\n\n(a) Empathize\n\n(b) Ideate\n\n(c) Define\n\n(d) Test\n\n(e) Prototype\n\n",
     "Q6. Design Thinking is seen as a means of addressing which identified gap in Universal Imports Group recommended Product Engineering Lifecyle?\n\n(a) Product Delivery\n\n(b) Product Support\n\n(c) Ideation and Conceptualization\n\n",
     "Q7. Which of these is the correct sequence of the phases in the Stanford Design Thinking model?\n\n(a) Empathize -> Define -> Ideate -> Prototype -> Test\n\n(b) Ideate -> Empathize -> Define -> Prototype -> Test\n\n(c) Define -> Empathize -> Ideate -> Prototype -> Test\n\n",
     "Q8. Product Engineering is a discipline that deals with which aspects of a product?\n\n(a) Design\n\n(b) Testing\n\n(c) Delivery\n\n(d) Support\n\n(e) Development\n\n(f) All of the above\n\n",
     "Q9. The cultural pivot required for a successful adaption of Product Engineering requires a shift to which type of mindset?\n\n(a) Project\n\n(b) Product\n\n",
     "Q10. In which phase of the Product Engineering Lifecycle being adapted by the Universal Imports Group is the product released to the market?\n\n(a) Product Support\n\n(b) Product Maintenance\n\n(c) Product Delivery\n\n"
]

questions = [
     Question(question_prompts[0], "c", module_welcome),
     Question(question_prompts[4], "a", module_designthinking),
     Question(question_prompts[5], "c", module_designthinking),
     Question(question_prompts[6], "a", module_designthinking),
     Question(question_prompts[1], "c", module_gettingstarted),
     Question(question_prompts[2], "a", module_gettingstarted),
     Question(question_prompts[3], "c", module_gettingstarted),
     Question(question_prompts[7], "f", module_introduction),
     Question(question_prompts[8], "b", module_introduction),
     Question(question_prompts[9], "c", module_introduction)
]

def run_quiz(questions):

     # Get first name of the user
     firstname = ""
     try:
          myfile = open('/tmp/firstname.txt', 'r')
          firstname = myfile.read().replace('\n', '')
     except IOError:
          firstname = "student"

     score = 0
     score_designthinking = 0
     score_gettingstarted = 0
     score_introduction = 0

     # welcome the student
     system("clear")
     print("\033[1;37;40m Welcome " + firstname + " shall we play a game?\n\n")
     print("\033[1;37;40m You have nearly completed your Online Product Engineering Dojo.\n")
     print("\033[1;37;40m Complete this assessment and you are there.\n\n")
     print("\033[1;34;40m Instructions:\n\n")
     print("\033[1;34;40m - Click anywhere on this terminal window to activate the cursor.\n")
     print("\033[1;34;40m - Press return to start the assessment.\n")
     print("\033[1;34;40m - To answer a question enter the letter corresponding to your answer.\n")
     print("\033[1;34;40m - When you have answered a question press return to proceed to the next question.\n\n")
     input("\033[1;37;40m This is the way!")

     system("clear")

     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               # update the module scores
               if module_introduction == question.module:
                    score_introduction +=1
               elif module_designthinking == question.module:
                    score_designthinking +=1
               elif module_gettingstarted == question.module:
                    score_gettingstarted +=1
          system("clear")

     # candidate has to
     # answer 7 out of 10 questions
     # get at least 2 questions right from each module
     if score > 6 and score_introduction >= 2 and score_designthinking >=2 and score_gettingstarted >=2 :
          print("\033[1;32;40m You got", score, "out of", len(questions), "\n")
          print("\033[1;32;40m Congratulations " + firstname + " you have passed the assessment and have earned your Product Engineering White Belt.\n")
          print("\033[1;32;40m Use the dojo - This is the way!\n")
          open('/tmp/assessment.txt', 'w')
     else:
          print("\033[1;31;40m You got", score, "out of", len(questions), "\n")
          print("\033[1;31;40m Unfortunately " + firstname + " you haven't passed the assessment.\n")
          print("\033[1;33;40m You have a bit more work to do to get your Product Engineering White Belt.\n")
          print("\033[1;33;40m Rest assured the answers are out there.\n\n Please review the following hints as to where they might be.\n")
          if score_introduction < 2:
               print("\033[1;33;40m Take another look at the Introduction to Product Engineering module before retaking the assessment.\n")
          if score_designthinking < 2:
               print("\033[1;33;40m You may want to review the Design Thinking module before resitting the assessment.\n")
          if score_gettingstarted < 2:
               print("\033[1;33;40m Spend some more time on the Getting Started module before taking the assessment.\n")
          print("\033[1;32;40m Use the dojo - This is the way!\n")

run_quiz(questions)
