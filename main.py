from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition, FadeTransition, CardTransition, RiseInTransition
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


class Manager(ScreenManager):
    pass


class ActiveSportScreen(MDScreen):
    pass


class BarreHaut(MDScreen):
    pass


class MenuProgramme(MDScreen):
    pass


class NavigationBasse(MDScreen):
    pass


class AddProg(MDScreen):
    pass


class Option(MDScreen):
    pass


class Historique(MDScreen):
    pass


#   nécessaire au dropdownMenu
class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Menu des programmes'
        self.KV_file = Builder.load_file('my_app.kv')
        self.dialog = None
        #   Création des items
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "chevron-right-circle",
                "text": f"Programme {i+1}",
                "height": dp(56),
                "on_release": lambda x=f"programme {i+1}": self.set_item(x),
            } for i in range(50)]

        # création et paramètres de DropDownMenu
        self.menu = MDDropdownMenu(
            caller=self.KV_file.ids.MenuProgramme.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=6,
            border_margin=dp(16),
            background_color=self.theme_cls.primary_light,
            elevation=4,
            radius=[20, 20, 20, 20],)
        # self.menu.bind() # pas trouvé à quoi ça sert

    def set_item(self, text_item):
        # changement de l'item et fermeture du DropDownMenu
        self.root.ids.MenuProgramme.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def switch_light(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        elif self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'

    def transition_manager(self, transition_type, direction, screen):
        if transition_type is not None:
            self.root.ids.MenuProgramme.manager.transition = eval(transition_type)
        if direction is not None:
            self.root.ids.MenuProgramme.manager.transition.direction = direction
        if screen is not None:
            self.root.current = screen

    def confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Vous souhaitez créer un nouveau programme ?",
                text="",
                type='confirmation',
                md_bg_color='orange',
                radius=[20, 20, 20, 20],
                buttons=[
                    MDFlatButton(
                        text="Non",
                        theme_text_color="Custom",
                        text_color='red',
                        on_release=self.dialog_close),
                    MDRaisedButton(
                        text="Oui",
                        theme_text_color="Custom",
                        md_bg_color='white',
                        text_color='green',
                        on_release=self.dialog_action)])
        self.dialog.open()

    def dialog_close(self, obj):
        self.dialog.dismiss()

    def dialog_action(self, obj):
        self.dialog.dismiss()
        self.root.current = 'AddProg'

    def build(self):
        self.icon = 'images/icon/MW.png'
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.4
        self.theme_cls.primary_hue = "500"
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = "Amber"  # indigo cyan DeepPurple LightGreen Purple
        return self.KV_file


MainApp().run()
