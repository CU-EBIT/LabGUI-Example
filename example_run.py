#!/usr/bin/env python3

### If running a server manually, replace the key below with the one your server uses
import LabGUI.lab_gui.utils.data_client as data_client
data_client.DATA_SERVER_KEY = "LabGUI_Example"
### If you have multiple servers running, change the lookup port as follows:
import LabGUI.lab_gui.utils.data_server as server
server.ServerProvider.PORT = 12345
data_client.ServerFinder.PORT = server.ServerProvider.PORT

def make_modules(main):
    """Here we add a few of our own modules.

    We add 2 test devices, which report random values, the second of which is our custom one,
    and then a SaveModule for saving settings.

    Args:
        main (MainModule): module having sub modules added
    """
    from LabGUI.lab_gui.examples.widgets.test_device import TestDevice

    module = TestDevice(main, id=27, data_key="Test_Value_A")
    main.plot_widget.addDock(module.dock)
    main._modules.append(module)
    _module = module

    from example_widgets.example_widget import TestDevice10
    module = TestDevice10(main, id=25, data_key="Test_Value_B")
    # This test device we manually place to the right of the previous
    main.plot_widget.addDock(module.dock, 'right', _module.dock)
    main._modules.append(module)
    _module = module

    from LabGUI.lab_gui.widgets.base_control_widgets import SaveModule

    module = SaveModule()
    # By not specifying location, it goes below the rest.
    main.plot_widget.addDock(module.dock)
    main._modules.append(module)
    _module = module

if __name__ == '__main__':
    from LabGUI.lab_gui import main_gui

    # Add some modules to run
    from LabGUI.lab_gui.modules import control_module
    control_module.make_modules = make_modules
    main_gui.__modules__.append(control_module.MainModule)
    
    from LabGUI.lab_gui.modules import live_plot
    main_gui.__modules__.append(live_plot.PlotModule)

    # Start the gui
    main_gui.start()
