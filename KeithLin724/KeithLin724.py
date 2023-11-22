"""Welcome to Reflex!."""

from KeithLin724 import styles

# Import all the pages.
from KeithLin724.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
