def table(function):
    def data_prettier(self, vertical_data=[]):
        table_string = ""
        data = self.data
        titles = data.keys()
        values = data.values()
        _list_values = []
        _dict_values_spacing = {}
        _vertical_values_spacing = {}
        _values_spacing = []
        _values_spacing_vertical = []
        for _, new_val in data.items():
            _list_values.append(len([item for item in new_val if item]))
        for i in range(-1, max(_list_values)):
            for title in titles:
                for key, value in data.items():
                    if not title in _dict_values_spacing :
                        _dict_values_spacing[title] = []
                    if key == title:
                        _dict_values_spacing[title].append(len(value[i]))
        for i in range(0, len(vertical_data)):
            _values_spacing_vertical.append(len(vertical_data[i]))
        for i in range(-1, max(_list_values)):
            if len(vertical_data) > 0:
                row = " " * (max(_values_spacing_vertical) + 2)  
            else:
                row = " " * (len(str(max(_list_values))) + 2) 
            if i != -1:
                if i < 10:
                    if len(vertical_data) > 0:
                        row = vertical_data[i] + " " * (max(_values_spacing_vertical) - len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * (len(str(max(_list_values))) + 1)
                else:
                    if len(vertical_data) > 0:
                        row = vertical_data[i] + " " * (max(_values_spacing_vertical) - len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * len(str(max(_list_values)))
            for title in titles:
                if i != -1:
                    for key, value in data.items():
                        if key == title:
                            row += value[i] + " " * (max(_dict_values_spacing[title]) - len(str(value[i])) + 2)
                else:
                    row += title + " "*(max(_dict_values_spacing[title]) - len(title) + 2)
            table_string += row + "\n"
        return table_string
    return data_prettier
