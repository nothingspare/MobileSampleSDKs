'''
 CustomersLib

 This file was automatically generated by APIMATIC BETA v2.0 on 09/17/2014
'''
class APIException(Exception):

    def __init__(self, reason , responseCode):
        '''

        :param reason: String containing the reason for raising an exception
        :param code:  The HTTP response code from the API request
        '''
        Exception.__init__(self, reason)
        self.responseCode= reason



    def getResponseCode(self):
        '''
        The HTTP response code from the API request

        :returns: http response code
        :rType: int
        '''
        return self.responseCode


    def getReason(self):
        '''
        The reason for raising an exception
        
        :returns: the reason for raising an exception
        :rtype: str
        '''
        return self.message