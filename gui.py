from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from json_search import JSONSearch

class JSONPathFinderGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JSONPathFinderGUI, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 10

        # Инициализация логики поиска
        self.search_engine = JSONSearch()

        # Левый блок для ввода JSON
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.6, 1))
        self.json_input = TextInput(hint_text='Вставьте JSON или перетащите файл', multiline=True, size_hint=(1, 0.8))
        left_layout.add_widget(self.json_input)

        # Правый блок для кнопок и ввода значения
        right_layout = GridLayout(cols=1, size_hint=(0.4, 1), padding=10, spacing=10)

        # Поле для ввода значения поиска
        self.search_input = TextInput(hint_text='Введите значение для поиска', multiline=False)
        right_layout.add_widget(self.search_input)

        # Кнопка "Поиск"
        search_button = Button(text='Поиск')
        search_button.bind(on_press=self.find_path)
        right_layout.add_widget(search_button)

        # Поле для отображения результатов
        self.result_output = TextInput(hint_text='Результаты поиска', multiline=True, readonly=True, size_hint=(1, 0.8))
        left_layout.add_widget(self.result_output)

        # Собираем в основной layout
        self.add_widget(left_layout)
        self.add_widget(right_layout)

        # Обработка перетаскивания файла
        Window.bind(on_dropfile=self.on_file_drop)

    def on_file_drop(self, window, file_path):
        """Обработка перетаскивания файла"""
        try:
            file_path = file_path.decode('utf-8')  # преобразуем байты в строку
            with open(file_path, 'r', encoding='utf-8') as f:
                self.json_input.text = f.read()
        except Exception as e:
            self.result_output.text = f'Ошибка открытия файла: {str(e)}'

    def find_path(self, instance):
        search_value = self.search_input.text

        if not self.search_engine.load_json_from_string(self.json_input.text):
            self.result_output.text = 'Неверный формат JSON'
            return

        results = self.search_engine.search_in_json(search_value, partial=True)

        if results:
            self.result_output.text = '\n'.join(f'{val}: {path}' for val, path in results)
        else:
            self.result_output.text = 'Значение не найдено'
