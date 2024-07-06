import sys, os, time, subprocess
sys.path.append(os.getcwd())
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from threading import Thread
from rich.progress import Progress, BarColumn
from tqdm import tqdm
import platform
import http.server
import socketserver
import socket
import time
import plyer
from plyer import notification
from fpdf import FPDF