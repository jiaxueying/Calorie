"""
admin.views
"""

from calorie.api import APIView


class Test(APIView):
    '''
    测试
    '''

    def get(self, request):
        '''
        get方法
        '''
        return self.success()
