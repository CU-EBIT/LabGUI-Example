# LabGUI-Example
Example of adding LabGUI as a submodule, and then adding your custom code

LabGUI was added via:

```
git submodule add https://github.com/CU-EBIT/LabGUI.git
```

it can be updated by:

```
git submodule update --remote LabGUI
```

or switched to the QT5 branch with:

```
git config -f .gitmodules submodule.LabGUI.branch QT5
git submodule update --remote LabGUI
```