def replicate():
    code = '''def replicate():
    code = {q}{code}{q}
    with open("replica.py", "w") as f:
        f.write(code.format(q=chr(39), code=code))

if __name__ == "__main__":
    replicate()
    print("Replication complete. New file created: replica.py")
'''''
    with open("replica.py", "w") as f:
        f.write(code.format(q=chr(39), code=code))

if __name__ == "__main__":
    replicate()
    print("Replication complete. New file created: replica.py")
