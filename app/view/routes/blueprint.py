# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Configures the address paths (URL routes)
"""
from flask import Blueprint
from ...controllers.controller import index, login, register, dashboard, logout, about
from ...controllers.srie.tp1_recon_footprint.controller import srie_home, srie_tp1_recon_footprint, srie_tp1_ipaddr, srie_tp1_whois, srie_tp1_TheHarvester
from ...controllers.srie.tp2_scanning_networks.controller import srie_tp2_scanning_networks, srie_tp2_pingaddr, srie_tp2_Nessus, srie_tp2_Nmap
from ...controllers.srie.tp3_enumeration.controller import srie_tp3_enumeration, srie_tp3_Telnet, srie_tp3_Nmap, srie_tp3_Enum4linux
from ...controllers.srie.tp4_gaining_access.controller import srie_tp4_gaining_access, srie_tp4_Hydra, srie_tp4_Netcat, srie_tp4_Metasploit
from ...controllers.user_profile.controller import user_profile
from ...controllers.toolbox.controller import toolbox_home
from ...controllers.toolbox.wtforms.controller import toolbox_wtforms_home, toolbox_wtforms_user_reg_form, toolbox_wtforms_upload_form  
from ...controllers.toolbox.database.controller import toolbox_database_home, toolbox_database_insert_data  

blueprint = Blueprint('blueprint', __name__, template_folder='../templates', static_folder='../../assets')

# Home
blueprint.route('/')(index)
blueprint.route('/login', methods=['GET', 'POST'])(login)
blueprint.route('/register', methods=['GET', 'POST'])(register)
blueprint.route('/dashboard', methods=['GET', 'POST'])(dashboard)
blueprint.route('/about', methods=['GET', 'POST'])(about)
blueprint.route('/logout', methods=['GET', 'POST'])(logout)

# User Profile
blueprint.route('/user_profile/user_profile', methods=['GET', 'POST'])(user_profile)

# SRIE
blueprint.route('/srie/home', methods=['GET', 'POST'])(srie_home)

# TP1 - Reconnaissance / Footprint
blueprint.route('/srie/tp1_recon_footprint/home', methods=['GET', 'POST'])(srie_tp1_recon_footprint)
blueprint.route('/srie/tp1_recon_footprint/ipaddr', methods=['GET', 'POST'])(srie_tp1_ipaddr)
blueprint.route('/srie/tp1_recon_footprint/whois', methods=['GET', 'POST'])(srie_tp1_whois)
blueprint.route('/srie/tp1_recon_footprint/TheHarvester', methods=['GET', 'POST'])(srie_tp1_TheHarvester)

# TP2 - Scanning Networks
blueprint.route('/srie/tp2_scanning_networks/home', methods=['GET', 'POST'])(srie_tp2_scanning_networks)
blueprint.route('/srie/tp2_scanning_networks/pingaddr', methods=['GET', 'POST'])(srie_tp2_pingaddr)
blueprint.route('/srie/tp2_scanning_networks/Nmap', methods=['GET', 'POST'])(srie_tp2_Nmap)
blueprint.route('/srie/tp2_scanning_networks/Nessus', methods=['GET', 'POST'])(srie_tp2_Nessus)

# TP3 - Enumeration
blueprint.route('/srie/tp3_enumeration/home', methods=['GET', 'POST'])(srie_tp3_enumeration)
blueprint.route('/srie/tp3_enumeration/Telnet', methods=['GET', 'POST'])(srie_tp3_Telnet)
blueprint.route('/srie/tp3_enumeration/Nmap', methods=['GET', 'POST'])(srie_tp3_Nmap)
blueprint.route('/srie/tp3_enumeration/Enum4linux', methods=['GET', 'POST'])(srie_tp3_Enum4linux)

# TP4 - Gaining Access
blueprint.route('/srie/tp4_gaining_access/home', methods=['GET', 'POST'])(srie_tp4_gaining_access)
blueprint.route('/srie/tp4_gaining_access/Hydra', methods=['GET', 'POST'])(srie_tp4_Hydra)
blueprint.route('/srie/tp4_gaining_access/Netcat', methods=['GET', 'POST'])(srie_tp4_Netcat)
blueprint.route('/srie/tp4_gaining_access/Metasploit', methods=['GET', 'POST'])(srie_tp4_Metasploit)

# Toolbox
blueprint.route('/toolbox/home', methods=['GET', 'POST'])(toolbox_home)
blueprint.route('/toolbox/wtforms/home', methods=['GET', 'POST'])(toolbox_wtforms_home)
blueprint.route('/toolbox/wtforms/user_reg_form', methods=['GET', 'POST'])(toolbox_wtforms_user_reg_form)
blueprint.route('/toolbox/wtforms/upload_form', methods=['GET', 'POST'])(toolbox_wtforms_upload_form)
blueprint.route('/toolbox/database/home', methods=['GET', 'POST'])(toolbox_database_home)
blueprint.route('/toolbox/database/insert_data', methods=['GET', 'POST'])(toolbox_database_insert_data)