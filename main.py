# программа с двумя экранами и одной ошибкой
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class Sick(Screen):
   def __init__(self, name):
      super().__init__(name=name)
      al1 = AnchorLayout(anchor_y="bottom")
      bl1 = BoxLayout(orientation='horizontal')
      home = Button(text='Аптечка', size_hint =[.4, .1])
      sick = Button(text='Заболел', size_hint =[.4, .1])
      nothing = Button(text='???', size_hint =[.4, .1])

      al = AnchorLayout()
      bl = BoxLayout(orientation='vertical', size_hint =[.4, .3], padding=40)

      ti = TextInput()
      lab = Label(text="Введите вашу болезнь", font_size=20, bold=True)
      btn_next = Button(text='Начать')

      bl.add_widget(lab)
      bl.add_widget(ti)
      bl.add_widget(btn_next)

      bl1.add_widget(home)
      bl1.add_widget(sick)
      bl1.add_widget(nothing)

      al.add_widget(bl)
      al.add_widget(bl1)
      home.on_press = self.toHome
      nothing.on_press = self.toTest
      self.add_widget(al)


   def toHome(self):
      self.manager.transition.direction = 'up'
      self.manager.current = 'home'

   def toTest(self):
      self.manager.transition.direction = 'down'
      self.manager.current = 'test'

class Home(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        al1 = AnchorLayout(anchor_y="bottom")
        bl1 = BoxLayout(orientation='horizontal')
        home = Button(text='Аптечка', size_hint =[.4, .1])
        sick = Button(text='Заболел', size_hint =[.4, .1])
        nothing = Button(text='???', size_hint =[.4, .1])

        bl1.add_widget(home)
        bl1.add_widget(sick)
        bl1.add_widget(nothing)

        al1.add_widget(bl1)
        nothing.on_press = self.toTest
        sick.on_press = self.toSick
        self.add_widget(al1)

    def toTest(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'test'

    def toSick(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'sick'

class Test(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        al1 = AnchorLayout(anchor_y="bottom")
        bl1 = BoxLayout(orientation='horizontal')
        home = Button(text='Аптечка', size_hint =[.4, .1])
        sick = Button(text='Заболел', size_hint =[.4, .1])
        nothing = Button(text='???', size_hint =[.4, .1])

        bl1.add_widget(home)
        bl1.add_widget(sick)
        bl1.add_widget(nothing)

        al1.add_widget(bl1)
        home.on_press = self.toHome
        sick.on_press = self.toSick
        self.add_widget(al1)


    def toHome(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'home'

    def toTest(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'test'

    def toSick(self):
       self.manager.transition.direction = 'up'
       self.manager.current = 'sick'

class MyApp(App):
    def build(self):
       sm = ScreenManager()
       sm.add_widget(Sick(name='sick'))
       sm.add_widget(Home(name='home'))
       sm.add_widget(Test(name='test'))
      # можно выбрать текущий экран такой строкой:
      # sm.current = 'second' # пробуйте раскомментировать
      # а вот так работать не будет, нет экрана с таким именем:
      # sm.current = 'first' # пробуйте раскомментировать
      # потому что имя не передано конструктору класса Screen.

      # В остальном первый экран работает - он добавлен в ScreenManager первым,
      # поэтому без переключений по имени экрана нормально показывается в начале работы

       return sm

app = MyApp()
app.run()
