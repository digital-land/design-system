def is_current_page(path, slug):
    if path.endswith(slug):
        return True
    return False
