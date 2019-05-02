class Constant(object):
    """
    一些常量
    """
    def __init__(self):
        self.month = [
            {'key': '0', 'value': '全部'},
            {'key':'1','value':'一月'},
            {'key':'2','value':'二月'},
            {'key':'3','value':'三月'},
            {'key':'4','value':'四月'},
            {'key':'5','value':'五月'},
            {'key':'6','value':'六月'},
            {'key':'7','value':'七月'},
            {'key':'8','value':'八月'},
            {'key':'9','value':'九月'},
            {'key':'10','value':'十月'},
            {'key':'11','value':'十一月'},
            {'key':'12','value':'十二月'}

        ]
        self.days = [
            {'key': '0', 'value': '全部'},
            {'key': '1', 'value': '一天'},
            {'key': '2', 'value': '两天'},
            {'key': '3', 'value': '三天'},
            {'key': '4', 'value': '三天以上'}
        ]
        self.price = [
            {'key': '0', 'value': '全部'},
            {'key':'1','value':'1000以下'},
            {'key': '2', 'value': '1000-2000'},
            {'key': '3', 'value': '2000-3000'},
            {'key': '4', 'value': '3000-4000'},
            {'key': '5', 'value': '4000以上'}
        ]
        self.target_url = {
            'tc':'/identical_list',
            'dt':'/short_list',
            'ct':'/long_list'
        }

CONSTANT = Constant()
