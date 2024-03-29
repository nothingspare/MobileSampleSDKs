'''
CustomersLib

This file was automatically generated by APIMATIC BETA v2.0 on 09/17/2014
'''
import jsonpickle
import re

class APIHelper:


    @staticmethod
    def jsonSerialize(obj):
        '''
        JSON Serialization of a given object
       
        :type obj: object
        :return: JSON String
        :rtype: str
        '''
        if obj is None:
            return None
        return jsonpickle.encode(obj,False)

    @staticmethod
    def jsonDeserialize(json):
        '''
        Returns a object that is deserialised into a dictionary or primitive type

        :param json: json String
        :type json: str
        :return: primitive or dictionary
        :rtype: primitive or dictionary
        '''

        if json is None:
            return None

        return jsonpickle.decode(json)

    @staticmethod
    def appendUrlWithTemplateParameters(url, parameters ):
        '''
        Replaces template parameters in the given url

        :param url: The query url string to replace the template parameters
        :type url: str
        :param parameters: The parameters to replace in the url
        :type parameters: dictionary
        :return: Url with replaced parameters
        :rtype: str
        '''

        #perform parameter validation
        if url is None:
            raise ValueError("url is null")
        if parameters is None:
            return url

        #iterate and replace parameters
        for key in parameters:

            replaceValue = ""

            #load parameter value
            if parameters[key] is not None :

                replaceValue = parameters[key]
            url = url.replace('{{{0}}}'.format(key),str(replaceValue))


        return url


    @staticmethod
    def appendUrlWithQueryParameters(url, parameters ):
        '''
        Appends the given set of parameters to the given query string

        :param url: The query url string to append the parameters
        :type url: str
        :param parameters:The parameters to append
        :type parameters: dictionary
        :return: Url with appended query parameters
        :rtype: str
        '''

        #perform parameter validation
        if url is None:
            raise ValueError("url is null")
        if parameters is None:
            return url

        #does the query string already has parameters
        hasParams = '?' in url

        #iterate and replace parameters
        for key in parameters:

            #ignore null values
            if parameters[key] is None:
                continue

            #if already has parameters, use the &amp; to append new parameters
            separator = '&' if hasParams else '?'

            url = url+'{0}{1}={2}'.format(separator,key,str(parameters[key]))

            #indicate the url has params
            hasParams=True


        return url

    @staticmethod
    def cleanUrl(url):
        '''
        Validates and processes the given query Url to clean empty slashes

        :param url:The given query Url to process
        :type url: str
        :return: Clean Url as string
        :rtype: str
        '''
        
        #ensure that the urls are absolute
        regex = "^https?://[^/]+"
        match =  re.match(regex, url)
        if match is None:
            raise ValueError('Invalid Url format.')

        #remove redundant forward slashes
        protocol = match.group(0)
        queryUrl = url[len(protocol):]
        queryUrl = re.sub("//+", "/",queryUrl);

        return protocol + queryUrl
        return queryUrl