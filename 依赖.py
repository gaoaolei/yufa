https://blog.csdn.net/NikoHsu/article/details/128521246


# 当前项目的所有库
# 安装pipreqs
#
# pip install pipreqs
#
# 装好之后切换到项目根目录下，执行下面命令：
#
# pipreqs ./
#
# 正常的话应该会在项目根目录下生成一个requirements.txt文件
#
# 如果出现unicode问题，通过下面命令解决：
#
# pipreqs ./ --encoding=utf-8
#
# 当项目里存在requirements .txt文件时，执行会命令会提示警告，这时需要在执行命令中增加"–force"参数。执行以下语句：
#
# pipreqs ./ --encoding=utf-8 --force
#
# 如果生成的requirements.txt文件有个别包漏掉，这时可以检查一下缺失的包名，将包名手工加到文件中。
#




# 导出所有的第三方包（适用于独立的虚拟环境）
# pip freeze >requirements.txt
#
# 会生成当前python环境安装的所有安装包，生成的文件名可以任意命名，安装的时候也要用这个名字
#
# pip freeze 会附带上一些不需要的包，以及某些包依赖的包~





# 使用
# 在新环境部署项目时在对应目录 pip install -r requirement.txt 即可
