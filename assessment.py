"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: Hiding details unneed
   Encaptulation: Keeping everything together
   Polymorphism: Interchangablility of components

2. What is a class?

   Code that encaptulates definitions of similar type of things.

3. What is an instance attribute?

   A characteristic that is defined for an individual occurence 
   of a class 

4. What is a method?

   A function that defined on a class

5. What is an instance in object orientation?

   A manifestation of a class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute is a character that will inherit to the 
   instances. Instance attribute is a character that defines
   the occurence.
   For example, in "animal" class, there may be a quality that
   is "with blood". In "reptile" which is an instance of the
   class "animal", "with blood" attribute will be inherited,
   but the reptile also may have "cold blood" attribute which
   is different from the "mannal" instance that will have
   the attribute of "warm blood"
"""

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
  def __init__(self, first_name, last_name, address):
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.info = {'first_name': first_name,
                 'last_name': last_name,
                 'address': address}


class Question(object):
  
  def __init__(self, question, correct_answer):
    self.question = question
    self.correct_answer = correct_answer
    self.q_a_pair = {'question': question,
                     'correct_answer': correct_answer}

  def ask_and_evaluate(self):
    user_answer = raw_input("%s > " %self.question)
    return user_answer == self.correct_answer


class Exam(object):
  
  def __init__(self, test_name):
    self.test_name = test_name
    self.questions = []
    self.exam_all = {'test_name': self.test_name,
                     'questions': self.questions}

  def add_question(self, question, correct_answer):
    question = Question(question, correct_answer).q_a_pair
    self.questions.append(question)

  def administer(self):
    self.score = 0.0
    if self.questions:
      for q in self.questions:
        test_question = Question(q["question"], q["correct_answer"])
        if test_question.ask_and_evaluate():
          self.score += 1
    return self.score/len(self.questions)

  def take_test(self, Student):
    self.score = self.administer()
    print "The score is %s." %str(self.score)


class Quiz(Exam):
  def __init__(self, test_name):
    super(Quiz,self).__init__(test_name)
    self.score = "Not Passed"

  def administer(self):
    cnt = 0
    self.score = "Test Not Passed"
    if self.questions:
      for q in self.questions:
        test_question = Question(q["question"], q["correct_answer"])
        if test_question.ask_and_evaluate():
          cnt += 1
    if cnt >= len(self.questions)/2:
        self.score = "Test Passed"
        return self.score
    return self.score

def example():
  #     Creates an exam
  sample_exam = Exam("Mari")

  # Adds a few questions to the exam
  # These should be part of the function; no need to prompt the user for questions.
  sample_exam.add_question('1+2', '3')
  sample_exam.add_question('2+3', '5')

  # Creates a student
  stu1 = Student("Seo", "Lee", "234 Main st.")
  
  # # Administers the test for that student using the take test function you just wrote
  print sample_exam.administer()

  # Test "take_test" module in Exam
  sample_exam.take_test(stu1)
  print sample_exam.score

  # Test "Quiz" module inheriting Exam
  sample_quiz = Quiz("quiz1")
  sample_quiz.add_question('2-1', '1')
  sample_quiz.add_question('5-2', '3')
  print sample_quiz.administer()

example()

