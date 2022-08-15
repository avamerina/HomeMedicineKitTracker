
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Application(App):
	def build(self):
		al1 = AnchorLayout(anchor_y="bottom")
		bl1 = BoxLayout(orientation='horizontal')
		home = Button(text='Аптечка', size_hint =[.4, .1])
		what = Button(text='Политика', size_hint =[.4, .1])

		al = AnchorLayout()
		bl = BoxLayout(orientation='vertical', size_hint =[.4, .3], padding=40)

		ti = TextInput()
		lab = Label(text="Введите вашу болезнь", font_size=20, bold=True)
		btn_next = Button(text='Начать')

		bl.add_widget(lab)
		bl.add_widget(ti)
		bl.add_widget(btn_next)

		bl1.add_widget(home)
		bl1.add_widget(what)

		al.add_widget(bl)
		al.add_widget(bl1)
		return al


if __name__ == "__main__":
	Application().run()
