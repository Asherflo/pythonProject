import json


class Custom(dict):
    def __init__(self, *args, **kwargs):
        super(Custom, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(F"key{key} already exist")
        else:
            super().__setitem__(key, value)
            with(open("temp.txt", "w")) as fil_obj:
                json.dump(a, fil_obj)


a = Custom()
a["key"] = "Value"
a["good"] = "good"
a["god"] = "good"
a["age"] = 98

