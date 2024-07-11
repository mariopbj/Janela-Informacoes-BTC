import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import pegar_informacoes
import time

time.sleep(5)

class MyWidget(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Informações do Bitcoin")
        self.set_default_size(400, 240)
        
        # Remover a barra de título e bordas da janela
        self.set_decorated(False)
        
        # Definir a cor de fundo da janela
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_data(b"""
            window {
                background-color: #333333;
            }
            label {
                color: #b6ff00;
                font-size: 20px;
                font-weight: bold;
            }
            label.title {
                font-size: 30px;
                font-weight: bold;
                color: #b6ff00;
            }
        """)
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        # Caixa vertical para organizar os widgets
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox.set_border_width(20)
        
        # Título
        title = Gtk.Label(label="BTC")
        title.get_style_context().add_class("title")
        title.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(title, False, False, 0)
        
        # Espaçamento entre o título e os parágrafos
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        vbox.pack_start(separator, False, False, 10)
        
        # Caixa vertical para os parágrafos
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        
        # Parágrafos
        labels = [
            ("Valor:", '${:,.2f}'.format(pegar_informacoes.preco_btc())),
            ("Multiplo de Mayer:", f"{str(pegar_informacoes.calcular_multiplo_de_mayer())[:4]}"),
            ("Taxa On-Chain:", "Indisponivel"),
        ]
        
        for left_text, right_text in labels:
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            
            left_label = Gtk.Label(label=left_text)
            left_label.set_justify(Gtk.Justification.LEFT)
            left_label.set_xalign(0)
            
            right_label = Gtk.Label(label=right_text)
            right_label.set_justify(Gtk.Justification.RIGHT)
            right_label.set_xalign(1)
            
            hbox.pack_start(left_label, True, True, 0)
            hbox.pack_start(right_label, True, True, 0)
            info_box.pack_start(hbox, False, False, 0)
        
        vbox.pack_start(info_box, False, False, 0)
        self.add(vbox)
        
        # Para mover a janela, conectamos o evento de clique do mouse
        vbox.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        vbox.connect("button-press-event", self.start_move)
        
        # Obter a resolução da tela e definir a posição da janela
        display = Gdk.Display.get_default()
        monitor = display.get_monitor(0)
        geometry = monitor.get_geometry()
        scale_factor = monitor.get_scale_factor()
        
        screen_width = geometry.width * scale_factor
        screen_height = geometry.height * scale_factor
        
        window_width, window_height = self.get_size()
        x_position = screen_width - window_width
        y_position = 0
        
        self.move(x_position, y_position)

    def start_move(self, widget, event):
        self.begin_move_drag(event.button, int(event.x_root), int(event.y_root), event.time)

win = MyWidget()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()