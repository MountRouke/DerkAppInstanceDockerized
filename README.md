# DerkAppInstance Dockerized

This is an example of how to run the DerkAppInstance in a Docker instance.
Note: This uses xvfb, which means it's all running on the CPU. To use GPU-acceleration
we'd need something like virtualgl.

Known issues:

- For some reason it runs out of texture memory when using xvfb. The solution is to run app.reload() between episodes (see main.py).
