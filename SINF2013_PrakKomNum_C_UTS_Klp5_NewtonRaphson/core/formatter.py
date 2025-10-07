

def format_persamaan(teks):
    teks = teks.replace("^", "**").replace("=0", "").strip()
    teks = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', teks)
    teks = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', teks)
    return teks

def fmt_excel(v):
    try:
        return f"{float(v):.9f}".rstrip('0').rstrip('.') if '.' in f"{float(v):.9f}" else f"{float(v):.9f}"
    except:
        return str(v)
