# Navigation bar
import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(
            html.Img(
                src="assets/golf_flag_header.png",
                alt="Source Code",
                id="golf-flag-header",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="assets/github-mark-white.png",
                    alt="Source Code",
                    id="github-logo",
                ),
                href="https://github.com",
                target="_blank",
                className="p-1",
            )
        ),
    ],
    brand="Mills Golf Stats",
    brand_href="/",
    id="navbar",
    color="dark",
    dark=True,
)
