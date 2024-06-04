import sys, os, time, subprocess
sys.path.append(os.getcwd())
from halo import Halo
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from threading import Thread
from rich.progress import Progress, BarColumn
from tqdm import tqdm
import platform