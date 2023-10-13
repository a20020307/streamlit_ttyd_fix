import platform
import subprocess

import psutil
from port_for import get_port
from streamlit.components.v1 import iframe





def get_ttyd():

    ttyd='/usr/local/bin/ttyd'

    return ttyd


def terminal(
    cmd: str = "echo terminal-speaking... && sleep 99999", 
    host: str = "http://localhost",
    port: int = 7681,
    exit_on_disconnect: bool = True,
    height: int = 400,
):
    assert type(port) == int

    if port == 0:
        port = get_port((5000, 7000))

    flags = f"-port {port} -W"
    if exit_on_disconnect:
        flags += "--once "

   
  

    ttydproc = subprocess.Popen(
        f"ttyd {flags} {cmd}",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    iframe(f"{host}:{port}", height=height)

    return ttydproc, port
