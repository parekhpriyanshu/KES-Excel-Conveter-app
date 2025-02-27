# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.popup import Popup
# from kivy.uix.spinner import Spinner
# from kivy.properties import StringProperty
# from kivy.core.window import Window
# from openpyxl import Workbook
# import os


# # Custom Date Input Widget
# class DateInput(BoxLayout):
#     date = StringProperty("")  # Stores the selected date as a string

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "horizontal"
#         self.spacing = 5

#         # Day Spinner
#         self.day_spinner = Spinner(
#             text="Day",
#             values=[str(i) for i in range(1, 32)],
#             size_hint=(0.3, None),
#             height=40,
#         )
#         self.day_spinner.bind(text=self.update_date)

#         # Month Spinner
#         self.month_spinner = Spinner(
#             text="Month",
#             values=[str(i) for i in range(1, 13)],
#             size_hint=(0.3, None),
#             height=40,
#         )
#         self.month_spinner.bind(text=self.update_date)

#         # Year Spinner
#         self.year_spinner = Spinner(
#             text="Year",
#             values=[str(i) for i in range(2000, 2031)],
#             size_hint=(0.4, None),
#             height=40,
#         )
#         self.year_spinner.bind(text=self.update_date)

#         self.add_widget(self.day_spinner)
#         self.add_widget(self.month_spinner)
#         self.add_widget(self.year_spinner)

#     def update_date(self, instance, value):
#         # Update the date string when a spinner value changes
#         if all(
#             [
#                 self.day_spinner.text != "Day",
#                 self.month_spinner.text != "Month",
#                 self.year_spinner.text != "Year",
#             ]
#         ):
#             self.date = f"{self.day_spinner.text}/{self.month_spinner.text}/{self.year_spinner.text}"
#         else:
#             self.date = ""


# # Screen 1: Input for company details
# class FirstScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

#         # Title
#         self.layout.add_widget(Label(text="Company Details", font_size=24, size_hint=(1, 0.1)))

#         # Input fields in a GridLayout
#         input_grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6))
#         input_grid.add_widget(Label(text="Company Name", font_size=16))
#         self.company_name = TextInput(hint_text="Enter Company Name", multiline=False, font_size=16)
#         input_grid.add_widget(self.company_name)

#         input_grid.add_widget(Label(text="Address", font_size=16))
#         self.address = TextInput(hint_text="Enter Address", multiline=False, font_size=16)
#         input_grid.add_widget(self.address)

#         input_grid.add_widget(Label(text="Gate Pass Date", font_size=16))
#         self.gate_pass_date = DateInput()  # Custom DateInput widget
#         input_grid.add_widget(self.gate_pass_date)

#         input_grid.add_widget(Label(text="Last Job ID", font_size=16))
#         self.last_job_id = TextInput(hint_text="Enter Last Job ID", multiline=False, font_size=16)
#         input_grid.add_widget(self.last_job_id)

#         self.layout.add_widget(input_grid)

#         # Next button
#         next_button = Button(text="Next", size_hint=(1, 0.1), background_color=(0, 0.7, 0, 1), font_size=18)
#         next_button.bind(on_press=self.next_screen)
#         self.layout.add_widget(next_button)

#         self.add_widget(self.layout)

#     def next_screen(self, instance):
#         # Validate inputs
#         if not all(
#             [
#                 self.company_name.text,
#                 self.address.text,
#                 self.gate_pass_date.date,
#                 self.last_job_id.text,
#             ]
#         ):
#             self.show_popup("Error", "Please fill all fields.")
#             return

#         # Save data and move to next screen
#         app = App.get_running_app()
#         app.company_data = {
#             "company_name": self.company_name.text,
#             "address": self.address.text,
#             "gate_pass_date": self.gate_pass_date.date,
#             "last_job_id": self.last_job_id.text,
#         }
#         self.manager.current = "second"

#     def show_popup(self, title, message):
#         popup = Popup(title=title, size_hint=(0.8, 0.4))
#         popup.content = Label(text=message, font_size=18)
#         popup.open()


# # Screen 2: Input for instrument details
# class SecondScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

#         # Title
#         self.layout.add_widget(Label(text="Instrument Details", font_size=24, size_hint=(1, 0.1)))

#         # Display company data
#         self.company_info = Label(font_size=16, size_hint=(1, 0.1))
#         self.layout.add_widget(self.company_info)

#         # Input fields in a GridLayout
#         input_grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6))
#         self.fields = [
#             "sr_no", "name_of_instrument", "make", "model", "id_no", "sr_num",
#             "low_range", "high_range", "unit", "l_c", "accuracy", "location",
#             "calibration_date", "due_date", "certificate_no", "remarks"
#         ]
#         self.inputs = {}
#         for field in self.fields:
#             input_grid.add_widget(Label(text=field.replace("_", " ").title(), font_size=16))
#             if field in ["calibration_date", "due_date"]:
#                 # Use DateInput for calibration_date and due_date
#                 self.inputs[field] = DateInput()
#                 input_grid.add_widget(self.inputs[field])
#             else:
#                 self.inputs[field] = TextInput(hint_text=f"Enter {field.replace('_', ' ')}", multiline=False, font_size=16)
#                 input_grid.add_widget(self.inputs[field])

#         self.layout.add_widget(input_grid)

#         # Add and Save buttons
#         button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
#         add_button = Button(text="Add Instrument", background_color=(0, 0.7, 0, 1), font_size=18)
#         add_button.bind(on_press=self.add_instrument)
#         save_button = Button(text="Save and Export", background_color=(0.2, 0.6, 1, 1), font_size=18)
#         save_button.bind(on_press=self.save_data)
#         button_layout.add_widget(add_button)
#         button_layout.add_widget(save_button)
#         self.layout.add_widget(button_layout)

#         self.add_widget(self.layout)
#         self.instruments = []

#     def on_enter(self):
#         # Display company data
#         app = App.get_running_app()
#         self.company_info.text = (
#             f"Company: {app.company_data['company_name']}\n"
#             f"Address: {app.company_data['address']}\n"
#             f"Gate Pass Date: {app.company_data['gate_pass_date']}\n"
#             f"Last Job ID: {app.company_data['last_job_id']}"
#         )

#     def add_instrument(self, instance):
#         # Validate inputs
#         if not all(
#             self.inputs[field].text if isinstance(self.inputs[field], TextInput) else self.inputs[field].date
#             for field in self.fields
#         ):
#             self.show_popup("Error", "Please fill all fields.")
#             return

#         # Save instrument data
#         instrument = {}
#         for field in self.fields:
#             if isinstance(self.inputs[field], DateInput):
#                 instrument[field] = self.inputs[field].date
#             else:
#                 instrument[field] = self.inputs[field].text
#         self.instruments.append(instrument)

#         # Clear inputs
#         for field in self.fields:
#             if isinstance(self.inputs[field], DateInput):
#                 self.inputs[field].date = ""
#             else:
#                 self.inputs[field].text = ""

#         self.show_popup("Success", "Instrument added successfully.")

#     def save_data(self, instance):
#         if not self.instruments:
#             self.show_popup("Error", "No instruments added.")
#             return

#         # Export to Excel
#         wb = Workbook()
#         ws = wb.active
#         ws.title = "Instrument Data"

#         # Write company data
#         app = App.get_running_app()
#         ws.append(["Company Name", app.company_data["company_name"]])
#         ws.append(["Address", app.company_data["address"]])
#         ws.append(["Gate Pass Date", app.company_data["gate_pass_date"]])
#         ws.append(["Last Job ID", app.company_data["last_job_id"]])
#         ws.append([])

#         # Write instrument headers
#         ws.append(self.fields)

#         # Write instrument data
#         for instrument in self.instruments:
#             ws.append([instrument[field] for field in self.fields])

#         # Save file
#         file_path = "instrument_data.xlsx"
#         wb.save(file_path)
#         self.show_popup("Success", f"Data exported to {file_path}")

#     def show_popup(self, title, message):
#         popup = Popup(title=title, size_hint=(0.8, 0.4))
#         popup.content = Label(text=message, font_size=18)
#         popup.open()


# # App Manager
# class MyApp(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(FirstScreen(name="first"))
#         sm.add_widget(SecondScreen(name="second"))
#         return sm


# if __name__ == "__main__":
#     MyApp().run()









from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.properties import StringProperty
from kivy.core.window import Window
from openpyxl import Workbook
import os


# Custom Date Input Widget
class DateInput(BoxLayout):
    date = StringProperty("")  # Stores the selected date as a string

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = 5

        # Day Spinner
        self.day_spinner = Spinner(
            text="Day",
            values=[str(i) for i in range(1, 32)],
            size_hint=(0.3, None),
            height=40,
        )
        self.day_spinner.bind(text=self.update_date)

        # Month Spinner
        self.month_spinner = Spinner(
            text="Month",
            values=[str(i) for i in range(1, 13)],
            size_hint=(0.3, None),
            height=40,
        )
        self.month_spinner.bind(text=self.update_date)

        # Year Spinner
        self.year_spinner = Spinner(
            text="Year",
            values=[str(i) for i in range(2000, 2031)],
            size_hint=(0.4, None),
            height=40,
        )
        self.year_spinner.bind(text=self.update_date)

        self.add_widget(self.day_spinner)
        self.add_widget(self.month_spinner)
        self.add_widget(self.year_spinner)

    def update_date(self, instance, value):
        # Update the date string when a spinner value changes
        if all(
            [
                self.day_spinner.text != "Day",
                self.month_spinner.text != "Month",
                self.year_spinner.text != "Year",
            ]
        ):
            self.date = f"{self.day_spinner.text}/{self.month_spinner.text}/{self.year_spinner.text}"
        else:
            self.date = ""


# Screen 1: Input for company details
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Title
        self.layout.add_widget(Label(text="Company Details", font_size=24, size_hint=(1, 0.1)))

        # Input fields in a GridLayout
        input_grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6))
        input_grid.add_widget(Label(text="Company Name", font_size=16))
        self.company_name = TextInput(hint_text="Enter Company Name", multiline=False, font_size=16)
        input_grid.add_widget(self.company_name)

        input_grid.add_widget(Label(text="Address", font_size=16))
        self.address = TextInput(hint_text="Enter Address", multiline=False, font_size=16)
        input_grid.add_widget(self.address)

        input_grid.add_widget(Label(text="Gate Pass Date", font_size=16))
        self.gate_pass_date = DateInput()  # Custom DateInput widget
        input_grid.add_widget(self.gate_pass_date)

        input_grid.add_widget(Label(text="Last Job ID", font_size=16))
        self.last_job_id = TextInput(hint_text="Enter Last Job ID", multiline=False, font_size=16)
        input_grid.add_widget(self.last_job_id)

        self.layout.add_widget(input_grid)

        # Next button with space added below
        next_button = Button(text="Next", size_hint=(1, 0.1), background_color=(0, 0.7, 0, 1), font_size=18)
        next_button.bind(on_press=self.next_screen)
        self.layout.add_widget(next_button)

        self.add_widget(self.layout)

    def next_screen(self, instance):
        # Validate inputs
        if not all(
            [
                self.company_name.text,
                self.address.text,
                self.gate_pass_date.date,
                self.last_job_id.text,
            ]
        ):
            self.show_popup("Error", "Please fill all fields.")
            return

        # Save data and move to next screen
        app = App.get_running_app()
        app.company_data = {
            "company_name": self.company_name.text,
            "address": self.address.text,
            "gate_pass_date": self.gate_pass_date.date,
            "last_job_id": self.last_job_id.text,
        }
        self.manager.current = "second"

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message, font_size=18)
        popup.open()


# Screen 2: Input for instrument details
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Title
        self.layout.add_widget(Label(text="Instrument Details", font_size=24, size_hint=(1, 0.1)))

        # Display company data
        self.company_info = Label(font_size=16, size_hint=(1, 0.1))
        self.layout.add_widget(self.company_info)

        # Input fields in a GridLayout
        input_grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6))
        self.fields = [
            "sr_no", "name_of_instrument", "make", "model", "id_no", "sr_num",
            "low_range", "high_range", "unit", "l_c", "accuracy", "location",
            "calibration_date", "due_date", "certificate_no", "remarks"
        ]
        self.inputs = {}
        for field in self.fields:
            input_grid.add_widget(Label(text=field.replace("_", " ").title(), font_size=16))
            if field in ["calibration_date", "due_date"]:
                # Use DateInput for calibration_date and due_date
                self.inputs[field] = DateInput()
                input_grid.add_widget(self.inputs[field])
            else:
                self.inputs[field] = TextInput(hint_text=f"Enter {field.replace('_', ' ')}", multiline=False, font_size=16)
                input_grid.add_widget(self.inputs[field])

        self.layout.add_widget(input_grid)

        # Add and Save buttons with spacing between
        button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        add_button = Button(text="Add Instrument", background_color=(0, 0.7, 0, 1), font_size=18)
        add_button.bind(on_press=self.add_instrument)
        save_button = Button(text="Save and Export", background_color=(0.2, 0.6, 1, 1), font_size=18)
        save_button.bind(on_press=self.save_data)
        button_layout.add_widget(add_button)
        button_layout.add_widget(save_button)
        self.layout.add_widget(button_layout)

        self.add_widget(self.layout)
        self.instruments = []

    def on_enter(self):
        # Display company data
        app = App.get_running_app()
        self.company_info.text = (
            f"Company: {app.company_data['company_name']}\n"
            f"Address: {app.company_data['address']}\n"
            f"Gate Pass Date: {app.company_data['gate_pass_date']}\n"
            f"Last Job ID: {app.company_data['last_job_id']}"
        )

    def add_instrument(self, instance):
        # Validate inputs
        if not all(
            self.inputs[field].text if isinstance(self.inputs[field], TextInput) else self.inputs[field].date
            for field in self.fields
        ):
            self.show_popup("Error", "Please fill all fields.")
            return

        # Save instrument data
        instrument = {}
        for field in self.fields:
            if isinstance(self.inputs[field], DateInput):
                instrument[field] = self.inputs[field].date
            else:
                instrument[field] = self.inputs[field].text
        self.instruments.append(instrument)

        # Clear inputs
        for field in self.fields:
            if isinstance(self.inputs[field], DateInput):
                self.inputs[field].date = ""
            else:
                self.inputs[field].text = ""

        self.show_popup("Success", "Instrument added successfully.")

    def save_data(self, instance):
        if not self.instruments:
            self.show_popup("Error", "No instruments added.")
            return

        # Export to Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Instrument Data"

        # Write company data
        app = App.get_running_app()
        ws.append(["Company Name", app.company_data["company_name"]])
        ws.append(["Address", app.company_data["address"]])
        ws.append(["Gate Pass Date", app.company_data["gate_pass_date"]])
        ws.append(["Last Job ID", app.company_data["last_job_id"]])
        ws.append([])

        # Write instrument headers
        ws.append(self.fields)

        # Write instrument data
        for instrument in self.instruments:
            ws.append([instrument[field] for field in self.fields])

        # Save file
        file_path = "instrument_data.xlsx"
        wb.save(file_path)
        self.show_popup("Success", f"Data exported to {file_path}")

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message, font_size=18)
        popup.open()


# App Manager
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        return sm


if __name__ == "__main__":
    MyApp().run()
