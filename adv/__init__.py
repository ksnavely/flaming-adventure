import characters
import FACollections
import FAInputController
import FAAppStepper
import FAViews
import FAEventScheduler
import curses
import locale


locale.setlocale(locale.LC_ALL,"")

class App:
    def __init__(self):
        # appColl -- used for application level event notification
        # sets up the game resources -- maps, npcs, etc..
        self.appColl = FACollections.AppCollection()

    def run(self, screen):
        """
        Trigger the application start. This function is designed to be started
        with curses.wrapper, example:

            ```
            import curses

            import adv

            curses.wrapper(adv.app.run)
            ```

        Note that besides the views, curses also controls some keyboard
        interactions.
        """
        # Enter the application
        # TODO move appropriate references to use app.screen
        self.screen = screen
        self.before_game_loop(screen)
        self.game_loop()
        self.after_game_loop(screen)

    def before_game_loop(self, screen):
        """
        Things to do before the main game loop.
          - App resources setup
          - Intro
          - Quick start
          - Character setup
          - Game intro
        """
        # Setup the curses 'screen'
        curses.echo()
        screen.scrollok(True)

        # Display a splash/intro screen
        self.game_intro(screen)

        # Create application resources (player, maps, etc...)
        self.initialize_game_resources(screen)

    def initialize_game_resources(self, screen):
        # Setup game resources
        self.player = characters.Player("default-player")
        self.appColl.set_player(self.player)
        
        self.appColl.init_map_collection()

        # These guys need screen
        self.app_view = FAViews.AdventureView(self, screen)
        self.eventScheduler = FAEventScheduler.EventScheduler()
        self.inputController = FAInputController.InputController(self.app_view)
        self.appStepper = FAAppStepper.AppStepper()
        self.app_view.refresh()

    def game_intro(self, screen):
        """
        Display the game title and intro info.
        """
        self.app_view = FAViews.IntroView(self, screen)
        self.app_view.refresh()

    def game_loop(self):
        """
        The 'game loop' -- start sending step events to the app collection.
        """
        self.appStepper.run()

    def after_game_loop(self, screen):
        """
        Things to do after the game loop.
          - Game exit handler
        """
        pass

    def game_quit(self):
        """
        e.g. 'quit' command or the player has died. Display an outro message
        and option to:
          - TODO retry
          - TODO undead mode
          - TODO mulligan
        """
        self.app_view = FAViews.OutroView(self, self.screen)
        self.app_view.refresh()

    def game_continue(self):
        """
        game_continue

        Things to do when 'continue' is selected in the quit menu.
        """
        self.app_view = FAViews.AdventureView(self, self.screen)
        self.player.heal_continue()
        self.app_view.refresh()
        self.appStepper.restart()

app = App()
