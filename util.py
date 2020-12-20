from settings import DEBUG


def debug(msg, end="\n", flush=True):
    if not DEBUG: return
    print(f"[DEBUG] {msg}", end=end, flush=flush)
