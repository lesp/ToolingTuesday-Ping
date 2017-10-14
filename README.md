# ToolingTuesday-Ping

Simple application to show off how the Halo terminal spinner for Python can be used to advise the user on the success or failure of a ping request.

It works like this!
![alt](https://raw.githubusercontent.com/lesp/ToolingTuesday-Ping/master/halo-demo.gif)

The ping.py file will need to be made executable, on Linux we can do this with.
```
sudo chmod +x ping.py
```
Then run the application, with the URL or IP address as an argument.

```
./ping.py google.co.uk
```
or
```
./ping.py 8.8.8.8
```

This project uses the [Halo](https://github.com/ManrajGrover/halo) spinner library.


