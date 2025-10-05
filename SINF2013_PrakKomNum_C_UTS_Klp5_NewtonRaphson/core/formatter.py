import re

def format_persamaan(teks):
    teks = teks.replace("^", "**").replace("=0", "").strip()
    teks = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', teks)
    teks = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', teks)
    return teks
