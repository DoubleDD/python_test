# -*- coding:utf-8 -*-
import json


def createFile(package, className):
    text = handle(package, className)
    fileName = 'data-center/result/'+className+'.java'
    file = open(fileName, 'w+',newline='',encoding='UTF-8')
    for t in text:
        # 写文件
        file.write(t+'\r\n')
        file.flush()
    file.close()


def handle(package, className):
    text = []
    text.append('package '+package+';')
    text.append('')
    text.append('@lombok.Data')
    text.append('public class ' + className + ' {')

    jsonArr = getJson()
    for jsonObj in jsonArr:
        str = jsonToJavaField(jsonObj)
        for s in str:
            text.append(s)

    text.append('}')
    return text


def getJson():
    ''' data -> resourceColumns[]
    '''
    jsonfile = open('data-center/code-gen/json/source.json','r',encoding='UTF-8')
    jsonStr = jsonfile.read()
    jsonObj = json.loads(jsonStr)
    jsonArr = jsonObj['data']['resourceColumns']
    return jsonArr


def jsonToJavaField(jsonObj):
    # 注释
    comment = jsonObj['columnDescription']
    # 类型
    javaType = jsonObj['columnType']
    # 字段名称
    fieldName = jsonObj['columnName']

    # []
    commentStr = getCommentStr(comment)
    # []
    fieldStr = getFieldStr(javaType, fieldName)
    str = []
    for c in commentStr:
        str.append(c)
    for f in fieldStr:
        str.append(f)
    return str


def getCommentStr(comment):
    commentStr = []
    commentStr.append('')
    commentStr.append('    /**')
    commentStr.append('     * ' + comment)
    commentStr.append('     */')
    return commentStr


def getFieldStr(javaType, fieldName):
    javaType = getTypeStr(javaType)
    fieldName = getFieldNameStr(fieldName)
    str = []
    str.append('    private {javaType} {fieldName};'.format(
        javaType=javaType, fieldName=fieldName))
    return str

string = ['string','String']
integer = ['bigint','int']
double = ['double']
date = ['timestamp']

def getTypeStr(javaType):
    if javaType in string:
        javaType = 'String'
    elif javaType in double:
        javaType = 'Double'
    elif javaType in integer:
        javaType = 'Integer'
    elif javaType in date:
        javaType = 'java.util.Date'
    return javaType


def getFieldNameStr(fieldName):
    if '_' in fieldName:
        fieldName = ''.join(
            map(lambda x: x.capitalize(), fieldName.split("_")))
        fieldName = fieldName[0].lower() + fieldName[1:]
    return fieldName


if __name__ == "__main__":
    createFile('com.yunli.ecology.multiplex.adaptersite.entity.wading.project', 'SurfaceWater')
