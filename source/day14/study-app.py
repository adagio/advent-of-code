import subprocess

# exec(open("study/sciyoshi.py").read())

# exec(open("study/jead.py").read())

# exec(open("study/vacation9.py").read())

# exec(open("study/aspittel.py").read())

arg1 = 'data/input1.plain'
args = [
    'python',
    'study/fogleman.py',
    arg1
]
subprocess.call(args)
