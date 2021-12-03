# get count of pandas dataframe column depending on column value match
def get_count(df, col_name, val):
    return len(df[df[col_name] == val])


# get square value
def get_square(val):
    try:
        return val ** 2
    except TypeError:
        raise "get_square function argument should be valid numeric value"
