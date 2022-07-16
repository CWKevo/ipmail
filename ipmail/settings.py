APP_NAME = "IPMail"
"""The application name."""
APP_VERSION = "0.0.1"
"""The application version."""

IP_REGEX = r"""^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"""
"""Regex for matching valid IPs."""

WEB_HOST = 'localhost'
"""The hostname to bind the web server to."""
WEB_PORT = 5000
"""The port to bind the web server to."""

USE_HTTPS = False
"""Whether or not to use `https://` schemes."""

DEBUG = True
"""Whether the applications are running in debug mode (will print more information)."""
