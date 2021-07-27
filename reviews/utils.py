def average_rating(rating_list):
    if not rating_list:
        return 0
    return round(sum(rating_list) / len(rating_list))


def initialled_name(obj):
    """obj.first_names='Jerome David', obj.last_names='Salinger'
    => 'Salinger, JD'"""
    initials = "".join([name[0] for name in obj.first_names.split(" ")])
    return "{}, {}".format(obj.last_names, initials)
