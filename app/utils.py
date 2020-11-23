from IPython.display import HTML, display
import tabulate

def as_table(table, headers=()):
    html = HTML(tabulate.tabulate(table, tablefmt='html', headers=headers))
    return display(html)