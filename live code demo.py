from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyKivyApp(App):
	def build(self):
		return BoxLayout()

app = InteractiveLauncher(MyKivyApp())

app.run()

btn1 = Button(text="I'm Spartacus!")
app.root.add_widget(btn1)

btn2 = Button(text="NOOOOO! I'm Spartacus!")
app.root.add_widget(btn2)

app.root.orientation = 'vertical'
app.root.orientation = 'horizontal'

def my_click_action(instance):
	btn2.text = "No your not! your a very naughty boy!"

btn1.bind(on_press=my_click_action)


