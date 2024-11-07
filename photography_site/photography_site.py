"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from reflex_motion import motion


class State(rx.State):
    """The app state."""

    ...

def infocard(title,text):
    return rx.center(
        motion(rx.card(
        rx.inset(
            rx.center(rx.heading(title),),
            rx.center(rx.text(text),),
    ),
    width="20vw",
    margin="5vh",
    padding="3vh",), size="2",
    
    while_hover={"scale": 1.1,"rotate":1.1},
    while_tap={"scale": 1.1,"rotate":1.1},
    transition={"type": "spring", "stiffness": 400, "damping": 10},
    ),)

def photocard(photo, aircraft):
    return rx.center( motion( rx.card(
        rx.inset(
            rx.image(
                src=photo,
                width="100%",
                height="auto",
                border_radius="1em",
            ),
            rx.center(rx.heading(aircraft, spacing="5", padding="1em", size="7")),
        ),
        width="70vh",
        size="5",
        margin="5vh"
    ),
    while_hover={"scale": 1.1,"rotate":1.1},
    while_tap={"scale": 1.1,"rotate":1.1},
    transition={"type": "spring", "stiffness": 400, "damping": 10},
    ),
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack( rx.center(
                rx.heading("Aviation Photography!", size="9"), ),
            rx.text(
                "A collection of aircraft photos I've taken!",
                size="5",
            ),
            spacing="2",
            justify="center",
            min_height="20vh",
        ), rx.divider(),

        infocard("Camera", "Canon T7"),
        infocard("Lens", "EF-S 55-250"),

        photocard("airshow-1.jpg", "United Boeing 777-300"),
        photocard("sfo.jpg", "Korean Air Boeing 777-300"),
        photocard("airshow-f22.jpeg", "USAF F-22 Raptor"),
        photocard("sunset1.jpg", "WestJet Boeing 737-800"),
        photocard("sunset2.jpg", "WestJet Boeing 737-800"),
    )

style = {
    "background": "linear-gradient(210.00deg, #261C15 0.75%, #344664 88.52%)",
}

app = rx.App(style=style)
app.add_page(index)
