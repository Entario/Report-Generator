class Config:
    def __init__(self,path_to_file):
        self.path_to_file = path_to_file
    def get_dict(self):
        with open(self.path_to_file,'r') as f:
            lines = f.readlines()
            dict = {}
            for line in lines:
                name,value = line.split('=')
                value=value.strip('\n')
                dict[name] = value
            return dict
