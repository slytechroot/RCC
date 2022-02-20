if __name__ == '__main__':

foo = ExampleClass(1)
bar = ExampleClass(2)

    # print the instance attribute of the object foo
    print (foo.istance_attr)
    #1
    #print the instance attribute of the object var
    print (bar.instance_attr)
    #2
    #print the class attribute of the class ExampleClass as a property of the class itself 
    print (ExampleClass.class_attr)
    #0
    #print the classattribute  of the class as a proporty of the objects foo,bar
    print (bar.class_attr)
    #0
    print (foo.class_attr)
    #0
    # try to print instance attribute as a class property
    print (ExampleClass.instance_attr)
    #AttributeError: type object 'ExampleClass' has no attribute 'instance_attr'