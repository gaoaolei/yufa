
def start():
    import jpype
    # from django.conf import settings
    jvmPath = jpype.getDefaultJVMPath()
    args = [jvmPath, '-ea']
    # args.append('-Djava.class.path=D:/backend1/file/jar/testtools-jar.jar')
    args.append('-Djava.class.path=D:/qcj-server.jar')
    args = ["java","-jar","D:/qcj-server.jar" ]
    print(args)
    # jpype.startJVM(*args)
    import os
    os.system("d:&& java -jar D:\qcj-server.jar")

start_jvm()
