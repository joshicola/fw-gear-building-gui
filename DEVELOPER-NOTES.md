# gear-building-gui

These are notes to assist in developing and maintaining the `Gear-Building GUI` in the absence of the original developer.

This will not be a complete introduction to GUI programming in Python or the myriad of other options to do so (Pyside, tktl, etc.). This document aims, instead, to quickly direct the developer/maintainer to resources that most readly facilitate that development.

## PyQt5

The `requirements.txt` of this repository contains the version of tools that this application is built upon. However, installation of the GUI Designer (**QT Designer**) is not included in these resources for Mac OS X.

### PyQt5 Designer

Multiple resources exist for installing the PyQt5 Designer on various platforms:

* linux: https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff
* os x: https://stackoverflow.com/questions/46542326/installing-pyqt5-incl-qt-designer-on-macos-sierra
* windows: https://build-system.fman.io/qt-designer-download

### Simple Example

With the a PyQt5 Form designed and ready for execution, it is important to have the functional elements perform actions.  This is going to occur from "binding" events and signals to the functions that will perform the desired behavior.

```
cbo_type.currentIndexChanged.connect(config_type_changed)
```

The above code connects the `currentIndexChanged` event of the combo box `cbo_type` to a function `config_type_changed`.

## Code Structure

The project is divided into various sections to assist with ease of use.

### Top-Level

On the top-level, there is the `GearBuilderGUI.py`. This is contains the central application object and reference to the main form.  It is intended to be a brief reference to the functionality of the three tabs.  These three tabs representing the necessary components of a gear: The Manifest, The Dockerfile, and the Run Script.

As with the other form components, the `.ui` file that defines the form and all of the tabs resides in `./gear_builder_gui/pyqt5_ui/`. We will revisit this later.

### gear_builder_gui

The `./gear_builder_gui` directory contains all of the functionality and resources for the gear components. In addition to a file named for each component (`manifest.py`, `dockerfile.py`, and `script_management.py`) there are two manifest-related files for adding and editing the input and configuration sections of the manifest (`config_dialog.py` and `input_dialog.py`).

The `config_dialog.py` and `input_dialog.py` files contain class structures and binding functions for dialog forms (`config.ui` and `inputs.ui`) in the `./gear_builder_gui/pyqt5_ui/` directory. These are pop-up dialogs that must be accepted or canceled before any other activity can occur.

### default_templates

The `./default_templates` directory contain [mustache](https://mustache.github.io/) templates for the Dockerfile (`Dockerfile.mu`), the README.md (`README.md.mu`), and the requirements.txt (`requirements.txt.mu`). 

Each of these templates (as with the script library, below) depends on elements defined in a sub-dictionary related to the associated gear component element.  Each component has its own sub-dictionary in the gear-configuration dictionary:
```
{
    "manifest": {
        ...
    },
    "dockerfile": {
        ...
    },
    "script": {
        ...
    }
}
```

### script_library

The `./script_library` subdirectory contains structural code templates for gears.  

Each library is named for its template (e.g. `bids-app-template`). The files within the script library fall into three categories:

1. Mustache Templates to be rendered.
2. Files or directories to be copied.
3. Configuration files defining the script-template or the whole gear.

The current script-template definition is embedded within the script_management.py file. These are intended to be exported to the script-template library's directory. The script-library can have templated files that override the default templates (e.g. Dockerfile.mu, README.md.mu).

Current script-template definition looks like:
```
{
    "template_name": "Bids App Template",
    "base_dir": "script_library/bids-app-template/",
    "tags": {
        "bids_command": "echo",
        ...
    },
    "templates": [
        "run.py"
    ],
    "copy": [
        "utils",
        "LICENSE"
    ]
}
```

### TODO:

* Place script-template definition into script-template directory. Display as available only if valid.
* Create schema validators for
  * script-template definition json
  * whole-gear definition json

* Create tag-discovery for a new script-template.
* Enforce versions on pip requirements.txt interface