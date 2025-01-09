def getPasserRating(filename):
    """
    a function that reads a csv file with qb stats and returns a dict of qb names and passer ratings.

    args:
        filename (str): name of the csv file

    returns:
        dict: dict with qb names (str) as keys and passer ratings (float) as values
    """

    # dict to store qb names and passer ratings
    passer_ratings = {}

    # open file, handle file not found error
    try:
        with open(filename, 'r') as f:
            # iterate over lines in file
            for line in f:
                # ignore lines starting with #
                if line.startswith('#'):
                    continue

                # split line by comma
                try:
                    data = line.strip().split(',')
                except:
                    raise ValueError("invalid file format, check for commas")
                # check if line has 6 entries, raise error if not
                if len(data) != 6:
                    raise ValueError("invalid file format, check line length")

                # get qb name and stats
                try:
                    name, att, comp, yds, td, inter = data
                except:
                    raise ValueError("invalid file format, check data types")

                # check for duplicate qb names, raise error if found
                if name in passer_ratings:
                    raise KeyError("duplicate player name found")

                # convert stats to int, handle type errors
                try:
                    att = int(att)
                    comp = int(comp)
                    yds = int(yds)
                    td = int(td)
                    inter = int(inter)
                except ValueError:
                    raise ValueError("invalid file format, check data types")

                # calculate a, b, c, d
                a = ((comp / att) - 0.3) * 5
                b = ((yds / att) - 3) * 0.25
                c = (td / att) * 20
                d = 2.375 - ((inter / att) * 25)

                # cap values at 2.375 and 0
                a = min(a, 2.375)
                a = max(a, 0)
                b = min(b, 2.375)
                b = max(b, 0)
                c = min(c, 2.375)
                c = max(c, 0)
                d = min(d, 2.375)
                d = max(d, 0)

                # calculate passer rating
                passer_rating = ((a + b + c + d) / 6) * 100

                # add qb name and passer rating to dict, round to 1 decimal place
                passer_ratings[name] = round(passer_rating, 1)

    except FileNotFoundError:
        raise FileNotFoundError("file not found")

    # return dict
    return passer_ratings