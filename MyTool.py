# -*- coding: utf-8 -*-
import sublime, sublime_plugin, os

class TCommand(sublime_plugin.TextCommand): #跳转到相应model或者controller
    def run(self, edit):
        fileName = self.view.file_name() #文件名 含具体路径
        fileName = fileName.replace('\\', '/')

        openFileName = '' #将要打开的文件名

        if fileName.find('controllers') != -1: #当前文件为controller
            tmpName = os.path.basename(fileName).replace('.php', '')
            modelFileName = tmpName[0:(tmpName.find('_controller')-1)] + '.php'
            openFileName = fileName[0:fileName.find('controllers')] + 'models/' + modelFileName
        elif fileName.find('models') != -1: #当前文件为model
            ctrlFileName = os.path.basename(fileName).replace('.php', '') + 's_controller.php'
            openFileName = fileName[0:fileName.find('models')] + 'controllers/' + ctrlFileName
        if openFileName != '':
            self.view.window().open_file(openFileName, sublime.ENCODED_POSITION) #打开相关文件

# class T1Command(sublime_plugin.TextCommand): #添加tlog
#     edit = None
#     def run(self, edit):
#         self.edit = edit
#         self.view.window().show_input_panel("Enter TLog:", "", self.on_done, None, None)

#     def on_done(self, result): #输入完，添加log信息
#         if len(result) > 0:
#             logTxt = "\n$this->log(\"" + result + "\", 't');"
#             for region in self.view.sel():
#                 line = self.view.line(region)
#                 self.view.insert(self.edit, line.end(), logTxt)

# view.settings().get('default_encoding')

class T2Command(sublime_plugin.TextCommand): #查文件格式
    edit = None
    def run(self, edit):
        sencoding = self.view.encoding()
        sublime.message_dialog(u'当前文件编码为：'+sencoding)
        #self.view.window().show_quick_panel([u'当前文件编码为：'+sencoding], None, sublime.MONOSPACE_FONT)

class DiffCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		trunkPath = 'D:/project/sanguo_mobile_2_server/trunk'
		brPath = 'D:/project/sanguo_mobile_2_server/br'
		fileName = self.view.file_name() #文件名 含具体路径
		fileName = fileName.replace('\\', '/').split('sanguo_mobile_2_server')[1]
		f1 = fileName.split('trunk')
		f2 = fileName.split('br')
		lenf1 = len(f1)
		lenf2 = len(f2)
		if lenf1==2:
			fileName = f1[1]
			fileName1 = trunkPath + fileName
			fileName2 = brPath + fileName
		if lenf2==2:
			fileName = f2[1]
			fileName1 = brPath + fileName
			fileName2 = trunkPath + fileName
		sh = '"C:\Program Files (x86)\WinMerge\WinMergeU.exe" ' + fileName1 + ' ' + fileName2
		#print(sh)
		os.system(sh)
#		print(fileName1)
#		print(fileName2)

class HelloCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.message_dialog(u'Hello 世界!')