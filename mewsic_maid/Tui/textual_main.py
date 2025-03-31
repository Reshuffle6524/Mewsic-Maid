
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup, VerticalScroll
from textual.widgets import Footer, Header,Label, Button, Input, Static, ListItem, ListView

import sys
from mewsic_maid.Constants import ascii_art
import ptmv


class Title(Label):
    """Titleing"""

    def compose(self) -> ComposeResult:
        title = ascii_art.TITLE
        yield Static(title, id="title")

class Autocomplete(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
            id="autocomplete"
        )
class Search(Input):

    """sometih"""

class Sources(HorizontalGroup):
    def compose(self) -> ComposeResult:
        """Create List of sources."""
        yield Button("", id="yt", variant="error")
        yield Button("", id="spotify", variant="success")
        yield Button("", id="bandcamp")

class MainArea(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Title()
        yield Search(placeholder="Search", id="search")



        yield VerticalScroll(Sources())


class MewsicMaidTui(App):
    """A Textual app to manage stopwatches."""
    CSS_PATH = "../mewsicmaid.tcss"

    BINDINGS = [
        ("ctrl+f", "app.focus('search')", "Search"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield MainArea()

        yield Autocomplete()

    def action_focus_search(self) -> None:
        """An action to toggle dark mode."""
        Search().focus()

if __name__ == "__main__":


    #image_path ="/home/d-d/Mewsic-Maid/Luckystar.webm"
    #subprocess.run(["timg", image_path, "-W", "--scroll", "-p", "quarter", "-U", "--color8"])
    ptmv.__main__.main("/tv-glitch.webm")

    app = MewsicMaidTui()
    app.run()
