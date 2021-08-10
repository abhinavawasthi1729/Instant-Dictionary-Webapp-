import justpy as jp
import sys
sys.path.append('E:\Python projects\Instant-dictionary-webapp')
from definition import Definition
from webapp.layout import DefaultLayout

class Dictionary:
    path= "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind= True)

        lay = DefaultLayout(a=wp, view = "hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container,  classes = "bg-gray-200 h-screen")
        jp.Div(a=div, text= "Instant dictionary", classes= "text-4xl m-2")
        jp.Div(a= div, text="Get definition of any english word", classes="text-lg p-2")
        input_div = jp.Div(a=div )
        output = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        user_input = jp.Input(a=input_div, placeholder = "type a word", output = output,
                classes = "m-2 bg-gray-100 border-2 border-gray-200 rounded "
                        "w-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4")
        # jp.Button(a=div, text="find", click = cls.find, user_input = user_input, output = output, 
        # classes= "border border-blue-500 m-2 py-1 px-4"
        #  " rounded text-blue-600 hover:bg-red-500"
        #  " hover:text-white")
        user_input.on('input', cls.find)
        return wp

    @staticmethod
    def find(widget, msg):
        term = widget.value
        definition_obj = Definition(term)
        result = definition_obj.get()
        # print(isinstance(result, str))
        widget.output.text =''
        if (isinstance(result, str)):
            widget.output.text += result
        else :
            index =1
            for item in result: 
                widget.output.text += f"{index} {item} \n "
                index +=1

        # widget.output.text = term
       
    

