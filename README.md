# pyWooting
Wooting RGB control and Analog Reader Python 3 Wrapper

## Getting Started
To get started, you will need a working python version. I'm not telling you where to find python, if you're confused about that, this module is too deep water for you.

Then before getting my module, you will need the DLL files for writing and reading the keyboard, and for that you have two options.

And the two options are:
* Downloading the pre-built DLL files by Jeroen that matches your OS(and matching bit number)

* Downloading the source code for analog reading and RGB control from [Analog Reader](https://github.com/PastaJ36/wooting-analog-reader) and [RGB-controller](https://github.com/PastaJ36/wooting-rgb-control) made by Jeroen(PastaJ36). Once downloaded, open them up with Visual Studio and compile them to make the

Personally I like to have the source code at hand, if I wanna edit it or add new things. But either way works, so make your choice.

With that said, you should have the DLL files and my module downloaded. All you have to do at this point is to put the two DLL files and my module into your project.

### Sample Code

To get start with the module, you import it and start it.
```python
from pyWooting import KeyboardReader, KeyboardRGBControl, WootingKey

KeyboardReader.start(dll_file="wooting-analog-reader.dll") # Feel free to write another path here if you add it elsewhere.
KeyboardRGBControl.start(dll_file="wooting-rgb-reader.dll")

print("Keyboard connected:", KeyboardReader.is_wooting_connected(), KeyboardRGBControl.is_wooting_connected())
```

If this prints `Keyboard connected: True, True`

That means everything is in order and you have installed it correctly.

I'm not gonna go over everything and leave the rest up to you.

## Version 1.0

The first version of the wrapper.

## Authors

* **BattleCisco aka Adde r2** - *Initial work* - [BattleCisco](https://github.com/BattleCisco)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Simon and Dommy from the Discord Server
* The Wooting Guys (especially Jeroen aka PastaJ36)