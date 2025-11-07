# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP3 - Enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp3_enumeration.forms import TelnetForm, NmapForm, Enum4linuxForm


@login_required
def srie_tp3_enumeration():
    """
        Logic for /srie/tp3_enumeration/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)

@login_required
def srie_tp3_Telnet():
    """
        Logic for view/templates/srie/tp3_enumeration/Telnet.html
        Login is required to view this page

        The telnet command is a network utility used to connect to remote devices and servers over the Telnet protocol. It allows users to establish an interactive communication session, often for testing and troubleshooting network services.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Telnet.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TelnetForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data
        port = content["form"].port.data

        content["command_executed"] = f"telnet {host} {port}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Telnet')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Telnet')+'.html', content=content)

@login_required
def srie_tp3_Nmap():
    """
        Logic for view/templates/srie/tp3_enumeration/Nmap.html
        Login is required to view this page

        The nmap command, short for Network Mapper, is a powerful open-source tool used for network discovery, auditing, and security analysis. Here, it allows to detect the operating system used by the victim.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Nmap.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data

        content["command_executed"] = f"sudo nmap -O {host}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Nmap')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Nmap')+'.html', content=content)

@login_required
def srie_tp3_Enum4linux():
    """
        Logic for view/templates/srie/tp3_enumeration/Enum4linux.html
        Login is required to view this page

        enum4linux is a Linux-based tool used to gather information from Windows systems by leveraging SMB (Server Message Block) and NetBIOS protocols. Here, it allows to get a list of users

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Enum4linux.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": Enum4linuxForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data

        content["command_executed"] = f"enum4linux -U {host}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Enum4linux')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Enum4linux')+'.html', content=content)