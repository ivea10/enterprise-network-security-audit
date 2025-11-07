# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP4 - Gaining Access
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp4_gaining_access.forms import HydraForm, NetcatForm, MetasploitForm


@login_required
def srie_tp4_gaining_access():
    """
        Logic for /srie/tp4_gaining_access/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp4_gaining_access')+'.html', username=username)

@login_required
def srie_tp4_Hydra():
    """
        Handles the logic for view/templates/srie/tp4_gaining_access/Hydra.html
        Login is required to view this page

        Hydra (also known as THC-Hydra) is a popular open-source password-cracking tool used in cybersecurity for conducting brute force attacks or dictionary attacks on network services.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/Hydra.html with content passed as a context variable
        """
    content = {"form": HydraForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        loginPath = content["form"].loginPath.data
        passPath = content["form"].passPath.data
        host = content["form"].host.data
        service = content["form"].service.data
        content["command_executed"] = f"hydra -L {loginPath} -P {passPath} {host} {service} -V"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_Hydra')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_Hydra')+'.html', content=content)

@login_required
def srie_tp4_Netcat():
    """
        Handles the logic for view/templates/srie/tp4_gaining_access/Netcat.html
        Login is required to view this page

        Netcat (often abbreviated as nc) is a versatile networking utility that reads and writes data across network connections.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/Netcat.html with content passed as a context variable
        """
    content = {"form": NetcatForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data
        content["command_executed"] = f"nc {host} 1524"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_Netcat')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_Netcat')+'.html', content=content)

@login_required
def srie_tp4_Metasploit():
    """
        Handles the logic for view/templates/srie/tp4_gaining_access/Metasploit.html
        Login is required to view this page

        Metasploit is a powerful, open-source penetration testing framework used by security professionals, ethical hackers, and attackers to find, exploit, and validate vulnerabilities in systems. It provides a suite of tools for conducting security assessments, performing penetration testing, and developing and executing exploits.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/Metasploit.html with content passed as a context variable
        """
    content = {"form": MetasploitForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        content["command_executed"] = f"msfconsole"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_Metasploit')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_Metasploit')+'.html', content=content)