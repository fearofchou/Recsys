from progressbar import *               # just a simple progress bar

def mybar(title,max_val):
    widgets = [title, Percentage(), ' ', Bar(marker='#',left='[',right=']'),
    ' ', ETA()] #see docs for other options

    pbar = ProgressBar(widgets=widgets, maxval=max_val)
    pbar.start()

    return pbar
