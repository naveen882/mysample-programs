"""

One would use @classmethod when he/she would want to change the behaviour of the method based on which subclass is calling the method. remember we have a reference to the calling class in a class method.

While using static you would want the behaviour to remain unchanged across subclasses
http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner/31503491#31503491
Example:

"""
class Hero:

  @staticmethod
  def say_hello():
     print("Helllo...")

  @classmethod
  def say_class_hello(cls):
     if(cls.__name__=="HeroSon"):
        print("Hi Kido")
     elif(cls.__name__=="HeroDaughter"):
        print("Hi Princess")

class HeroSon(Hero):
  def say_son_hello(self):
     print("test  hello")



class HeroDaughter(Hero):
  def say_daughter_hello(self):
     print("test  hello daughter")


testson = HeroSon()

testson.say_class_hello()

testson.say_hello()

testdaughter = HeroDaughter()

testdaughter.say_class_hello()

testdaughter.say_hello()


