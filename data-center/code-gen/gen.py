# -*- coding:utf-8 -*-
import json


class CodeGenerator:
    fieldMapping = {}
    string = ['string', 'String']
    integer = ['bigint', 'int']
    double = ['double']
    date = ['timestamp']
    path = 'data-center/result'

    def createFile(self, package, className, jsonFileName):
        text = self.handle(package, className, jsonFileName)
        fileName = self.path + '/'+className+'.java'
        file = open(fileName, 'w+', newline='', encoding='UTF-8')
        for t in text:
            # 写文件
            file.write(t+'\r\n')
            file.flush()

        file.close()

        mappingStr = json.dumps(self.fieldMapping, sort_keys=True,
                                indent=4, separators=(',', ': '))
        print(mappingStr)
        fieldMappingFile = self.path + '/'+className+'.json'
        mappingFile = open(fieldMappingFile, 'w+',
                           newline='', encoding='UTF-8')
        mappingFile.write(mappingStr)
        mappingFile.close()

    def handle(self, package, className, jsonFileName):
        jsonObj = self.getJson(jsonFileName)
        text = []
        text.append('package '+package+';')
        text.append('')
        text.append('/**')
        text.append(' * ' + jsonObj['data']['nameEn'])
        text.append(' * ' + jsonObj['data']['nameCn'])
        text.append(' */')
        text.append('@lombok.Data')
        text.append('public class ' + className + ' {')

        for jsonObj in jsonObj['data']['resourceColumns']:
            str = self.jsonToJavaField(jsonObj)
            for s in str:
                text.append(s)

        text.append('}')
        return text

    def getJson(self, jsonFileName):
        ''' data -> resourceColumns[]
        '''
        fileName = 'data-center/code-gen/json/'+jsonFileName+'.json'
        jsonfile = open(fileName, 'r', encoding='UTF-8')
        jsonStr = jsonfile.read()
        jsonObj = json.loads(jsonStr)
        return jsonObj

    def jsonToJavaField(self, jsonObj):
        # 注释
        comment = jsonObj['columnDescription']
        # 类型
        javaType = jsonObj['columnType']
        # 字段名称
        fieldName = jsonObj['columnName']

        # []
        commentStr = self.getCommentStr(comment)
        # []
        fieldStr = self.getFieldStr(javaType, fieldName)
        str = []
        for c in commentStr:
            str.append(c)
        for f in fieldStr:
            str.append(f)
        return str

    def getCommentStr(self, comment):
        commentStr = []
        commentStr.append('')
        commentStr.append('    /**')
        commentStr.append('     * ' + comment)
        commentStr.append('     */')
        return commentStr

    def getFieldStr(self, javaType, fieldName):
        javaType = self.getTypeStr(javaType)
        fieldName = self.getFieldNameStr(fieldName)
        str = []
        str.append('    private {javaType} {fieldName};'.format(
            javaType=javaType, fieldName=fieldName))
        return str

    def getTypeStr(self, javaType):
        if javaType in self.string:
            javaType = 'String'
        elif javaType in self.double:
            javaType = 'Double'
        elif javaType in self.integer:
            javaType = 'Integer'
        elif javaType in self.date:
            javaType = 'java.util.Date'
        return javaType

    def getFieldNameStr(self, sourceName):
        fieldName = sourceName
        if '_' in fieldName:
            fieldName = ''.join(
                map(lambda x: x.capitalize(), fieldName.split("_")))
            fieldName = fieldName[0].lower() + fieldName[1:]
        self.fieldMapping[sourceName] = fieldName
        return fieldName


if __name__ == "__main__":
    # 包名
    package = 'com.yunli.ecology.multiplex.adaptersite.entity.wading.project'
    objs = [
        (package, 'FetchWater', 'dwd_fzr_fss_wr_int_b'),
        (package, 'GroundWater', 'dwd_fzr_fss_wr_gws_b'),
        (package, 'SurfaceWater', 'dwd_fzr_fss_wr_sws_b'),
    ]
    for obj in objs:
        CodeGenerator().createFile(obj[0], obj[1], obj[2])
