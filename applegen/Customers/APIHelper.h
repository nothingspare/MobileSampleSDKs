//
//  APIHelper.h
//  Customers
//
//  This file was automatically generated by APIMATIC BETA v2.0 on 09/17/2014
//
#ifndef APIHELPER
#define APIHELPER

#import <Foundation/Foundation.h>
#import "JSONModel.h"

@interface APIHelper : NSObject

/**
* JSON Serialization of a given object.
* @param	obj		The object to serialize into JSON
* @return	The	serialized Json string representation of the given object */
+ (NSString*) jsonSerialize: (NSObject*) obj;

/**
* JSON Deserialization of the given json string.
* @param	json	The json string to deserialize
* @param	cls		The type of the object to desialize into
* @return	The deserialized object */
+ (JSONModel*) jsonDeserialize: (NSString*) json
                       toClass: (Class) cls;

/**
 * JSON Deserialization of the given json string.into an array of json objects
 * @param	json	The json string to deserialize
 * @return	The deserialized array of json objects */
+ (NSArray*) jsonDeserializeArray: (NSString*) json;

/**
* Replaces template parameters in the given url
* @param	queryBuilder    The query string builder to replace the template parameters
* @param	parameters	The parameters to replace in the url */
+ (void) appendUrl: (NSMutableString*) queryBuilder
         withTemplateParameters: (NSDictionary*) parameters;

/**
* Appends the given set of parameters to the given query string
* @param	queryBuilder	The query url string to append the parameters
* @param	parameters	The parameters to append */
+ (void) appendUrl: (NSMutableString*) queryBuilder
         withQueryParameters: (NSDictionary*) parameters;

/**
 * Validates if the string is null, empty or whitespace
 * @param	str	The string to validate
 * @return	The result of validation */
+ (BOOL) isNullOrWhiteSpace:(const NSString*) str;

/**
* Validates and processes the given Url
* @param    url The given Url to process
* @return   Pre-process Url as string */
+(NSString*) cleanUrl: (NSString*) url;

/**
 * Removes any NSNull value from the given dictionary
 * @param    url The given Url to process */
+(void) removeNullValues: (NSMutableDictionary*) dictionary;

@end

#endif