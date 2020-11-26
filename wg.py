def wgfunk(god):
    if god % 4 == 0 or (god % 100 == 0 and god % 400 != 0):
        return 'visokosnii'
    else:
        return 'ne visokosnii'