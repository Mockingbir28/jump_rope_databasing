"""
Create a database for jump rope tournaments
"""
import toga
from os import path
from os import mkdir, rmdir
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .utilities.get_data_path import get_data_path, find_databases


class JumpRopeDatabase(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        # determine if datapath exists
        valid_system, system_data_path = get_data_path()
        
        # Initialize main window
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.system_data_path = system_data_path
        self.main_window.content = main_box
        
        if valid_system and path.isdir(system_data_path):
            self.main_app()
        elif valid_system and not path.isdir(system_data_path):
            install_button = toga.Button("Install", on_press=self.create_directory)
            install_button.style.update(width=100)
            main_box.add(install_button)
            main_box.style.update(direction=COLUMN, padding=100,
                                  alignment="right")
        else:
            None
        
        self.main_window.show()
    
    def create_directory(self, widget):
        mkdir(self.system_data_path)
        widget.style.update(visibility="hidden")
        self.main_app()
    
    def main_app(self):
        # get the main container
        main_box = self.main_window.content
        
        # find databases that exist
        databases = find_databases(self.system_data_path)
        db_dropdown = toga.Selection(items=databases)
        main_box.add(db_dropdown)

        # add the uninstall button in bottom right
        
        
        

def main():
    return JumpRopeDatabase()

