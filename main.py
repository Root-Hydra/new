from kivymd.app import MDApp
from kivymd.ui.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.ui.label import MDLabel
from kivymd.ui.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import threading
import time

class WiFiBruteApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        
        # মেইন কন্টেইনার (গাঢ় নীল/কালো ব্যাকগ্রাউন্ড)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # হেডার টাইটেল - আপনার স্ক্রিনশটের মতো
        header = MDLabel(
            text="[b][color=00FF00]W8WifiBrute V1[/color][/b]",
            markup=True,
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=50
        )
        layout.add_widget(header)

        sub_header = MDLabel(
            text="[color=2196F3]@Mr-Unsung / BDCS Team[/color]",
            markup=True,
            halign="center",
            font_style="Caption",
            size_hint_y=None,
            height=30
        )
        layout.add_widget(sub_header)

        # বাটন লেআউট
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=12)
        
        scan_btn = Button(
            text="➤ SCAN",
            background_normal='',
            background_color=get_color_from_hex("#00FF00"),
            color=(0,0,0,1),
            bold=True,
            on_release=self.start_scan
        )
        
        history_btn = Button(
            text="⚑ HISTORY",
            background_normal='',
            background_color=get_color_from_hex("#FFFF00"),
            color=(0,0,0,1),
            bold=True
        )
        
        btn_layout.add_widget(scan_btn)
        btn_layout.add_widget(history_btn)
        layout.add_widget(btn_layout)

        # টার্মিনাল/আউটপুট উইন্ডো
        self.output_terminal = MDLabel(
            text="[color=00FF00][*] READY TO ATTACK...[/color]",
            markup=True,
            halign="left",
            valign="top",
            font_name="Roboto",
            padding=(10, 10)
        )
        layout.add_widget(self.output_terminal)
        
        screen.add_widget(layout)
        return screen

    def start_scan(self, instance):
        self.output_terminal.text = "[color=FFFF00][*] SCANNING FOR TARGETS...[/color]"
        # ব্যাকগ্রাউন্ড থ্রেডে স্ক্যানিং সিমুলেশন
        threading.Thread(target=self.simulate_scan).start()

    def simulate_scan(self):
        time.sleep(2)
        scan_results = (
            "[color=00FF00][+] Detected 3 targets | SELECT TO BREACH[/color]\n\n"
            "⚡ Nazmul@GrinNet\n   Security: [WPA2]\n   Signal: ▆▆▆▆  (-76 dBm)\n\n"
            "⚡ Nadia wifi\n   Security: [WPA2]\n   Signal: ▆▆▆    (-67 dBm)\n\n"
            "⚡ BDCS_Scanner\n   Security: [WPA2]\n   Signal: ▆▆▆▆▆ (-50 dBm)"
        )
        self.output_terminal.text = scan_results
        self.show_target_dialog()

    def show_target_dialog(self):
        # image_1449fe.jpg এর মতো ডায়ালগ বক্স
        self.dialog = MDDialog(
            title="⚡ TARGET ANALYSIS",
            type="custom",
            content_cls=MDLabel(
                text="SSID: Nazmul@GrinNet\nBSSID: e4:be:ed:bb:82:55\n\n[color=00FF00]>> Ready for Dictionary Attack?[/color]",
                markup=True,
                theme_text_color="Secondary"
            ),
            buttons=[
                Button(text="CONNECT", color=(0.5, 0, 0.5, 1), background_normal=''),
                Button(text="DICTIONARY", color=(0.5, 0, 0.5, 1), background_normal=''),
            ],
        )
        self.dialog.open()

if __name__ == "__main__":
    WiFiBruteApp().run()