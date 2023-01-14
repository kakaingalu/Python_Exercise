if __name__ == "__main__":
    import hidden_4

    for a in hidden_4:
        if a.startswith('__'):
            continue
        print(a)