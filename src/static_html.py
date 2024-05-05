import os, glob

def list_html_files(directory):
    html_files = []
    pattern = os.path.join(directory, '*.html')
    html_files.extend(glob.glob(pattern))
    return html_files