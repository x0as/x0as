

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Info")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

    Slow(f"""
    {INFO_ADD} Name Tool     :  {white}x0as
    {INFO_ADD} Type Tool     :  {white}{type_tool}
    {INFO_ADD} Version       :  {white}{version_tool}
    {INFO_ADD} Copyright     :  {white}x0.ase?
    {INFO_ADD} Coding        :  {white}{coding_tool}
    {INFO_ADD} Language      :  {white}{language_tool}
    {INFO_ADD} Creator       :  {white}Liam Joanne?
    {reset}""")

    license_read = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open 'Just Type N lil bro.' ? (n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)